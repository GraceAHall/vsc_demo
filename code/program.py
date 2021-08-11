

# library imports
import sys

# local file imports
from utils.io import read_fasta


# main
def main(argv):
    fasta_file = argv[0]
    my_fasta = read_fasta(fasta_file)

    print('')
    print(f'filename: {fasta_file}')
    print(f'genome length: {my_fasta.total_length}')
    print(f'num contigs: {len(my_fasta.contigs)}')
    print(f'first contig header: {my_fasta.contigs[0].header}')


if __name__ == '__main__':
    main(sys.argv[1:])
