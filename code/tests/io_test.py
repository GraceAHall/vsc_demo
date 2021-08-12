
from utils.io import read_fasta

bs_filepath = 'data/Bacillus_subtilis_complete_genome.fasta'


def test_read_genome_bs():
    demo_genome = read_fasta(bs_filepath)
    assert demo_genome.contigs[0].header == 'BS.pilon.polished.v3.ST170922'
    assert len(demo_genome.contigs) == 1





