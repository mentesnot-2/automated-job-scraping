import sqlite3
from scraper.config import DB_PATH

def save_jobs_to_db(jobs):
    """
    Save scraped job data to an SQLite database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT
        )
    """)

    # Insert job entries
    for job in jobs:
        cursor.execute("""
            INSERT INTO jobs (title, company, location)
            VALUES (?, ?, ?)
        """, (job["title"], job["company"], job["location"]))

    conn.commit()
    conn.close()

def get_all_jobs():
    """
    Retrieve all jobs from the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    conn.close()
    return rows
