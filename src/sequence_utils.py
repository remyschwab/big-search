import pysam
import re

fasta = pysam.Fastafile("../input/ref/genome")

refs = fasta.references

genome_iter = []

