import argparse
import requests
import queue

from urllib.parse import urlparse
from bs4 import BeautifulSoup
# from datetime import datetime

VALID_URLS_REPORT_FILE = 'valid.txt'
INVALID_URLS_REPORT_FILE = 'invalid.txt'

# DATETIME_FORMAT = '%d/%m/%Y, %H:%M'
# datetime.now().strftime(DATETIME_FORMAT)

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('url', help='url to test availability of links')
    parser.add_argument('-val', help='file for logging VALID urls', metavar='filename', default=VALID_URLS_REPORT_FILE)
    parser.add_argument('-inval', help='file for logging INVALID urls', metavar='filename', default=VALID_URLS_REPORT_FILE)

    return parser.parse_args()

def is_href_available(href):
    if href == None:
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
            if parsed_base_url.netloc in href:
                links.append(href)
            links.append(parsed_base_url._replace(path=href).geturl())

    return links

def log_link():
    pass

def crawl_from_url(args):
    valid_url_counter = 0
    invalid_url_counter = 0

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
            #TODO logging
            invalid_url_counter += 1
            pass
        #TODO logging
        valid_url_counter += 1

        links = get_available_links(r.text, args.url)
        for link in links:
            if link in visited_urls:
                continue
            urls_queue.put(link)

        print(visited_urls)

if __name__ == '__main__':
    args = get_args()
    crawl_from_url(args)
    