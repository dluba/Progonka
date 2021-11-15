import random
import numpy
import datetime


class Progonka:
    def get_random_matrix(n):
        A = numpy.zeros((n, n))
        for a in range(0, n):
            for b in range(a - 1, a + 2):
                if (b == -1):
                    A[a][0] = random.randrange(0, 1000)
                    continue
                if (b == n):
                    break
                A[a][b] = random.randrange(0, 1000)
        return A

    def get_a(mat, number):
        if number < len(mat) - 1:
            return mat[number + 1, number]
        else:
            return 0

    def get_b(mat, number):
        if number < len(mat):
            return mat[number, number]
        else:
            return 0

    def get_c(mat, number):
        if number < len(mat) - 1:
            return mat[number, number + 1]
        else:
            return 0

    def get_alpha(mat, number):
        if number >= 0:
            return -Progonka.get_c(mat, number) / Progonka.get_y(mat, number)
        else:
            return 0

    def get_beta(mat_a, mat_b, number):
        if number >= 0 and number < len(mat_a):
            return (mat_b[number] - Progonka.get_a(mat_a, number - 1) * Progonka.get_beta(mat_a, mat_b, number - 1)) / Progonka.get_y(mat_a, number)
        else:
            return 0

    def get_y(mat, number):
        return Progonka.get_b(mat, number) + Progonka.get_a(mat, number - 1) * Progonka.get_alpha(mat, number - 1)

    def get_x(mat_a, mat_b, numeber):
        if numeber < len(mat_a):
            return Progonka.get_alpha(mat_a, numeber) * Progonka.get_x(mat_a, mat_b, numeber + 1) + Progonka.get_beta(mat_a, mat_b, numeber)
        else:
            return 0

    def get_all_x(mat_a, mat_b):
        i = len(mat_a) - 1
        x_arr = []
        while i >= 0:
            x_arr.append(Progonka.get_x(mat_a, mat_b, i))
            i -= 1
        return numpy.array(x_arr[::-1])

size = int(input("Размер матрицы A:"))
A = Progonka.get_random_matrix(size)
B = numpy.array([random.randrange(0, 100) for i in range(size)])


x = Progonka.get_all_x(A, B)


print("Матрица A: ", A)
print("Матрица B: ", B)
print("Матрица коэффициентов X: ", x)
print()

print("A * X = ", numpy.dot(A, x))
print("Проверка:", B == numpy.around(numpy.dot(A, x), 0))
