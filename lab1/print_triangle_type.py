import sys

ERROR_MESSAGE = 'неизвестная ошибка'
ERROR_EXIT_CODE = 1
OK_EXIT_CODE = 0

NOT_TRIANGLE_MESSAGE = 'не треугольник'
EQUILATERAL_TRIANLGE_MESSAGE = 'равносторонний'

def get_triangle_sides(sides_lengths):
    if len(sides_lengths) != 3:
        print(ERROR_MESSAGE)
        sys.exit(ERROR_EXIT_CODE)
    try:
        sides = [float(sides_lengths[0]), float(sides_lengths[1]), float(sides_lengths[2])]
    except ValueError:
        print(ERROR_MESSAGE)
        sys.exit(ERROR_EXIT_CODE)
    return sides

def is_sides_valid(sides):
    for side in sides:
        if side <= 0:
            return False
    return True

def is_triangle(sides):
    return  sides[0] + sides[1] > sides[2] and \
            sides[1] + sides[2] > sides[0] and \
            sides[2] + sides[0] > sides[1] 

def is_equilateral(sides):
    return sides[0] == sides[1] and sides[0] == sides[2]


def get_triangle_type(sides_lengths):
    sides = get_triangle_sides(sides_lengths)

    if not is_sides_valid(sides):
        print(NOT_TRIANGLE_MESSAGE)
        sys.exit(OK_EXIT_CODE)

    if not is_triangle(sides):
        print(NOT_TRIANGLE_MESSAGE)
        sys.exit(OK_EXIT_CODE)

    if is_equilateral(sides):
        print(EQUILATERAL_TRIANLGE_MESSAGE)

    print('OK')

if __name__ == '__main__':
    triangle_type = get_triangle_type(sys.argv[1:])