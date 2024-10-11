# AI Web Scraper

## Overview

The **AI Web Scraper** is a Streamlit application that allows users to scrape and extract specific information from any website using AI-based parsing. By entering a URL, users can retrieve the DOM content of the website, clean it, and then specify the data they want to extract. The app leverages the power of AI to parse the content based on user-defined descriptions.

## Features

- **URL Input**: Enter any website URL to start scraping.
- **DOM Content Viewer**: View the raw and cleaned DOM content from the scraped website.
- **AI-Based Parsing**: Specify the information you want to extract using natural language, and let the AI handle the parsing.
- **User-Friendly Interface**: Built with Streamlit, providing an interactive and straightforward user experience.

## Requirements

To run this application, ensure you have the following installed or downloaded:

- Python 3.7 or higher
- [Ollama server](https://ollama.com/download)
- [ChromeDriver for Selenium](https://googlechromelabs.github.io/chrome-for-testing/#stable)
- Necessary Python packages. Installation using using pip:

```bash
pip install -r requirements
```



## Setup
### Clone the repository:
```bash
git clone {Link to this repo};
cd AI-Web-Scrapper;
```
### Unzip the ChromeDriver:
```bash 
cd drivers;
unzip chromedriver.zip; 
mv chromedriver\ \(Copy\) chromedriver;
```
Or [Download the ChromeDriver manually:](https://googlechromelabs.github.io/chrome-for-testing/#stable)
```bash 
cd drivers;
wget {specific url}
```
![image](https://github.com/user-attachments/assets/c62099d0-88aa-4313-8cee-575a2ff6d0d2)

### (Optional) Create the environment variables file:
By default, the app uses the "llama3.2:1b" model without needing a .env file. However, the .env file allows you to quickly configure different versions of Ollama.
```
cp .env.example .env
```
### Ollama installation (Ubuntu)
1. Navegate to ollama download website ([llama3.2:1b is working](https://github.com/ollama/ollama))
```
curl -fsSL https://ollama.com/install.sh | sh
ollama run {desired ollama version}
```


### How to Use This README

1. Replace `https://github.com/yourusername/ai-web-scraper.git` with the actual URL of your repository.
2. Update the `your-email@example.com` and `yourusername` placeholders with your actual contact information.
3. Add any additional details specific to your app or any other features you might have included.

This README provides a comprehensive overview of the application, making it easy for users to understand how to set it up and use it.
