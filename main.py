from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

class Scraper:

    def __init__(self, keyword):
        self.keyword = keyword

    def __enter__(self, keyword):
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.wanted.co.kr/search?query={self.keyword}&tab=position")

        for x in range(5):
            time.sleep(5)
            page.keyboard.down("End")

        self.content = page.content()

        p.stop()

    def keyword_jobs(self):
        jobs_db = []
        soup = BeautifulSoup(self.content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")

        for job in jobs:
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            title = job.find("strong", class_="JobCard_title__ddkwM").text
            company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
            reward = job.find("span", class_="JobCard_reward__sdyHn").text
            job = {
                "title":title,
                "company_name":company_name,
                "reward":reward,
                "link":link,
            }
            jobs_db.append(job)

        file = open(f"{self.keyword}.csv", "w", encoding="utf-8", newline="")
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Reward", "Link"])

        for job in jobs_db:
            writer.writerow(job.values())

        file.close()

keywords = ["flutter", "nextjs", "kotlin"]

for keyword in keywords:
    jobs = Scraper(keyword)
    jobs.__enter__(keyword)
    jobs.keyword_jobs()