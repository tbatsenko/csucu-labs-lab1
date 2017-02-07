"""
read_field (str) -> (data) що зчитує з файлу ​filename​ поле та записує його у довільний зручний формат data​.
Ігрове поле у файлі представлене 10 стрічками, що містять символи ​*​ ​— частина корабля, яка ще не потонула,
 ​X​ ​—​ частина корабля, яка уже потонула та ​символ пробіл​ — частина поля, що не містить корабля.
  Наприклад, field.txt
"""
import doctest


def read_field(str):
    """
    (filename) -> (list)
    Docs
    """
    with open(str, 'r', encoding='utf-8', errors='ignore') as field_str:
        content = [list(line.strip('\n')) for line in field_str.readlines()]
    print(content)
    return content

def convert_ltr_coord(coord):
    """
    docs
    """
    letters = "ABCDEFGHIJ"
    return letters.index(coord)
    
    
def has_ship(data, coords_tuple):
    """
    (data, tuple) -> (bool)
    Docs
    """
    return False if data[convert_ltr_coord(coords_tuple[0])][coords_tuple[1]-1] == " " else True


def ship_size(data, coords_tuple):
    """-
    (data, tuple) -> (tuple)
    яка на основі зчитаних даних та координат клітинки
    (наприклад, (J, 1) або (A, 10)) визначає розмір корабля, частина якого знаходиться у даній клітинці
    >>> ship_size(read_field("field.txt"), ("G", 1))
    4
    """
    i_0 = convert_ltr_coord(coords_tuple[0])
    j_0 = coords_tuple[1]-1
    lst = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    counter = 1
    for i, j in lst:
        ic = i
        jc = j
        try:
            while data[i_0+i][j_0+j] != " ":
                i += ic
                j += jc
                counter += 1
        except:
            pass
    return counter

print(ship_size(read_field("field.txt"), ("G", 1)))


def is_valid(data):
    """
    is_valid (data) -> (bool) яка перевіряє чи поле зчитане з файлу може бути ігровим полем,
    на якому розмішені усі кораблі
    check 10x10 +
    check ships:
    - amount
    - situation
    
    >>> is_valid([[1], [1,2], [23], [34]])
    False
    """
    def check_ship_position(matrix):
        lst = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != " ":
                    for i1, j1 in lst:
                        try:
                            if matrix[i + i1][j + j1] == "*":
                                return False
                        except:
                            pass
        return True

    def check_ships_amount(matrix):
        """
        Docs
        
        """
        needed_ships = {1: 4, 2: 3, 3: 2, 4: 1}
        ships = {1: 0, 2: 0, 3: 0, 4: 0}
        letters = "ABCDEFGHIJ"
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != " ":
                    curr_ship = ship_size(matrix, (letters[i], j+1))
                    print("SHIP", curr_ship)
                    if curr_ship == 1:
                        ships[1] += 1
                    elif curr_ship == 2:
                        ships[2] += 1
                    elif curr_ship == 3:
                        ships[3] += 1
                    elif curr_ship == 4:
                        ships[4] += 1
                        print(ships)   
                    else:
                        print(curr_ship)
                        return False
        for i in ships.keys():
            ships[i] /= i
        return True if ships == needed_ships else False

    if sum(len(item) for item in data) != 100:
        return False
    if not check_ship_position(data):
        return False
    if not check_ships_amount(data):
        return False
    return True

"""
На основі зчитаних даних реалізуйте функції:


 

 is_valid (data) -> (bool) яка перевіряє чи поле зчитане з файлу може бути ігровим полем, на якому розмішені усі кораблі

Додатково реалізуйте функції:

● field_to_str (data) -> (str) яка дозволить з обраний вами формат перетворити у стрічку,
 що можна буде записати у файл або вивести на екран.

 ● generate_field () -> (data) яка дозволить згенерувати випадкове поле у вибраному форматі,
  на якому розміщенні класичні кораблі. Зауважте, що не є правильною стратегія заповнювати ігрове поле кораблями
   у довільному порядку, оскільки за такого підходу може не залишитися місця для розміщення корабля розміром 1 ✕ 4.
"""

# doctest.testmod()