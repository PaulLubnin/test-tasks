def stone_wall(array: str) -> int:

    matrix = [elem for elem in zip(*array.split())]
    if matrix:
        return max(range(len(matrix)), key=lambda i: matrix[i].count('0'))
    return 0


if __name__ == '__main__':
    print(stone_wall('''
    ##########
    ####0##0##
    00##0###00
    ''') == 4)
    print(stone_wall('''

    ''') == 0)
