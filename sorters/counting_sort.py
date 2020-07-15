def counting_sort(lst, max_value=256, unsqueeze=True):
    vls = [0 for _ in range(max_value)]
    for l in lst:
        vls[l] += 1

    if unsqueeze:
        result = []
        for i in range(max_value):
            if vls[i] != 0:
                result += [i for _ in range(vls[i])]
        return result
    else:
        return vls


if __name__ == '__main__':
    arr = [1, 4, 6, 5, 8, 4, 6, 8, 5, 3, 5, 7, 7, 8, 4, 3]
    res = counting_sort(arr)
    print(res)
