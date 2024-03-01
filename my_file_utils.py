import csv
import os

def save_to_file(file_name, jobs_db):
    if not os.path.exists('danimic_scraper/csv'):
        os.makedirs('dynamic_scraper/csv', exist_ok=True)

    file = open(os.path.join('dynamic_scraper/csv', f"{file_name}.csv"), "w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Link"])

    for job in jobs_db:
        writer.writerow(job.values())

    file.close()
