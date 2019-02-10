import random as rd
import string

matrix = [[' ', ' ', ' '], ['h', 'g', 'e'], ['r', 't', ' ']]


def fill_gaps(matrix):
    for row in range(len(matrix)):
        print(row)
        for kol in range(len(matrix[row])):
            if matrix[row][kol] == ' ':
                matrix[row][kol] = rd.choice(string.ascii_uppercase)
                print('to miejsce jest puste')
    return matrix


print(fill_gaps(matrix))
