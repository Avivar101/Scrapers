import asyncio
from utils import async_get_html, timeit
import sys


args = int(sys.argv[1])
headers = {"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
           "Accept-Language": "en-gb",
           "Accept-Encoding": "br, gzip, deflate"}

@timeit
def main():
    asyncio.run(async_get_html(args, headers))

main()