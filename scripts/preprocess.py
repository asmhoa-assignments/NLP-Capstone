import sys
import re

punc = set(['.', ',', '!', '?'])

def elim_punc(match):
    s = match.group(0)
    if '?' in s:
        return '?'
    elif '!' in s:
        return '!'
    elif '...' in s:
        return '...'
    else:
        return s[0]
i = 0
with open(sys.argv[1], 'r') as raw_file, \
        open(sys.argv[2], 'w') as out_file:
    for line in raw_file:
        line_tkns = line.split('\t')
        index = 6 if len(line_tkns) >= 7 else 0
        body = line_tkns[index]
        body = \
            re.sub(r'( |^)(https?:\/\/|www\.).*?( |$)', ' ', body)
        body = \
            re.sub(r'[\.,\!\?]+', elim_punc, body)
        line_tkns[index] = body
        out_file.write('\t'.join(line_tkns))
        print(i)
        i += 1

        
