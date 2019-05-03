import sys

THRESHOLD = 2
buf = []
acc_length = 0

with open(sys.argv[1], 'r') as raw, \
        open('{0}_length_{1}'.format(sys.argv[1], THRESHOLD), 'w') as out:
    for line in raw:
        components = line.strip().split('\t')

        if len(components) >= 7:
            if acc_length > THRESHOLD:
                for ln in buf:
                    out.write(ln)
            buf = []
            acc_length = 0
            index = 6
        else:
            index = 0

        body = components[index]
        
        acc_length += len(body.split())
        buf.append(line)
    if acc_length > THRESHOLD:
        for ln in buf:
            out.write(ln)
