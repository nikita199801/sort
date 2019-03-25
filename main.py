from  sort import *

a = []
while True:
    choose=int(input("1. Ввести массив\n"
          "2. Сортировка выбором\n"
          "3. Пирамидальная сортировка\n"
          "0. Выход\n"
          "Выберите пункт: "))
    if choose == 1:
        len=int(input("Введите длинну массива: "))
        for x in range(0, len):
            val = int(input("Введите значение: "))
            a.append(val)
        print("Неотсортированный массив: ", a)
    elif choose == 2:
        SelectionSort(a)
    elif choose == 3:
        heapsort(a)
    elif choose == 0:
        break


