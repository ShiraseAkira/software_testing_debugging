import argparse

VALID_URLS_REPORT_FILE = 'valid.txt'
INVALID_URLS_REPORT_FILE = 'invalid.txt'

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('url', help='url to test availability of links')
    parser.add_argument('-val', help='file for logging VALID urls', metavar='filename', default=VALID_URLS_REPORT_FILE)
    parser.add_argument('-inval', help='file for logging INVALID urls', metavar='filename', default=VALID_URLS_REPORT_FILE)

    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()