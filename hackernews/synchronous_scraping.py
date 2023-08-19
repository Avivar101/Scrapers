from utils import get_html, timeit
import sys


args = int(sys.argv[1])


URL = "https://news.ycombinator.com/?p=1"
headers = {"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
           "Accept-Language": "en-gb",
           "Accept-Encoding": "br, gzip, deflate"}
filename = "sync_hackernews.txt"

@timeit
def main(num_of_pages):
    get_html(num_of_pages, headers=headers, filename=filename)



if __name__=="__main__":
    main(args)