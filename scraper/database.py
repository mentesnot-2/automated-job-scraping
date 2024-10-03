import sqlite3

class Database:
    def __init__(self, db_name='jobs.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (title TEXT, company TEXT, link TEXT)''')

    def insert_job(self, job):
        self.cursor.execute('INSERT INTO jobs (title, company, link) VALUES (?, ?, ?)',
                            (job['title'], job['company'], job['link']))
        self.conn.commit()

    def job_exists(self, link):
        self.cursor.execute('SELECT * FROM jobs WHERE link = ?', (link,))
        return self.cursor.fetchone() is not None

    def close(self):
        self.conn.close()
