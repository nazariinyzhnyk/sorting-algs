from utils import register_sorter


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i+1


def quick(lst, low, high):
    if low <= high:
        pi = partition(lst, low, high)
        quick(lst, low, pi - 1)
        quick(lst, pi + 1, high)
    return lst


@register_sorter
def quick_sort(lst):
    return quick(lst, 0, len(lst)-1)


if __name__ == '__main__':
    from utils import check_if_sorted
    srt = quick_sort([7, 8, 5, 2, 2, 3, 1])
    print(srt)
    print(check_if_sorted(srt))
