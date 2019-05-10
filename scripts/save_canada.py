import argparse

parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--reference-file',
                    type=str,
                    help='File to check Tweets against',
                    required=True)
parser.add_argument('--input-file',
                    type=str,
                    help='File to check for duplicates',
                    required=True)
parser.add_argument('--output-file',
                    type=str,
                    help='Output filename',
                    required=True)

args = parser.parse_args()

seen = set()
with open(args.reference_file) as ref:
    for line in ref:
        components = line.strip().split('\t')
        tweet_body = components[6]
        seen.add(tweet_body)

with open(args.input_file) as in_file, open(args.output_file, 'w') as out_file:
    for line in in_file:
        components = line.strip().split('\t')
        tweet_body = components[6]
        if tweet_body not in seen:
            out_file.write(line)
