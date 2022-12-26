import sys

ERROR_MESSAGE = 'неизвестная ошибка'
ERROR_EXIT_CODE = 1
OK_EXIT_CODE = 0

NOT_TRIANGLE_MESSAGE = 'не треугольник'
EQUILATERAL_TRIANLGE_MESSAGE = 'равносторонний'

def get_triangle_triangle_sides(triangle_sides_lengths):
    if len(triangle_sides_lengths) != 3:
        print(ERROR_MESSAGE)
        sys.exit(ERROR_EXIT_CODE)
    try:
        triangle_sides = [float(triangle_sides_lengths[0]), float(triangle_sides_lengths[1]), float(triangle_sides_lengths[2])]
    except ValueError:
        print(ERROR_MESSAGE)
        sys.exit(ERROR_EXIT_CODE)
    return triangle_sides

def is_triangle_sides_valid(triangle_sides):
    for side in triangle_sides:
        if side <= 0:
            return False
    return True

def is_triangle(triangle_sides):
    return  triangle_sides[0] + triangle_sides[1] > triangle_sides[2] and \
            triangle_sides[1] + triangle_sides[2] > triangle_sides[0] and \
            triangle_sides[2] + triangle_sides[0] > triangle_sides[1] 

def is_equilateral(triangle_sides):
    return triangle_sides[0] == triangle_sides[1] and triangle_sides[0] == triangle_sides[2]


def get_triangle_type(triangle_sides_lengths):
    triangle_sides = get_triangle_triangle_sides(triangle_sides_lengths)

    if not is_triangle_sides_valid(triangle_sides):
        print(NOT_TRIANGLE_MESSAGE)
        sys.exit(OK_EXIT_CODE)

    if not is_triangle(triangle_sides):
        print(NOT_TRIANGLE_MESSAGE)
        sys.exit(OK_EXIT_CODE)

    if is_equilateral(triangle_sides):
        print(EQUILATERAL_TRIANLGE_MESSAGE)

    print('OK')

if __name__ == '__main__':
    triangle_type = get_triangle_type(sys.argv[1:])