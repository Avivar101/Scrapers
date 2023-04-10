import concurrent.futures
from utils import threading_get_html, timeit
import sys

ARGS = int(sys.argv[1])


URL = "https://news.ycombinator.com/?p=1"
headers = {"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
           "Accept-Language": "en-gb",
           "Accept-Encoding": "br, gzip, deflate"}

@timeit
def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=ARGS) as executor:
        future = [executor.submit(threading_get_html, args, headers) for args in range(ARGS)]

if __name__=="__main__":
    main()