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

A = [[5, 10, 20], [110, 15, 20], [7, 3, 1]]
print(A)
max_sum = 0
sum_str = 0
col = 0
for i in range(len(A)):
    for j in range(len(A)):
        sum_str += A[i][j]
    print(sum_str)
    if sum_str > max_sum:
        max_sum = sum_str
        col = i
        sum_str = 0

print("номер строки, сумма чисел в которой максимальна: ", col + 1)

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