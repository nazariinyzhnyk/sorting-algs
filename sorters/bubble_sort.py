from utils import register_sorter


@register_sorter
def bubble_sort(lst):
    n = len(lst)
    for idx_end in range(n):
        for i in range(n - idx_end - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


if __name__ == '__main__':
    from utils import check_if_sorted
    srt = bubble_sort([7, 8, 5, 2, 2, 3, 1])
    print(srt)
    print(check_if_sorted(srt))
