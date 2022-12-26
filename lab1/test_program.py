import sys

ARG_NUM_ERROR_MESSAGE = 'invalid argument count'
USAGE_MESSAGE = 'test_program.exe [program_to_test.exe] [test_cases.txt] [output.txt]'
ERROR_EXIT_CODE = 1
FILE_READ_ERROR_MESSAGE = 'Could not open/read file:'
WHITESPACE_CHARS = ' \n'
TEST_DATA_RESULT_DELIMETER = '->'

def get_tests(test_file):
    tests = []

    try:
        f = open(test_file, 'r', encoding='utf-8')
    except OSError:
        print(FILE_READ_ERROR_MESSAGE, test_file)
        sys.exit(ERROR_EXIT_CODE)

    for line in f.readlines():
        line = line.strip(WHITESPACE_CHARS)
        if len(line) == 0:
            continue

        args, excpected_result = line.split(TEST_DATA_RESULT_DELIMETER)
        tests.append([args.strip(WHITESPACE_CHARS), excpected_result.strip(WHITESPACE_CHARS)])

    f.close()
    return tests

def main(args):
    if len(args) != 3:
        print (ARG_NUM_ERROR_MESSAGE)
        print (USAGE_MESSAGE)
        sys.exit(ERROR_EXIT_CODE)

    program_to_test = args[0]
    test_file = args[1]
    output_file = args[2]

    tests = get_tests(test_file)

    print(tests)


if __name__ == '__main__':
    triangle_type = main(sys.argv[1:])