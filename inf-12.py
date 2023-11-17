"""Создать квадратную матрицу размера MxM, где M является четным
числом из диапазона [2,8]. Конкретный размер матрицы задается пользователем.
Матрица содержит только целые числа из диапазона [1, 100], которые могут быть
как случайными, так и вводиться пользователем. Отсортировать элементы матрицы по убыванию и перераспределить их таким образом, чтобы в ее левой половине располагались только младшие элементы, а в правой – только старшие.
Результаты обработки матрицы вывести на экран."""
import numpy

print("Введите размер M квадратной матрицы MxM")
M = int(input("M="))
if M > 8 or M < 2 or M % 2 != 0:
    exit("Некорректный размер матрицы")
print("Вы хотите ввести значения элементов матрицы, иначе они заполнятся случайными числами?\nДа/Нет")
while True:
    answer = input("Ваш ответ: ")
    if answer == "Да" or answer == "Нет":
        random_input = answer == "Нет"
        break
    else:
        print("Некорректный ввод, попробуйте снова")
matrix = numpy.zeros((M, M), int)
if random_input:
    for i in range(M):
        for j in range(M):
            matrix[i][j] = int(numpy.random.random() * 99 + 1)
else:
    print(f"Введите матрицу размера {M}x{M}")
    for i in range(M):
        value = list(input().split())
        for j in range(M):
            if int(value[j]) == float(value[j]) and 1 <= int(value[j]) <= 100:
                matrix[i][j] = int(value[j])
            else:
                exit(f"Некорректное значение в {i + 1} строке {j + 1} столбце")
sort_matrix = numpy.zeros((M * M), int)
for i in range(M):
    for j in range(M):
        sort_matrix[i * M + j] = matrix[i][j]
sort_matrix.sort()
for i in range(M):
    for j in range(M // 2):
        matrix[i][j] = sort_matrix[i * M // 2 + j]
    for j in range(M // 2, M):
        matrix[i][j] = sort_matrix[M * M // 2 + i * M // 2 + j - M // 2]
print("Отсортированная матрица")
for i in range(M):
    for j in range(M):
        print(matrix[i][j],end=" ")
    print("")