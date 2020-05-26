#!/usr/bin/python3.6

from KmerGenerator import KmerGenerator, BaseSet


# Instance KmerGenerator
kgenerator = KmerGenerator()


# Print convention code
kgenerator.base_set_descriptions()


# Given a test sequence
sequence = 'AUCAUCAUGGGAUAUAUUGGCCCCCUAARCUUAUAUCUCUGGSAAUGACUCUAUAUU'


# and the size k
k = 3


# Get the kmers dict
kmers = kgenerator.count_kmer(sequence, k, BaseSet.Dubious2)


# print result
print(kmers)
