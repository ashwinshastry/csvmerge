import argparse
import itertools

parser = argparse.ArgumentParser(description='Merge CSV files.')
parser.add_argument('files', metavar='files', type=str, nargs='+',
                   help='the list of CSV files')
parser.add_argument('--out', dest='outfile', action='store',
                   help='output file to store the merged file')
parser.add_argument('--skip-header', default=False, action='store_true',
                   help='skip appending headers multiple times to the output file')

args = parser.parse_args()

fout=open(args.outfile,"a")
for line in open(args.files[0]):
    fout.write(line)

for csvfile in itertools.islice(args.files, 1, len(args.files)):
    f = open(csvfile, 'r+')
    if args.skip_header:
        next(f)
    for line in f:
        fout.write(line)
    f.close()
fout.close()
