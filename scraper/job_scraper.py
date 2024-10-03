from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from database import Database
from email_notifier import send_email
from config import JobBoardURL, SEARCH_QUERY, LOCATION

def scrape_jobs():
    driver = webdriver.Chrome()
    driver.get(JobBoardURL)

    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(SEARCH_QUERY)
    location_box = driver.find_element(By.NAME, 'l')
    location_box.send_keys(LOCATION)
    search_box.submit()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_listings = soup.find_all('div', class_='job-listing')

    jobs = []
    for job in job_listings:
        title = job.find('h2', class_='title').text
        company = job.find('div', class_='company').text
        link = job.find('a')['href']
        jobs.append({'title': title, 'company': company, 'link': link})

    driver.quit()
    return jobs
