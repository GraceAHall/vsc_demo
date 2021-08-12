
from utils.io import read_fasta

bs_filepath = 'data/Bacillus_subtilis_complete_genome.fasta'
ec_filepath = 'data/Escherichia_coli_complete_genome.fasta'


def test_read_genome_bs():
    demo_genome = read_fasta(bs_filepath)
    assert demo_genome.contigs[0].header == 'BS.pilon.polished.v3.ST170922'
    assert len(demo_genome.contigs) == 1


def test_read_genome_ec():
    demo_genome = read_fasta(ec_filepath)
    assert demo_genome.contigs[0].header == 'N3.1 Escherichia coli ZYMOBIOMICS plasmid'
    assert len(demo_genome.contigs) == 2





