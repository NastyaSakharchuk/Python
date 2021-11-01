# задание 1 - вариант 1: Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.
m = int(input("Введите первое число: "))
n = int(input("Введите второе число: "))
p = int(input("Введите третье число: "))
x = 0
if m < 0:
    x += 1
if n < 0:
    x += 1
if p < 0:
    x += 1
print("Количество отрицательных чисел: ", x)

# задание 1 - вариант 4: По номеру месяца напечатать пору года.
month = int(input("Введите число месяца: "))
if month <= 2 or month == 12:
    print("winter")
elif month <= 5:
    print("spring")
elif month <= 8:
    print("summer")
else:
    print("autumn")
