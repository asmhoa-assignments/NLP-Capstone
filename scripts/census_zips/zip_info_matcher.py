

import sys

def make_dict(f):
    d = {}
    for line in f:
        pieces = line.split('\t')
        pieces = pieces[:3]
        d[pieces[0]] = '\t'.join(pieces)+'\n'
    return d


if __name__ == '__main__':
    if len(sys.argv) == 4:
        with open(sys.argv[1], 'r') as f:
            zinfo = make_dict(f)
        with open(sys.argv[2], 'r') as g, open(sys.argv[3], 'w+') as h:
            for line in g:
                r = zinfo.get(line.strip(), None)
                if r:
                    h.write(r + '\t')
                else:
                    print('could not find info for', line.strip())
    else:
        print('usage: zip_info_matcher.py zip_info_file, zip_goals_file, outfile')


