
"""script to run all the bounding-box from census-data pieces at once"""

import cluster, extract, filterer, group_boxes, zip_info_matcher

import json, argparse, os

acs_data = "ACS_17_5YR_S0601_with_ann.csv"
zip_loc_data="zip_res.tsv"

parser = argparse.ArgumentParser()
parser.add_argument('--feature', type=int, required=True)#required. which column to read
parser.add_argument('--min_percent', type=int, default=0)
parser.add_argument('--max_dist', type=int, default=0.1)#for zip grouping
parser.add_argument('--box_cutoff', type=int, default=0)
parser.add_argument('--dump_zips')#list of zips passing bar
parser.add_argument('--dump_groups')#zipgroup objs in jsondict format
parser.add_argument('--boxes', required=True)#outfile contianing boxes. required.


"""
plan:
    get feature out of acs and filter on  min_percent
    if dump_zips specified, write zips there
    get location info from zip_loc_data (already processed form zip full data)
    cluster zips with max_dist as distance
    if dump_groups specified, then write group info there
    turn groups into boxes
    write boxes to boxes file
basically, redoing __main__ method of each so we don't have to write to files
"""

# print error message about how we couldn't read the file, then die.
def file_problem(fname, desc):
    print('there was a problem reading the ' + desc + ' file.')
    print('it may be that the file is not there, or there was some other issue.')
    print('please check that the file ' + fname + ' is in this directory and you have read permission')
    exit(1)

args = parser.parse_args()
print(args)

def concat_zinfo((a, b)):
    # concats, and also removes the unhelpful prefix ACS uses
    return a[6:] + '\t' + b + '\n'

keep_first = lambda x, y: x

def write_boxes(f, groups):
    f.write('minLong\tminLat\tmaxLong\tmaxLat\tnumZips\n')
    for group in groups:
        f.write('\t'.join(group_boxes.get_box(group)) + '\n')


### begin script!!

# get zip demographic info from ACS

try:
    with open(acs_data, 'r') as acs:
        zip_dem = [concat_zinfo(x) for x in extract.get_info(acs, args.feature)]
except:# (FileNotFoundError, IOError):
    file_problem(acs_data, 'ACS data')
# write zip demographic info to file if given (do not silently overwrite)
if args.dump_zips:
    if os.path.exists(args.dump_zips):
        q = args.dump_zips + ' already exists. Do you want to overwrite it? y/N'
        if raw_input(q).lower().strip() == 'y':
            with open(args.dump_zips, 'w+') as zdump:
                for z in zip_dem:
                    zdump.write(z)
# filter information
filtered_zip_gen = filterer.filter_by(zip_dem, filterer.filt_perc(args.min_percent), keep_first)
# load zip location info from file
try:
    with open(zip_loc_data, 'r') as zloc:
       zlocs = zip_info_matcher.make_dict(zloc)
except:# (FileNotFoundError, IOError):
    file_problem(zip_loc_data, 'zip coordinates')
# match wtih relevant zips
problems = []
filter_zlocs = []
for z in filtered_zip_gen:
    r = zlocs.get(z)
    if r:
        filter_zlocs.append(r+'\n') # to match what cluster.get_items expects
    else:
        problems.append(z)
# what to do with problems???
#run clustering
zs, zlook = cluster.setup(filter_zlocs)
ds = cluster.get_dists(zs)
cluster.cluster(ds, zlook, maxSpace=args.max_dist)# modifies zlook and ds in place
zgs = list(set(zlook[z] for z in zlook.keys()))
# dump groups if wanted
if args.dump_groups:
    if os.path.exists(args.dump_groups):
        q = args.dump_groups + ' already exists. Do you want to overwrite it? y/N'
        if raw_input(q).lower().strip() == 'y':
            d = cluster.prepare_dump(zlook)
            with open(args.dump_groups, 'w+') as zdump:
                zdump.write(json.dumps(d))
# filter by number min number of zips in group
if args.box_cutoff >= 1:
    zgs = [z for z in zgs if len(z.zs) >= args.box_cutoff]
zgs = sorted(zgs, key=lambda zg: len(zg.zs))
fname = args.boxes
while os.path.exists(fname):
    q = fname + ' already exists. Do you want to overwrite it? y/N'
    if raw_input(q).lower().strip() == 'y':
        with open(fname, 'w') as boxes:
            write_boxes(boxes, zgs)
        print('(over)wrote boxes to ' + fname)
        exit(0)
    r = 'Enter new filename to write to:'
    fname = raw_input(r)
with open(fname, 'w+') as boxes:
    write_boxes(boxes, zgs)
print('wrote boxes to ' + fname)
      


