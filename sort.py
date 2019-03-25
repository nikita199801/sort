def SelectionSort(lst):                       #сортировка выбором
    for i in range(0, len(lst)-1):
        min= i
        for j in range (i+1,len(lst)):
            if lst[j]< lst[min]:
                min=j
        lst[i], lst[min] = lst[min], lst[i]
    print("Сортировка выбором:", lst)


def heapsort(lst):                           #пирамидальная сортировка
    sl = len(lst)

    def swap(pi, ci):                       #функция меняте местами элементы в массиве
        if lst[pi] < lst[ci]:
            lst[pi], lst[ci] = lst[ci], lst[pi]

    def sift(pi, unsorted):                                     #метод отсеивания узлов
        i_gt = lambda a, b: a if lst[a] > lst[b] else b
        while pi * 2 + 2 < unsorted:
            gtci = i_gt(pi * 2 + 1, pi * 2 + 2)
            swap(pi, gtci)
            pi = gtci

    # Строим дерево
    for i in range(int(sl / 2) - 1, -1, -1):
        sift(i, sl)
    # сортируем его функциями sift и swap
    for i in range(sl - 1, 0, -1):
        swap(i, 0)
        sift(0, i)

    print("Пирамидальная сортировка: ", lst)