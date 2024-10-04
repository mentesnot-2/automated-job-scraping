# Configuration settings for the scraper project

# URLs to scrape
TARGET_URLS = [
    "https://www.indeed.com/jobs?q=python&l=United+States",
    # "https://another-job-site.com/search"
]

# Selenium WebDriver path (update this with the actual path to your WebDriver)
SELENIUM_DRIVER_PATH = "/path/to/chromedriver"

# Database configurations
DB_PATH = "scraper/jobs.db"

# Email settings (dummy values)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = " mentesnotsibatu63@gmail.com"
EMAIL_PASSWORD = "byha hjri wdfp stxy"

# Celery broker URL for task queue management
CELERY_BROKER_URL = "redis://localhost:6380/0"
CELERY_RESULT_BACKEND = "redis://localhost:6380/0"
