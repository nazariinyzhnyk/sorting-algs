from sorters import insertion_sort


def bucket_sort(lst, n_buckets=10):
    bcks = []
    for _ in range(n_buckets):
        bcks.append([])

    for el in lst:
        bcks[int(el * n_buckets)].append(el)

    for bck in bcks:
        bck = insertion_sort(bck)

    res = []
    for bck in bcks:
        if bck:
            res += bck

    return res


if __name__ == '__main__':
    from utils import check_if_sorted
    srt = bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434])
    print(srt)
    print(check_if_sorted(srt))
