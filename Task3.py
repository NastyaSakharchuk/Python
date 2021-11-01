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
