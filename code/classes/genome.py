


# library imports
import random
import sys


# local file imports
from classes.contig import Contig


# class definition
class Genome:
    def __init__(self):
        self.contigs = {}
        self.contig_id = 0
        self.total_length = 0


    def add_contig(self, header, sequence):
        genome_position = self.total_length + 1
        new_contig = Contig(self.contig_id, header, sequence, genome_position)
        self.contigs[new_contig.cid] = new_contig
        self.contig_id += 1
        self.total_length += new_contig.length


    def get_contig_ids(self):
        return list(self.contigs.keys())


    def get_longest_contig(self):
        contig_ids = self.get_contig_ids()
        contig_sizes = []

        for ident in contig_ids:
            contig_sizes.append([ident, self.contigs[ident].length])
        
        contig_sizes.sort(key=lambda x: x[1], reverse=True)
        largest_contig_id = contig_sizes[0][0]

        return self.contigs[largest_contig_id]


    def get_contig_sequence(self, ident):
        return self.contigs[ident].sequence


    def get_random_contig(self, banlist=[]):
        for contig in self.contigs.values():
            if contig.cid not in banlist:
                return contig
        
        sys.exit('could not find appropriate contig after 100 iterations')

    
    def get_contig_by_prob(self, banlist=[]):
        location = random.randint(0, self.total_length)
        for contig in self.contigs.values():
            if contig.cid not in banlist:
                if location > contig.genome_span[0] and location < contig.genome_span[1]:
                    return contig
        return self.get_random_contig(banlist=banlist)






 