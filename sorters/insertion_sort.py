from utils import register_sorter


@register_sorter
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


if __name__ == '__main__':
    from utils import check_if_sorted
    srt = insertion_sort([7, 8, 5, 2, 2, 3, 1])
    print(srt)
    print(check_if_sorted(srt))
