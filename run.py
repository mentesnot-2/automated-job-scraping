from celery import Celery
from scraper.celery_tasks import scrape_and_notify

if __name__ == "__main__":
    scrape_and_notify.apply_async(countdown=60)  # Start immediately or use a schedule
