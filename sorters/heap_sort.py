from utils import register_sorter


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)


@register_sorter
def heap_sort(lst):
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]  # swap
        heapify(lst, i, 0)
    return lst


if __name__ == '__main__':
    from utils import check_if_sorted
    srt = heap_sort([7, 8, 5, 2, 2, 3, 1])
    print(srt)
    print(check_if_sorted(srt))
