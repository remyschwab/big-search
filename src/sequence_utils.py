import pysam
from itertools import izip_longest, islice


def build_genome(fasta):
    refs = fasta.references
    genome_iter = []
    for ref in refs:
        genome_iter.append(fasta.fetch(reference=ref))
    print "Joining..."
    genome = "".join(genome_iter)
    return genome


def fasta_wrap(path):
    fasta = pysam.Fastafile(path)
    return fasta


def partition(p, parts=2):
    """ Divide p into non-overlapping partitions. If there are excess
    characters, distribute them round-robin starting with 1st. """
    base, mod = len(p) / parts, len(p) % parts
    idx = 0
    ps = []
    mod_adjust = 1
    for i in xrange(0, parts):
        if i >= mod:
            mod_adjust = 0
        new_idx = idx + base + mod_adjust
        ps.append((p[idx:new_idx], idx))
        idx = new_idx
    return ps


def to_int_keys_best(l):
    """
    l: iterable of keys
    returns: a list with integer keys
    """
    seen = set()
    ls = []
    for e in l:
        if not e in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]


def suffix_array_best(s):
    """
    suffix array of s
    O(n * log(n)^2)
    """
    n = len(s)
    k = 1
    line = to_int_keys_best(s)
    while max(line) < n - 1:
        line = to_int_keys_best(
            [a * (n + 1) + b + 1
             for (a, b) in
             izip_longest(line, islice(line, k, None), fillvalue=-1)])
        k <<= 1
    return line
