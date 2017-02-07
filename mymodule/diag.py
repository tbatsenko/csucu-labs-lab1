matrix1 = [["*", " ", " ", " "], [" ", " ", "*"], [" ", " ", " "]]


#first part of matrix
def check_ships_position(matrix):
    for diag1 in range(len(matrix)):  # From right to left like this - /
        counter = 0
        for i in range(diag1+1):
            if matrix[i][diag1] != " ":
                if counter:
                    return False
                counter += 1
            else:
                counter = 0
            diag1 -= 1
    for diag2 in range(len(matrix)-1, 0, -1):  # From right to left like this - /
        counter = 0
        j = len(matrix)-1
        for c in range(1, len(matrix)-diag2+1):
            if matrix[j][diag2] != " ":
                if counter:
                    return False
                counter +=1
            else:
                counter = 0
            diag2 += 1 
            j -= 1
    for diag3 in range(len(matrix) - 1, -1, -1):  # From left to right  like this - \
        counter = 0
        for i in range(0, len(matrix) - diag3):
            if matrix[i][diag3] != " ":
                if counter:
                    return False
                counter += 1
            else:
                counter = 0
            diag3 += 1
    for j in range(len(matrix)-1, 0, -1):  # From right to left like this - /
        counter = 0
        for diag4 in range(0, len(matrix)-j):
            if matrix[j][diag4] != " ":
                if counter:
                    return False
                counter +=1
            else:
                counter = 0 
            j += 1
    return True
    

print(check_ships_position(matrix1))