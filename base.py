def less(a, b):
    return a < b


def exch(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def selection_sort():
    a = ["S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
    length = len(a)
    for index in range(length):
        min_num = index
        for index1 in range(index, length):
            if less(a[index1], a[min_num]):
                min_num = index1
        exch(a, index, min_num)
    print(a)

selection_sort()
