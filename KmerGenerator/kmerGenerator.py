import argparse
import itertools
import re
from enum import Enum
from typing import Dict, List


class BaseSet(Enum):
    """
    Enum for Base set types.
    """

    Pure: str = 'pure'
    Dubious2: str = 'dubious2'
    Dubious3: str = 'dubious3'
    Full: str = 'full'


class KmerGenerator:

    __bases_pure = {
        "A": "Adenine",
        "C": "Cytosine",
        "G": "Guanine",
        "T": "Thymine",
        "U": "Uracil",
    }

    __bases_2dubious = {
        "R": "A or G",
        "Y": "C or T",
        "S": "G or C",
        "W": "A or T",
        "K": "G or T",
        "M": "A or C",
    }

    __bases_3dubious = {
        "B": "C or G or T",
        "D": "A or G or T",
        "H": "A or C or T",
        "V": "A or C or G",
    }

    __bases_any = {
        "N": "any",
    }

    def base_set_descriptions(self, verbose: bool = True) -> Dict[str, str]:
        """
        Get description of bases.
        """

        bases = {
            **self.__bases_pure,
            **self.__bases_2dubious,
            **self.__bases_3dubious,
            **self.__bases_any
        }

        if verbose:
            [
                print('{0} => {1}'.format(k, v))
                for k, v in bases.items()
            ]

        return bases

    def __base_set_selector(self, base_set: BaseSet) -> List[str]:
        """
        Select the set of nucleotide for count.
        """

        assert base_set in BaseSet

        if base_set == base_set.Pure:
            return self.__bases_pure.keys()

        elif base_set == base_set.Dubious2:
            return {
                **self.__bases_pure,
                **self.__bases_2dubious
            }.keys()

        elif base_set == base_set.Dubious3:
            return {
                **self.__bases_pure,
                **self.__bases_2dubious,
                **self.__bases_3dubious
            }.keys()

        elif base_set == base_set.Full:
            return {
                **self.__bases_pure,
                **self.__bases_2dubious,
                **self.__bases_3dubious,
                **self.__bases_any
            }.keys()

    def __make_kmers(self, base_set: BaseSet = BaseSet.Pure, k: int = 2) -> List[str]:
        """
        Make kmers of k length.
        """

        bases = self.__base_set_selector(base_set)

        return [
            ''.join(p) for p in itertools.product(bases, repeat=k)
        ]

    def __get_match_case(self, sequence, case):
        """
        Get the match case given the pattern (kmer) and the sequence.
        """

        return re.findall(case, sequence, re.I | re.M)

    def count_kmer(self, sequence: str, k: int = 2, base_set: BaseSet = BaseSet.Pure) -> List[Dict[str, int]]:
        """
        Map kmers into sequence.
        """

        kmer_set = {}

        match_objs = map(
            lambda case:
            self.__get_match_case(sequence, case),
            self.__make_kmers(base_set, k)
        )

        for m in match_objs:
            if m.__len__() > 0:
                kmer_set[m[0]] = m.__len__()

        return kmer_set


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Get a kmer list given a single DNA or RNA sequence.\n"
    )

    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    required.add_argument(
        '--sequence',
        help="A string containing the target DNA or RNA sequence.\n"
        "Ex.: --sequence 'AUCAUCAUGGGAUAUAUUGGCCCCCUAACUUAUAUCUCUGGAAUGACUCUAUAUU'.",
        required=True
    )

    optional.add_argument(
        '--k',
        help="An integer containing the kmer length.\n"
        "Ex.: --k 2.",
        required=False
    )

    optional.add_argument(
        '--base_set',
        help="An string containing the base set to be used. Choices are: "
        "pure, dubious2, dubious3, and full. Ex.: --base_set 'pure'.",
        required=False
    )

    args = parser.parse_args()
    kgenerator = KmerGenerator()
    kmer = kgenerator.count_kmer(args.sequence, int(args.k))
    print(kmer)
