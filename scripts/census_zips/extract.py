
import sys

percent_aa = 99

# gets the information out of the file and returns a generator of (zip, col) pairs
# f is a file of information
# col is which column we care about (by index)
def get_info(f, col):
    # supposedly this skips the first two lines
    for _ in range(2):
        next(f)
    for line in f:
        pieces = line.split(',')
        yield pieces[2], pieces[col]

def main(fname, gname, col):
    with open(fname, 'r') as f, open(gname, 'w+') as g:
        for item in get_info(f, col):
            g.write(item[0] + '\t' + item[1] + '\n')

if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
        print('done')
    else:
        print('usage: extract.py input_filename output_filename goal_column_number')


