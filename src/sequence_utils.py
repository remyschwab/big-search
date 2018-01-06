import pysam
import re

fasta = pysam.Fastafile("../input/ref/ref_genome")

refs = fasta.references
