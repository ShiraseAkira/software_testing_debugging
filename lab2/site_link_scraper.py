import argparse
import requests
import queue
import sys

from urllib.parse import urlparse
from bs4 import BeautifulSoup
from datetime import datetime


VALID_URLS_REPORT_FILE = 'valid.txt'
INVALID_URLS_REPORT_FILE = 'invalid.txt'
FILE_WRITE_ERROR_MESSAGE = 'Could not write to file:'
ERROR_EXIT_CODE = 1
DATETIME_FORMAT = '%d/%m/%Y, %H:%M'


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('url', help='url to test availability of links')
    parser.add_argument('-val', help='file for logging VALID urls', metavar='filename', default=VALID_URLS_REPORT_FILE)
    parser.add_argument('-inval', help='file for logging INVALID urls', metavar='filename', default=INVALID_URLS_REPORT_FILE)

    return parser.parse_args()

def is_href_available(href):
    if href == None or href =='':
        return False
    
    if href[-1] == '#':
        return False

    for protocol in ['http', 'https', 'tel', 'mailto']:
        if protocol in href:
            return False

    return True


def get_available_links(response_text, base_url):
    links = []
    parsed_base_url = urlparse(base_url)._replace(fragment='')

    soup = BeautifulSoup(response_text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if is_href_available(href):
            links.append(parsed_base_url._replace(path=href).geturl())

        if href and (parsed_base_url.netloc in href):
            links.append(href)

    return links

def crawl_from_url(args):
    valid_url_counter = 0
    invalid_url_counter = 0
    
    try:
        fv = open(args.val, 'w', encoding='utf-8')
    except OSError:
        print(FILE_WRITE_ERROR_MESSAGE, args.val)
        sys.exit(ERROR_EXIT_CODE)

    try:
        fi = open(args.inval, 'w', encoding='utf-8')
    except OSError:
        print(FILE_WRITE_ERROR_MESSAGE, args.inval)
        sys.exit(ERROR_EXIT_CODE)

    urls_queue = queue.Queue()
    urls_queue.put(args.url)
    visited_urls = []

    while not urls_queue.empty():
        link = urls_queue.get()
        if link in visited_urls:
            continue
        
        visited_urls.append(link)

        r = requests.get(link)

        if not r.ok:
            print(link, r.status_code, file=fi)
            invalid_url_counter += 1
            continue
        print(link, r.status_code, file=fv)
        valid_url_counter += 1

        links = get_available_links(r.text, args.url)
        for link in links:
            if link in visited_urls:
                continue
            urls_queue.put(link)

    time_now = datetime.now().strftime(DATETIME_FORMAT)

    # print(visited_urls)
    print(file=fv)
    print(f'Links number {valid_url_counter}', file=fv)
    print(time_now, file=fv)
    fv.close()
    print(file=fi)
    print(f'Links number {invalid_url_counter}', file=fi)
    print(time_now, file=fi)
    fi.close()

if __name__ == '__main__':
    args = get_args()
    crawl_from_url(args)
    