from utils import register_sorter


@register_sorter
def shell_sort(lst):
    n = len(lst)
    gap = int(n // 2)
    while gap != 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap = int(gap / 2)
    return lst


if __name__ == '__main__':
    from utils import check_if_sorted
    srt = shell_sort([7, 8, 5, 2, 2, 3, 1])
    print(srt)
    print(check_if_sorted(srt))
