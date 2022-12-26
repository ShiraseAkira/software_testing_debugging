import sys

ERROR_MESSAGE = 'неизвестная ошибка'
ERROR_EXIT_CODE = 1
OK_EXIT_CODE = 0

NOT_TRIANGLE_MESSAGE = 'не треугольник'
EQUILATERAL_TRIANLGE_MESSAGE = 'равносторонний'
ISOSCELES_TRIANGLE_MESSAGE = 'равнобедренный'
REGULAR_TRIANGLE_MESSAGE = 'обычный'

def get_triangle_sides(triangle_sides_lengths):
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

def is_all_sides_signinicant(triangle_sides):
    a, b, c = triangle_sides
    if a + b == b and a != 0 \
        or a + b == a and b != 0 \
        or a + c == a and c != 0:
            return False

    return True

def is_triangle(triangle_sides):
    a, b, c = triangle_sides
    if is_all_sides_signinicant(triangle_sides):
        return  a + b > c and \
                b + c > a and \
                c + a > b 
    else:
        return  a + b >= c and \
                b + c >= a and \
                c + a >= b 

def is_equilateral(triangle_sides):
    a, b, c = triangle_sides
    return a == b and a == c

def is_isosceles(triangle_sides):
    a, b, c = triangle_sides
    return  (a == b and a != c) or \
            (b == c and b != a) or \
            (c == a and c != b)


def get_triangle_type(triangle_sides_lengths):
    triangle_sides = get_triangle_sides(triangle_sides_lengths)

    if not is_triangle_sides_valid(triangle_sides):
        print(NOT_TRIANGLE_MESSAGE)
        sys.exit(OK_EXIT_CODE)

    if not is_triangle(triangle_sides):
        print(NOT_TRIANGLE_MESSAGE)
        sys.exit(OK_EXIT_CODE)

    if is_equilateral(triangle_sides):
        print(EQUILATERAL_TRIANLGE_MESSAGE)
    elif is_isosceles(triangle_sides):
        print(ISOSCELES_TRIANGLE_MESSAGE)
    else:
        print(REGULAR_TRIANGLE_MESSAGE)

if __name__ == '__main__':
    triangle_type = get_triangle_type(sys.argv[1:])