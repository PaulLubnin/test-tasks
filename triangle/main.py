import math


def triangle(a: int, b: int, c: int) -> [int, int, int]:

    if a + b <= c or b + c <= a or c + a <= b:
        return [0, 0, 0]
    else:
        angle_a = round(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))), 0)
        angle_b = round(math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))), 0)
        angle_c = round(math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))), 0)
        return sorted([int(angle_a), int(angle_b), int(angle_c)])


if __name__ == '__main__':
    print(triangle(4, 4, 4) == [60, 60, 60])
    print(triangle(3, 4, 5) == [37, 53, 90])
    print(triangle(2, 2, 5) == [0, 0, 0])
    print(triangle(10, 20, 30) == [0, 0, 0])
