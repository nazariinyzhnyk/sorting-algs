import time
import argparse

from utils import sort_algs
import sorters

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--lst', nargs='+', type=int)
    args = parser.parse_args()
    print(f'List to sort = {args.lst}')

    for sort_alg in sort_algs:
        t1 = time.time()
        res = sort_alg(args.lst)
        print(f"\n{sort_alg.__name__}({args.lst}) = {res}. Time: {round(time.time() - t1, 2)}s.")
