from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
from scraper.config import SELENIUM_DRIVER_PATH, TARGET_URLS
import logging
import undetected_chromedriver as uc


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def scrape_jobs():
    """
    Main function to scrape jobs from specified URLs using Selenium and BeautifulSoup.
    """
    logger.info("Starting job scraping...")
    service = Service(ChromeDriverManager().install())
    print(f"ChromeDriver service: {service}")
    # driver = webdriver.Chrome(service=service)
    driver = uc.Chrome()



    all_jobs = []

    for url in TARGET_URLS:
        logger.info(f"Scraping URL: {url}")
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Example extraction logic (adjust based on the site's HTML structure)
        job_elements = soup.find_all("div", class_="job-card")
        for job in job_elements:
            title = job.find("h2", class_="job-title").text.strip()
            company = job.find("span", class_="company-name").text.strip()
            location = job.find("span", class_="job-location").text.strip()

            job_info = {
                "title": title,
                "company": company,
                "location": location
            }
            all_jobs.append(job_info)

    driver.close()  # Close the WebDriver
    # time.sleep(1)
    logger.info(f"Total jobs scraped: {len(all_jobs)}")
    return all_jobs
