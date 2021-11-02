'''
Задание 1. Задачи на одномерные списки
Вариант 2
Введите одномерный целочисленный список. Найдите наибольший нечетный элемент. 
Найдите минимальный по модулю элемент списка.
'''

array = []
n = int(input("Введите количество чисел в списке: "))
for i in range(n):
    array.append(int(input("Введите целое число из списка: ")))
print(array)

array1 = list(filter(lambda x: x % 2 == 1, array))
max_element = max(array1)
print(f"наибольший нечетный элемент {max_element}")

array2 = list(map(lambda x: abs(x), array))
min_abs = min(array2)
print(f"минимальный по модулю элемент {min_abs}")

'''
Задание 2. Задачи на многомерные списки 
1. В матрице найти номер строки, сумма чисел в которой максимальна. 
'''
matrix = [[4, 0], [20, 0], [2, 0], [1, 0]]


def find_max_row(matrix):
    max_sum = sum(matrix[0])
    max_index = 0
    for i, row in enumerate(matrix):
        row_sum = sum(row)
        if row_sum > max_sum:
            max_sum, max_index = row_sum, i
    return max_index


print("номер строки, сумма чисел в которой максимальна: ", find_max_row(matrix) + 1)

'''
2. Симметричная матрица. 
Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.
'''
matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]


def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


print('Симметрична ли матрица относительно главной диагонали: ', is_symmetric(matrix))
