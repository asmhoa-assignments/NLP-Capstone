
import sys, json

def dist((x1, y1), (x2, y2)):
    dx = x1 - x2
    dy = y1 - y2
    return dx**2 + dy**2
    #return (dx**2 + dy**2)**0.5

class ZipGroup:
    def __init__(self, z, lat, lon):
        self.zs = [z]
        self.lats = [lat]
        self.lons = [lon]

    def dist(self, other):
        return min([dist(other, (self.lats[i], self.lons[i])) for i in range(len(self.lats))])

    def add(self, other):
        if other is self:
            return
        self.lats.extend(other.lats)
        self.lons.extend(other.lons)
        self.zs.extend(other.zs)

    def __str__(self):
        return str(self.zs)

    def to_jdict(self):
        d = {}
        d['zs'] = self.zs
        d['lats'] = self.lats
        d['lons'] = self.lons
        return d

    def load_from_dict(self, dct):
        self.zs = dct['zs']
        self.lats = dct['lats']
        self.lons = dct['lons']


def get_dists(lst):
    """Takes in a list of tuples (zip, lat, long)
    makes a nested dict s.t. dct[z1][z2] = dist between z1 and z2
    DOES NOT HAVE dct[z][z] for same z
    """

    dct = {}
    for i in range(len(lst)):
        di = {}
        for j in range(len(lst)):
            if i == j:
                continue # don't repeatself
            d = dist(lst[i][1:], lst[j][1:])
            di[lst[j][0]] = d
        dct[lst[i][0]] = di
    return dct

def get_min_dist(dct, z):
    """Given a dict of not-already-checked distances
    and a goal zip
    gives the zip who is the closest to that one
    """
    m = min(dct[z].keys(), key=dct[z].get)
    return (m, dct[z][m])


def min_overall(dct):
    """ returns smallest value in dict:
    (outer, (val, inner))
    """
    mins = [(z, get_min_dist(dct, z)) for z in dct.keys()]
    #print(mins)
    m = min(range(len(mins)), key=lambda i: mins[i][1][1])
    return mins[m]

def remove_group(dct, lst):
    """removes all pairs in the group from the dict"""
    #print('removing interactions between:', lst)
    #print('before removing:', dct)
    for x in lst:
        for y in lst:
            dct[x].pop(y, 0)
    #print('after removing', dct)

def get_items(f):
    """ reads items, turns zips into strings and lat/long into floats"""
    for line in f:
        pieces = line.split('\t')
        pieces[-1] = pieces[-1][:-1] # take off newline
        yield pieces[0], float(pieces[1]), float(pieces[2])


def setup(f):
    """reads the examples in and makes data structures:
    a list of all the locations,
    and a dict of zip-name-to-ZipGroup object
    """
    zs = []
    zlook = {}
    for it in get_items(f):
        z = ZipGroup(*it)
        zs.append(it)
        zlook[it[0]] = z

    return zs, zlook


def cluster(dists, zlook, maxSpace=0.1):
    """cluster them then return ZipGroups.
    dists: a nested dict of distances
    zlook: a dict from zip numbers to ZipGroups they belong to
    maxSpace: maximum space between two adjacent points in a cluster
    """

    #print('maxSpace', maxSpace)
    m = min_overall(dists)
    #print(m)
    while m[1][1] < maxSpace: # when do we say groups should stay apart?
        # get two closest points and their groups they belong to
        z1, (z2, _) = m
        zg1 = zlook[z1]
        zg2 = zlook[z2]
        # stick them together
        zg1.add(zg2)
        # modify the ones in group 2 to point to full group
        for x in zg2.zs:
            zlook[x] = zg1
        # take all these pairs out of the distances (they're already grouped)
        squish = zg1.zs
        remove_group(dists, squish)

        m = min_overall(dists)

def prepare_dump(zlook):
    s = set(zlook[z] for z in zlook.keys())
    lensort = lambda zg: len(zg.zs)
    gs = sorted([x for x in s], key=lensort)
    res = {'groups': [x.to_jdict() for x in gs]}

    return res

def cluster_and_dump(dists, zlook, maxSpace=0.1):
    cluster(dists, zlook, maxSpace=0.1)
    return prepare_dump(zlook)

# usage: infile, outfile
if __name__ == '__main__':
    if len(sys.argv) > 2:
        with open(sys.argv[1], 'r') as f:
            zs, zlook = setup(f)
        ds = get_dists(zs)
        if len(sys.argv) > 3:
            x = float(sys.argv[3])
            res = cluster_fancy(ds, zlook, maxSpace=x)
        else:
            res = cluster_fancy(ds, zlook)
        with open(sys.argv[2], 'w+') as g:
            g.write(json.dumps(res))
    else:
        print('usage: cluster.py infile outfile')



