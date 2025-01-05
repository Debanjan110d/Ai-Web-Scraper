import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup


def scrape_website(website):
    # Set up the Chrome driver
    print("Launching Chrome Browser...")

    chrome_driver_path = "./chromedriver.exe"
    options= webdriver.ChromeOptions()
    driver=webdriver.Chrome(service=Service(chrome_driver_path),options=options)

    try:
        driver.get(website)
        print("Page Loded...")
        html = driver.page_source
        time.sleep(10)

        return html
    except Exception as e:
        print(e)
    finally:
        driver.close()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)  # Convert to string if needed, or return body_content
    else:
        return "No body content found"

def clean_body_content(body_content):
    # Add your cleaning logic here
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup (["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content

def split_dom_content(dom_content,max_length=6000):
    # Add your logic here to split the content into sections
    return [dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)]