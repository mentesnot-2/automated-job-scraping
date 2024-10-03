import smtplib
from config import EMAIL_ADDRESS, EMAIL_PASSWORD

def send_email(job):
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = f"New Job Alert: {job['title']} at {job['company']}"
        body = f"Check out the job posting here: {job['link']}"
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL_ADDRESS, "user@example.com", message)
