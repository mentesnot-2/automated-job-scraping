from celery import Celery
from job_scraper import scrape_jobs
from database import Database
from email_notifier import send_email

app = Celery('job_scraper', broker='redis://localhost:6379/0')

@app.task
def scrape_and_notify():
    db = Database()
    jobs = scrape_jobs()
    for job in jobs:
        if not db.job_exists(job['link']):
            db.insert_job(job)
            send_email(job)
    db.close()
