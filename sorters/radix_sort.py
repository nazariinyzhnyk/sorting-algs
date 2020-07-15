def counting_sort_exp(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(0, n):
        index = int(arr[i] / exp1)
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = int(arr[i] / exp1)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(lst):
    max1 = max(lst)
    exp = 1
    while max1 / exp > 0:
        counting_sort_exp(lst, exp)
        exp *= 10
    return lst


if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    res = radix_sort(arr)
    print(res)
