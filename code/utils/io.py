

# local file imports
from classes.genome import Genome


# function definitions
def read_fasta(filepath): 
    new_genome = Genome()

    header = ''
    sequence = ''
    
    with open(filepath, 'r') as fp:
        line = fp.readline().rstrip('\n')
        while line:
            if line.startswith('>'):
                if header != '' and sequence != '':
                    new_genome.add_contig(header, sequence)
                header = line.lstrip('>')
                sequence = ''
            else:
                sequence += line
            
            line = fp.readline().rstrip('\n')

        new_genome.add_contig(header, sequence)

    return new_genome