from celery import Celery
from scraper.job_scraper import scrape_jobs
from scraper.database import save_jobs_to_db
from scraper.email_notifier import send_email
from scraper.config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND, EMAIL_ADDRESS

# Set up Celery
app = Celery("job_scraper", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@app.task
def run_scraping_task():
    """
    Celery task to run the job scraping process.
    """
    print("starting celery task ")
    jobs = scrape_jobs()
    save_jobs_to_db(jobs)
    send_email(
        subject="Job Scraping Completed",
        body=f"Scraping completed. Total jobs scraped: {len(jobs)}",
        recipient="sibhatmentesnot@gmail.com"
    )
