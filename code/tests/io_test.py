
from utils.io import read_fasta

fasta_filepath = 'data/Bacillus_subtilis_complete_genome.fasta'


def test_read_genome_header():
    demo_genome = read_fasta(fasta_filepath)
    assert demo_genome.contigs[0].header == 'BS.pilon.polished.v3.ST170922'


def test_read_genome_contigs():
    demo_genome = read_fasta(fasta_filepath)
    assert len(demo_genome.contigs) == 1

