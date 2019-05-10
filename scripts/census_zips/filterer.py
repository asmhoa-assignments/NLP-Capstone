
import sys


# returns true if x is a valid float-string or float and bigger than p
def bigger_percent(p, x):
    if x == '-':
        return False
    y = float(x)
    return y > p

# currying so we can pass in p once then pass in lots of xs
filt_perc = lambda p: lambda x: bigger_percent(p, x)

# post processing
trunc_zip = lambda s: s[6:]

get_zip = lambda z, p : (trunc_zip(z),)


# reads the pairs in f
# keeps them if the function comp says the second element of the pair is ok
# does post-processing on the pair
def filter_by(f, comp, post):
    for line in f:
        x, y = line[:-1].split('\t')
        if comp(y):
            yield post(x, y)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w+') as g:
            for item in filter_by(f, filt_perc(float(sys.argv[3])), get_zip):
                g.write('\t'.join(item) + '\n')
    else:
        print('usage: filterer.py infile outfile percentage+')

