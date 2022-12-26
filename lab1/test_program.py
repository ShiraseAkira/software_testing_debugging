import sys
import subprocess

ARG_NUM_ERROR_MESSAGE = 'invalid argument count'
USAGE_MESSAGE = 'test_program.exe [program_to_test.exe] [test_cases.txt] [output.txt]'
ERROR_EXIT_CODE = 1
FILE_READ_ERROR_MESSAGE = 'Could not open/read file:'
FILE_WRITE_ERROR_MESSAGE = 'Could not write to file:'
WHITESPACE_CHARS = ' \n\r'
TEST_DATA_RESULT_DELIMETER = '->'

ENCODING = 'windows-1251'
TEST_SUCCESS_MESSAGE = 'SUCCESS'
TEST_FAIL_MESSAGE = 'ERROR'

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

def run_tests(program_to_test, tests, output_file):
    try:
        f = open(output_file, 'w', encoding='utf-8')
    except OSError:
        print(FILE_WRITE_ERROR_MESSAGE, output_file)
        sys.exit(ERROR_EXIT_CODE)

    for test in tests:
        args = test[0].split()
        expected_outcome = test[1]
        result = subprocess.run([program_to_test, *args], capture_output=True)
        result_message = result.stdout.decode(ENCODING).strip(WHITESPACE_CHARS)
        if result_message == expected_outcome:
            print(TEST_SUCCESS_MESSAGE, file=f)
        else :
            print(TEST_FAIL_MESSAGE, file=f)

    f.close()

def main(args):
    if len(args) != 3:
        print (ARG_NUM_ERROR_MESSAGE)
        print (USAGE_MESSAGE)
        sys.exit(ERROR_EXIT_CODE)

    program_to_test = args[0]
    test_file = args[1]
    output_file = args[2]

    tests = get_tests(test_file)

    run_tests(program_to_test, tests, output_file)


if __name__ == '__main__':
    triangle_type = main(sys.argv[1:])