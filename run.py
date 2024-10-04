from scraper.celery_tasks import run_scraping_task

if __name__ == "__main__":
    # Manually trigger the scraping task
    run_scraping_task.delay()
