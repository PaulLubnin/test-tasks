def number_of_squares(array: list) -> int:

    set_squares = {tuple([elem[1], elem[0]]) if elem[0] > elem[1] else tuple(elem) for elem in array}

    n = 1
    count_square = 0
    all_square = []
    filter_side_square = []

    # начинаем с перебора элементов в множестве
    for elem in set_squares:

        # поиск маленьких квадратов
        a = (elem[0], elem[1])
        b = (elem[0] + n, elem[1] + n)
        c = (elem[0], elem[0] + n)
        d = (elem[1], elem[1] + n)
        small_square = {a, b, c, d}
        if len(small_square) == 4:
            if len(set_squares & small_square) == 4:
                count_square += 1
                all_square.append(set_squares & small_square)

        # ищем стороны средних квадратов
        search_side = search_middle_side(elem, set_squares)
        if search_side:
            filter_side_square.append(search_side)

        # ищем большой квадрат
        search_big_square = search_big_side(elem, set_squares)
        if search_big_square:
            all_square.append(search_big_square)
            count_square += 1

    # собираем средние квадраты на основе найденных сторон
    for elem in filter_side_square:
        middle_square = create_middle_square(elem, filter_side_square, set_squares)
        if middle_square:
            all_square.append(middle_square)
            count_square += 1

    return count_square


def search_middle_side(side, set_squares):
    for elem in set_squares:
        if side[1] == elem[0] and (elem[1] - side[0] == 2):
            return side[0], elem[1]


def create_middle_square(side, filter_side_square, set_squares):
    for elem in filter_side_square:
        if side[0] + 8 == elem[0] and side[1] + 8 <= 16:
            all_edge = {(side[0], side[0] + 1), (side[0] + 1, side[1]),
                        (side[0], side[0] + 4), (side[0] + 4, side[0] + 8),
                        (side[0] + 8, (side[0] + 8) + 1), ((side[0] + 8) + 1, (side[0] + 8) + 2),
                        (side[1], side[1] + 4), (side[1] + 4, side[1] + 8)}
            if len(all_edge & set_squares) == 8:
                a = side
                b = (side[1], side[1] + 8)
                c = (side[0], side[0] + 8)
                d = (side[0] + 8, side[1] + 8)
                return {a, b, c, d}


def search_big_side(side, set_squares):
    for elem in set_squares:
        if side[1] == elem[0]:
            point = search_last_point(elem, set_squares)
            if point and (point[1] + 12 <= 16):
                a = (side[0], point[1])
                b = (side[0], side[0] + 12)
                c = (point[1], point[1] + 12)
                d = (side[0] + 12, point[1] + 12)
                return {a, b, c, d}


def search_last_point(point, set_squares):
    for elem in set_squares:
        if point[1] == elem[0]:
            return elem


if __name__ == '__main__':
    print(number_of_squares([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7], [7, 8], [6, 10], [7, 11],
                             [8, 12], [10, 11], [10, 14], [12, 16], [14, 15], [15, 16]]) == 3)
    print(number_of_squares([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8], [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                             [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2)
    print(number_of_squares([[16, 15], [16, 12], [15, 11], [11, 12], [11, 10], [10, 14], [9, 10], [14, 13], [13, 9],
                             [15, 14]]) == 3)
    print(number_of_squares([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8], [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                             [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16], [2, 6], [5, 6]]) == 3)
