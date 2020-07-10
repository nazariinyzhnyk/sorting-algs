import random
from typing import List

sort_algs = []


def check_if_sorted(lst: List) -> bool:
    """
    Function checks if provided list is sorted
    :param lst - list to be checked
    :return: bool - if the list is sorted
    >>> check_if_sorted([1, 2, 3, 4, 5])
    True
    >>> check_if_sorted([1, 2, 4, 3])
    False
    >>> check_if_sorted([1, 2, 2, 3])
    True
    """
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True


def get_list_for_test(quant: int = 1000, rand: bool = False, near: bool = False, rev: bool = False, srt: bool = True,
                      few: bool = False) -> List:
    """
    Function returns list of elements for testing algorithms
    :param quant: quantity of points to generate
    :param rand: simple random points
    :param near: points that are almost sorted
    :param rev: rev sorted list
    :param srt: already sorted list
    :param few: randomly shuffled finite set of points
    :return: list for test
    """
    if rand:
        lst = [random.randint(0, quant) for _ in range(quant)]
    elif near:
        rng = list(range(quant))
        lst = [rng[i] if random.random() > 0.1 else random.randint(0, quant) for i in rng]
    elif rev:
        lst = list(range(quant, -1, -1))
    elif few:
        lst = [random.randint(0, quant // 10) for _ in range(quant)]
    else:
        raise RuntimeError("Please choose one of following to be true: (rand, near, rev, few)")
    return lst


def register_sorter(sorter_func):
    sort_algs.append(sorter_func)
    return sorter_func


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    get_list_for_test(100, few=True)
    get_list_for_test(100, rand=True)
    get_list_for_test(100, rev=True)
    get_list_for_test(100, near=True)
