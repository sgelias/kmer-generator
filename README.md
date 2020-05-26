# kmer-generator
Get a kmer list given a single DNA or RNA sequence.

## Base sets
Kmers can be generated using the standart four nucleotide codes A, C, T (or U), and G, and also all anbiguous codes of IUPAC convention (https://www.bioinformatics.org/sms/iupac.html).

# Usage
Instance the class and store in a object.

```python

from KmerGenerator import KmerGenerator, BaseSet
kgenerator = KmerGenerator()

```

Print IUPAC convention code used in KmerGenerator.
```python

kgenerator.base_set_descriptions()

```

The output is:
```
A => Adenine
C => Cytosine
G => Guanine
T => Thymine
U => Uracil
R => A or G
Y => C or T
S => G or C
W => A or T
K => G or T
M => A or C
B => C or G or T
D => A or G or T
H => A or C or T
V => A or C or G
N => any
```

Note: To generate kmers with ambiguous IUPAC codes (R, Y, S, ...), create an instance of the class and set the ***base_set*** parameter.

Set objects containing example sequence, kmer length, and base_set Enum.
```python

sequence = 'AUCAUCAUGGGAUAUAUUGGCCCCCUAARCUUAUAUCUCUGGSAAUGACUCUAUAUU'
k = 3
base_set = BaseSet.Dubious2

```

Then, generate kmer.
```python

kmers = kgenerator.count_kmer(sequence, k, base_set)
print(kmers)

```

The output:
```

[{'AAU': 1}, {'AAR': 1}, {'ACU': 1}, {'AUA': 3}, {'AUC': 3}, {'AUG': 2}, {'AUU': 2}, {'ARC': 1}, {'CAU': 2}, {'CCC': 1}, {'CCU': 1}, {'CUA': 2}, {'CUC': 2}, {'CUG': 1}, {'CUU': 1}, {'GAC': 1}, {'GAU': 1}, {'GCC': 1}, {'GGA': 1}, {'GGC': 1}, {'GGG': 1}, {'GGS': 1}, {'GSA': 1}, {'UAA': 1}, {'UAU': 3}, {'UCA': 2}, {'UCU': 2}, {'UGA': 1}, {'UGG': 3}, {'UUA': 1}, {'UUG': 1}, {'RCU': 1}, {'SAA': 1}]

```

Notice that only kmers with a frequency higher than zero are returned.
