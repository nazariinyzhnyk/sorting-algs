from utils import register_sorter


@register_sorter
def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


if __name__ == '__main__':
    from utils import check_if_sorted
    srt = selection_sort([7, 8, 5, 2, 2, 3, 1])
    print(srt)
    print(check_if_sorted(srt))
