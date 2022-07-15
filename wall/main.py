from collections import Counter


def stone_wall(array: str) -> int:

    clear_array = array.strip().replace(' ', '').split('\n')
    matrix = []
    for elem in clear_array:
        matrix.append([elem])

    indexes = []
    for row in matrix:
        for elem in row:
            for one_symbol in enumerate(elem):
                if one_symbol[1] == '0':
                    indexes.append(one_symbol[0])
    counter = Counter(indexes).most_common(1)

    return counter[0][0]


if __name__ == '__main__':
    print(stone_wall('''
    ###0###0####
    ###0#0#0#0##
    00#0#0#0##00
    ''') == 4)
