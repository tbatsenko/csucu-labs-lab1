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


def is_valid(data):
    """
    is_valid (data) -> (bool) яка перевіряє чи поле зчитане з файлу може бути ігровим полем,
    на якому розмішені усі кораблі
    check 10x10 +
    check ships:
    - amount
    - ships position
    - ships amount

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
                    if curr_ship == 1:
                        ships[1] += 1
                    elif curr_ship == 2:
                        ships[2] += 1
                    elif curr_ship == 3:
                        ships[3] += 1
                    elif curr_ship == 4:
                        ships[4] += 1
                    else:
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

def field_to_str(data):
    """
    (data) -> (str)
    з обраний вами формат перетворити у стрічку,
    що можна буде записати у файл або вивести на екран.
    """
    line = "        -----------------------------------------------------------\n"
    nums_str = "          1     2     3     4     5     6     7     8     9     10     \n"
    field_str = ""+nums_str+line
    letters = "ABCDEFGHIJ"
    for i in range(len(data)):
        field_str += "    "+letters[i]+"  |"
        for j in range(len(data[i])):
            field_str += "  "+data[i][j]+"  |"
        field_str += "\n"
        field_str += line
    return field_str


def generate_field():
    """
    (None)-> (data)
    This function randomly generates a field with the ships for Battleship game.
    """
    import random
    def gen_angle():
        """
        
        :return: 
        """
        if random.choice((0,1)) == 0:
            return "h"  # horizontal
        return "v"  # vertical
    def situate_ship(ship_size, free_cells, field):
        """
        
        :param ship_size: 
        :param free_cells: 
        :return: 
        """
        angle = gen_angle()
        if angle == "v":
            free_cells = list(filter(lambda item: item[0] < 11-ship_size, free_cells))
        else:
            free_cells = list(filter(lambda item: item[1] < 11-ship_size, free_cells))
        random_coord = random.choice(free_cells)
        if angle == "v":
            for c1 in [-1,0,1]:
                for c2 in range(-1,ship_size+1):
                    try:
                        free_cells.remove((random_coord[0]+c2, random_coord[1]+c1))
                    except:
                        pass
            for i in range(ship_size):
                field[random_coord[0]+i][random_coord[1]] = "*"
        if angle == "h":
            for c1 in [-1, 0, 1]:
                for c2 in range(-1, ship_size + 1):
                    try:
                        free_cells.remove((random_coord[0] + c1, random_coord[1] + c2))
                    except:
                        pass
            for i in range(ship_size):
                field[random_coord[0]][random_coord[1]+i] = "*"
        return free_cells, field
    while True:
        availible_cells = [(i, j) for j in range(10) for i in range(10)]
        field = [[" " for c in range(10)] for r in range(10)]
        for num in range(1, 5):
            
            if num == 1:
                try:
                    after_ship = situate_ship(1, availible_cells, field)
                    availible_cells, field = after_ship[0], after_ship[1]
                except: 
                    field = []
            
            for times in range(5-num):
                try:
                    after_ship = situate_ship(num, availible_cells, field)
                except: 
                    field = []
                    availible_cells, field = after_ship[0], after_ship[1]
                
        if is_valid(field):
            return field
print(field_to_str(generate_field()))


"""
 ● generate_field () -> (data) яка дозволить згенерувати випадкове поле у вибраному форматі,
  на якому розміщенні класичні кораблі. Зауважте, що не є правильною стратегія заповнювати ігрове поле кораблями
   у довільному порядку, оскільки за такого підходу може не залишитися місця для розміщення корабля розміром 1 ✕ 4.
"""

# doctest.testmod()