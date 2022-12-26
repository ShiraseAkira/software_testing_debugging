import sys

ERROR_MESSAGE = 'неизвестная ошибка'
ERROR_EXIT_CODE = 1

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

def get_triangle_type(sides_lengths):
    sides = get_triangle_sides(sides_lengths)

    print(sides)

if __name__ == '__main__':
    triangle_type = get_triangle_type(sys.argv[1:])