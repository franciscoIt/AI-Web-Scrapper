import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Helper to initialize driver
def init_driver(proxy_url=None):
    """Initializes a Chrome WebDriver with optional proxy settings."""
    chrome_driver_path = "drivers/chromedriver"
    options = Options()

    if proxy_url:
        options.add_argument(f"--proxy-server={proxy_url}")

    return webdriver.Chrome(service=Service(chrome_driver_path), options=options)

def scrape_website(url: str):
    """Scrapes a website and returns its HTML content."""
    driver = init_driver()

    try:
        url = normalize_url(url)
        driver.get(url)

        # Use WebDriverWait instead of time.sleep for better performance
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        html = driver.page_source
        return html

    except Exception as e:
        print(f"Error scraping {url}: {e}")

    finally:
        driver.quit()

def scrape_website_with_proxy(url: str):
    """Scrapes a website using a proxy and returns its HTML content."""
    proxy_url = ""
    driver = init_driver(proxy_url)

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        html = driver.page_source
        return html

    except Exception as e:
        print(f"Error scraping {url} with proxy: {e}")
    finally:
        driver.quit()

def extract_body(html_content: str) -> str:
    """Extracts the body tag content from the HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_body(body_content: str) -> str:
    """Cleans the body content by removing script and style elements."""
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom(dom_content: str, max_length: int = 6000):
    """Splits DOM content into chunks with a maximum length."""
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]


def normalize_url(url: str) -> str:
    """
    Normalizes the given URL to ensure it starts with 'https://'.

    Args:
        url (str): The URL to normalize.

    Returns:
        str: The normalized URL with 'https://'.
    """
    url = url.strip()  # Remove any leading/trailing whitespace
    if not url.startswith(('http://', 'https://')):
        return f"https://{url}"
    return url.replace("http://", "https://")
