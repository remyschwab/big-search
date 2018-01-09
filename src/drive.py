import sequence_utils as utils

fasta = utils.fasta_wrap("../input/ref/genome")
genome = utils.build_genome(fasta)
query = 'TGGATGTGAAATGAGTCAAG'
partitions = utils.partition(query)
genome_sa = utils.suffix_array_best(genome)
print genome_sa
