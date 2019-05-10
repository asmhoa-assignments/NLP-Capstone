
import sys

def examples(f):
    for line in f:
        pieces = line.split(',')
        z = pieces[3]
        lat = pieces[4]
        lon = pieces[9]
        stat = pieces[6]

        yield z, lat, lon, stat

def write_ex(g, (z, lat, lon, stat), write_stat=False):
    g.write(z + '\t' + lat + '\t' + lon)
    if write_stat:
        g.write('\t' + stat)
    g.write('\n')

def main(iname, oname, wstat):
    with open(iname, 'r') as f, open(oname, 'w+') as g:
        for ex in examples(f):
            write_ex(g, ex, wstat)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2], sys.argv[3] == 'y' if len(sys.argv) > 3 else False)
    else:
        print('usage: zip_log_extract.py infile outfile write_stat')

