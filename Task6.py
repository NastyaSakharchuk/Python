"""""
Вариант 9:
Скопировать из файла F1 в файл F2 все строки, начинающиеся на букву «А», 
расположенные между строками с номерами N1 и N2. 
Определить количество слов в первой строке файла F2.
"""""

N1 = int(input('Введите номер первой строки N1:\n'))
N2 = int(input('Введите номер последней строки N2:\n'))

with open('F1.txt', 'r') as fp:
    lines = fp.readlines()[N1 + 1:N2]

out_lines = []
for i, line in enumerate(lines):
    if line.startswith('а'):
        out_lines.append(line)

with open('F2.txt', 'w') as fp:
    for i in out_lines:
        fp.write(i)

print('Количество слов в первой строке файла F2:', len(out_lines[0].split()))
