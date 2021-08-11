


# class definition
class Contig:
    def __init__(self, cid, header, sequence, genome_position):
        self.cid = cid
        self.header = header
        self.sequence = sequence
        self.length = len(sequence)
        self.genome_span = [genome_position, genome_position + self.length]