from my_file_utils import save_to_file
from scraper import Scraper

keywords = []

while(True):
    keyword = input("What do you want to search for? (you don't want to, type 'exit') : ")
    if keyword == "exit":
        break
    keywords.append(keyword)

for keyword in keywords:
    scraper = Scraper(keyword)
    scraper.__enter__()
    jobs = scraper.keyword_jobs()
    save_to_file(keyword, jobs)