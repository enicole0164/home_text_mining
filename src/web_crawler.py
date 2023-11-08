import requests
from retrying import retry
from requests.exceptions import ConnectionError, ReadTimeout, HTTPError

from bs4 import BeautifulSoup

# Retry decorator with exponential backoff strategy
@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=1)
def crawl_website(url):
    retries = 3
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        text_data = soup.get_text()
        return text_data, True
    except HTTPError as http_err:
        if http_err.response.status_code == 403:
                print("HTTPError 403: Forbidden - You don't have permission to access this resource.")
                # Handle 403 error, such as logging, waiting, or stopping the script
        else:
            print(f"HTTP error occurred: {http_err}")
            # Handle other HTTP errors as needed
        return [], False
    except (ConnectionError, ReadTimeout) as e:
        print(f"Connection error occurred: {e}")
        return [], False
