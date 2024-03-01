import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Job:
    def __init__(self, company, title, url):
        self.company = company
        self.title = title
        self.url = url

class Scrape_wwr:

    def __init__(self, skills):
        self.skills = skills
        self.url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={self.skills}"
        self.jobs = []

    def scrape_page(self):
        print(f"Scraping... {self.url}\n\n")
        print("-----------------------------------\n")
        response = requests.get(
            self.url,
            headers={
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
            })

        soup = BeautifulSoup(response.content, "html.parser")

        jobs = soup.find("section", class_="jobs").find_all("li", class_="feature")
        for job in jobs:
            title = job.find("span", class_="title").text
            company = job.find("span", class_="company").text
            relative_url = job.find("a").attrs['href']
            absolute_url = urljoin(self.url, relative_url)

            self.jobs.append(Job(company, title, absolute_url))

    def keyword_jobs(self):
        jobs_db = []
        for job in self.jobs:
            job_info = {
                "title": job.title,
                "company_name": job.company,
                "link": job.url,
            }
            jobs_db.append(job_info)
        return jobs_db

    def print_jobs(self):
        for job in self.jobs:
            job.print_job()