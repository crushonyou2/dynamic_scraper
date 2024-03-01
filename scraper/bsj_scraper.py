import requests
from bs4 import BeautifulSoup

class Job:
    def __init__(self, company, title, url):
        self.company = company
        self.title = title
        self.url = url

class Scrape_Skills:

    def __init__(self, skills):
        self.skills = skills
        self.url = f"https://berlinstartupjobs.com/skill-areas/{self.skills}"
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

        jobs = soup.find(
            "ul", class_="jobs-list-items").find_all("li", class_="bjs-jlid")
        for job in jobs:
            title = job.find("h4", class_="bjs-jlid__h").text
            company = job.find("a", class_="bjs-jlid__b").text
            url = job.find("h4", class_="bjs-jlid__h").find("a").attrs['href']

            self.jobs.append(Job(company, title, url))

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