"""
This file computes seive of eratosthenes lazily.
This provides a generator which can be iterated infinitely
to generate the list of prime numbers
"""

from itertools import count
from typing import Iterator, Union


def seive(gen: Union[Iterator[int], int] = count(2)) -> Iterator[int]:
    """
    Generates sieve lazily until the provided iterator ends else infinitely.

    Args:
        gen (Union[Iterator[int], int], optional): Iterator to find the prime numbers
            from or the int to start itertator from. Defaults to count(2).

    Yields:
        int: Next prime number in the given iterator
    """
    if isinstance(gen, int):
        gen: Iterator[int] = count(gen)
    n = next(gen)
    yield n
    yield from seive(i for i in gen if i % n != 0)


if __name__ == "__main__":
    from itertools import islice

    for p in islice(seive(), 15):
        print(p)
    # for i, p in zip(range(1, 16), seive()):
    #     print(i, p)
