import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_website(url:str):

    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path),options=options)
    
    try:
        driver.get(url)
        html = driver.page_source
        time.sleep(5)
        return html
    except Exception as e:
        print(e)
    finally:
        driver.quit()

def scrape_website_with_proxy(url:str):
    SBR_WEBDRIVER = "https://brd-customer-hl_a3bb8c54-zone-ai_scraper:fue3jhh6xjyk@brd.superproxy.io:9515"
    
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver: print('Connected! Navigating...')
    
    try:
        driver.get(url)
        html = driver.page_source
        return html
    except Exception as e:
        print(e)
    finally:
        driver.quit()

def extract_body(html_content):
    soup = BeautifulSoup(html_content,"html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body(body_content):
    soup = soup = BeautifulSoup(body_content,"html.parser")
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
        )
    return cleaned_content


def  split_dom(dom_content,max_length=6000):
    return[
        dom_content[i : i + max_length] for i in range(0,len(dom_content),max_length)
    ]