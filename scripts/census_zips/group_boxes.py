
from cluster import ZipGroup
import json, sys


def zg_factory():
    while True:
        yield ZipGroup('a', 0, 0)
    
    
def make_zg(dct):
    z = ZipGroup('a', 0, 0)
    z.load_from_dict(dct)
    return z

def load_groups(f):
    j = json.loads(f.read())

    zgf = zg_factory()
    zgs = [make_zg(x) for x in j['groups']]
    return zgs


def get_box(zg):
    minlat = min(zg.lats)
    maxlat = max(zg.lats)
    minlon = min(zg.lons)
    maxlon = max(zg.lons)

    return [str(x) for x in [minlon, minlat, maxlon, maxlat, len(zg.zs)]]

if __name__ == '__main__':
    if len(sys.argv) == 3:
        with open(sys.argv[1], 'r') as f:
            zgs = load_groups(f)
        with open(sys.argv[2], 'w+') as g:
            g.write('minLong\tminLat\tmaxLong\tmaxLat\tnumZips\n')
            for zg in zgs:
                g.write('\t'.join(get_box(zg)) + '\n')
    else:
        print('usage: group_boxes.py zg_dict_file outfile')


