import sys

THRESHOLD = 3 
buf = []
acc_length = 0

with open(sys.argv[1], 'r') as raw, \
        open('{0}_length_{1}'.format(sys.argv[1], THRESHOLD), 'w') as out:
    for line in raw:
        components = line.strip().split('\t')

        # we need to handle for the edge case where the Tweet body is empty
        # which occurs when there are > 2 and < 7 components
        if len(components) > 2:
            if acc_length >= THRESHOLD:
                out.write(' '.join(buf))
                out.write('\n')
                # for ln in buf:
                #     out.write(ln)
            buf = []
            acc_length = 0
            index = 6
            if len(components) < 7:
                continue
        else:
            index = 0

        body = components[index]
        
        acc_length += len(body.split())
        buf.append(line.strip())
    if acc_length > THRESHOLD:
        out.write(' '.join(buf))
        out.write('\n')
        # for ln in buf:
        #     out.write(ln)
