from utils import sort_algs, check_if_sorted
import sorters

print('\nCurrently available sorting algs:', [sort_alg.__name__ for sort_alg in sort_algs])


def dummy_test():
    lst = [1, 2, 3, 5, 4]
    print('\nEntered dummy test to sort list: ', lst)

    for sort_alg in sort_algs:
        res = sort_alg(lst)
        print(f"\n{sort_alg.__name__}({lst}) = {res}")
        print('Sorting was successful: ', check_if_sorted(res))


if __name__ == '__main__':
    dummy_test()
