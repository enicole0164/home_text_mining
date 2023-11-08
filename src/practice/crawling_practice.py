import requests
from bs4 import BeautifulSoup

# Function to crawl a website and extract text data
def crawl_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract text content from the website (modify as per website structure)
    text_data = soup.get_text()
    return text_data

# Example usage
url = 'https://www.britannica.com/dictionary/eb/qa/what-s-the-difference-between-a-house-and-a-home'  # Replace this with the target website URL
website_text = crawl_website(url)
