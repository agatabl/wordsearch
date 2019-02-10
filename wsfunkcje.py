import random as rd
import string


def ipmort_from_txt(fname):
    with open(fname) as f:
        words = f.readlines()
        words = [x.strip() for x in words]
    return words


def find_start_point_x(matrix):
    rand_place_x = rd.randint(0, len(matrix) - 1)
    return rand_place_x


def find_start_point_y(matrix):
    rand_place_y = rd.randint(0, len(matrix[0]) - 1)
    return rand_place_y


def insert_letters_row(word, matrix):
    # print(word)
    start_point_x = find_start_point_x(matrix)
    start_point_y = find_start_point_y(matrix)
    #print(start_point_x, start_point_y)
    if matrix[start_point_x][start_point_y] == " ":
        counter_of_places = 0
        for f in range(start_point_y, len(matrix[0])):
            if matrix[start_point_x][f] == " ":
                counter_of_places += 1
            else:
                #print("Nie ma miejsce")
                break
        if counter_of_places >= (len(word)):
            counter_of_letters = 0
            for n in word:
                matrix[start_point_x][start_point_y + counter_of_letters] = n
                counter_of_letters += 1

        else:
            #print("Szukam nowego miejsca")
            insert_letters_row(word, matrix)
    else:
        #print("Szukam nowego miejsca")
        insert_letters_row(word, matrix)


def insert_letters_col(word, matrix):
    # print(word)
    start_point_x = find_start_point_x(matrix)
    start_point_y = find_start_point_y(matrix)
    #print(start_point_x, start_point_y)
    if matrix[start_point_x][start_point_y] == " ":
        counter_of_places = 0
        for f in range(start_point_x, len(matrix)):
            if matrix[f][start_point_y] == " ":
                counter_of_places += 1
            else:
                #print("Nie ma miejsce")
                break
        if counter_of_places >= (len(word)):
            counter_of_letters = 0
            for n in word:
                matrix[start_point_x + counter_of_letters][start_point_y] = n
                counter_of_letters += 1

        else:
            #print("Szukam nowego miejsca")
            insert_letters_col(word, matrix)
    else:
        #print("Szukam nowego miejsca")
        insert_letters_col(word, matrix)

# losuje czy wstawia słowo w pionie czy poziomie (0- pion, 1- pozniom)


def select_dir():
    dir = rd.randint(0, 1)
    return dir


def select_word(x, matrix):
    for word in x:
        if select_dir() == 0:
            insert_letters_col(word, matrix)
        else:
            insert_letters_row(word, matrix)


def fill_gaps(matrix):
    for row in range(len(matrix)):
        for kol in range(len(matrix[row])):
            if matrix[row][kol] == ' ':
                matrix[row][kol] = rd.choice(string.ascii_uppercase)


def printMatrix(matrix):
    fill_gaps(matrix)
    for m in matrix:
        print(m, "\n")
