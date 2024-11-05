import random
from typing import Iterable


class BloomFilter:
    def __init__(self):
        self._L = 7  # number of hash-functions to use
        self._seeds = [[random.randint(0, 255) for _ in range(3)] for _ in range(self._L)]

        self._M = 10_000_000
        self._filter = [False for _ in range(self._M)]

    @staticmethod
    def _hash(word: Iterable[int]) -> int:
        """Compute the hash of a string."""
        p = 499
        m = 2 ** 61 - 1
        hash_value = 0
        p_power = 1
        for v in word:
            hash_value = (hash_value + v * p_power) % m
            p_power = (p_power * p) % m
        return hash_value

    def _get_indexes(self, s: str):
        """Get bloom filter indexes for a string."""
        indexes = []
        for seed in self._seeds:
            word = [ord(c) for c in s] + seed
            h = self._hash(word)
            index = h % self._M
            indexes.append(index)
        return indexes

    def add(self, s: str) -> None:
        assert len(s) <= 15, 'string too long'
        for i in self._get_indexes(s):
            self._filter[i] = True

    def has(self, s: str) -> bool:
        for i in self._get_indexes(s):
            if not self._filter[i]:
                return False
        return True


def main() -> None:
    bf = BloomFilter()
    while True:
        command = input().split()
        if len(command) == 0:
            continue
        elif len(command) == 1 and command[0] == '#':
            break
        elif len(command) == 2 and command[0] == 'add':
            bf.add(command[1])
        elif len(command) == 2 and command[0] == 'has':
            if bf.has(command[1]):
                print('Y')
            else:
                print('N')
        else:
            print(f'Invalid command "{" ".join(command)}"')


if __name__ == '__main__':
    main()
