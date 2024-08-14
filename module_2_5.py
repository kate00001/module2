def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)


value = int(input('Введите отличное от нуля положительное число: '))
n = int(input('Введите число строк в матрице: '))
m = int(input('Введите число столбцов в матрице: '))
if int(value) <= 0 or int(m) <= 0 or int(n) <= 0:
    print('Вы ввели неподходящее число, попробуйте еще раз')
else:
    get_matrix(n, m, value)
