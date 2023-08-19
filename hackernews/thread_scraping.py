import concurrent.futures
from utils import concurrent_get_html, timeit
import sys


ARGS = int(sys.argv[1])


URL = "https://news.ycombinator.com/?p=1"
headers = {"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
           "Accept-Language": "en-gb",
           "Accept-Encoding": "br, gzip, deflate"}
filename = "threading_hackernews.txt"

@timeit
def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=ARGS) as executor:
        {executor.submit(concurrent_get_html, args, headers, filename): args for args in range(ARGS)}


main()