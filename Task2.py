"""""
Задание 1. Задачи на одномерные списки
Вариант 2
Введите одномерный целочисленный список. Найдите наибольший нечетный элемент. 
Найдите минимальный по модулю элемент списка.
"""""

array = []
n = int(input("Введите количество чисел в списке: "))
for i in range(n):
    array.append(int(input("Введите целое число из списка: ")))
print(array)

# array = [777777772, 864, -547, 42, 154, -542, 724, 543, 37542, -4752, 4321]
max_element = None
for x in array:
    if x % 2 != 0:
        if max_element is None or x > max_element:
            max_element = x
print("наибольший нечетный элемент: ", max_element)

min_element = None
for x in array:
    if min_element is None or abs(x) < min_element:
        min_element = abs(x)
print("минимальный по модулю элемент списка: ", min_element)

""""
Задание 2. Задачи на многомерные списки 
1. В матрице найти номер строки, сумма чисел в которой максимальна. 
"""""

a = [[4, 0], [2, 0], [2, 0], [1, 0]]
print(a)
max_sum = None
row_sum = 0
row_index = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        row_sum += a[i][j]
    print(row_sum)
    if max_sum is None or row_sum > max_sum:
        max_sum = row_sum
        row_index = i
    row_sum = 0
print("номер строки, сумма чисел в которой максимальна: ", row_index + 1)

"""""
2.	Симметричная матрица. 
Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.
"""""
matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
is_symmetric = True
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break
    else:
        continue
    break
print(is_symmetric)
