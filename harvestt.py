from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import re

def harvest_emails(url):
    options = Options()
    options.headless = True
    service = Service('/usr/local/bin/geckodriver')

    try:
        driver = webdriver.Firefox(service=service, options=options)
        driver.get(url)
        driver.implicitly_wait(10)
        
        page_source = driver.page_source
        driver.quit()

        emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', page_source))
        return emails
    except Exception as e:
        print(f"Error: {e}")
        return None

def print_harvested_emails(url):
    emails = harvest_emails(url)
    if emails:
        print(f"\nHarvested Emails from {url}:\n")
        if emails:
            for email in emails:
                print(f" - {email}")
        else:
            print("No emails found.")
    else:
        print("Failed to retrieve emails.")



