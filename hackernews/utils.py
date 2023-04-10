import re
import requests
from bs4 import BeautifulSoup
import time
from functools import wraps

aggregate_count = 0

def timeit(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		result = func(*args, **kwargs)
		end = time.perf_counter()
		print(f'{func.__name__} took {end - start:.6f} seconds to run')
		return result
	return wrapper

def get_html(num_of_pages, headers):
    for i in range(num_of_pages):
        page = i + 1
        r = requests.get(f"https://news.ycombinator.com/?p={page}", headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        selector(soup)

async def async_get_html(num_of_pages:int, headers:dict):
     for i in range(num_of_pages):
          await request_page(i, headers)

async def request_page(i, headers):
     page = i + 1
     r = requests.get(f"https://news.ycombinator.com/?p={page}", headers=headers)
     soup = BeautifulSoup(r.content, "html.parser")
     await selector(soup)


def threading_get_html(page, headers):
    print("scrape")
    r = requests.get(f"https://news.ycombinator.com/?p={page+1}", headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    selector(soup)

async def selector(soup):
    global aggregate_count
    for item in soup.find_all('tr', class_='athing'):
        item_a = item.find('span', class_='titleline')

        item_link = item_a.find('a').get('href') if item_a else None
        item_text = item_a.get_text(strip=True) if item_a else None

        next_row = item.find_next_sibling('tr')
        item_score = next_row.find('span', class_='score').get_text(strip=True) if next_row.find('span', class_='score') else '0 points'

        # we use regex to find the correct element
        item_comments = next_row.find('a', string=re.compile('\d+(&nbsp;|\s)comment(s?)'))
        item_comments = item_comments.get_text(strip=True).replace('\xa0', ' ') if item_comments else '0 comments'

        aggregate_count = aggregate_count + 1

        text = f"""
        count: {aggregate_count},\n
        link: {item_link},\n
        title: {item_text},\n
        score: {item_score},\n
        comments: {item_comments}\n
        --------------------------------------------------"""
        
        write_to_txt(text)

def write_to_txt(text):
    with open("content/async_hackernews.txt", "+a", encoding="UTF-8") as file:
        file.write(text)