import re
import bs4
import requests
from bs4 import BeautifulSoup


def fetch_conversion_factor(source_currency, target_currency):
    # Define the URL of the website you want to scrape
    url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={source_currency}&To={target_currency}"

    try:
        # Send an HTTP GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the exchange rate from the HTML
            exchange_rate = soup.find('p', class_='result__BigRate-sc-1bsijpp-1 dPdXSB').get_text()
            return float(re.sub(r'[^0-9.]', '', exchange_rate))

        else:
            return f"Failed to fetch data. Status code: {response.status_code}"

    except Exception as e:
        return str(e)

# Usage example
# source_currency = "USD"
# target_currency = "EUR"
# exchange_rate = fetch_conversion_factor(source_currency, target_currency)
# print(f"1 {source_currency} equals {exchange_rate} {target_currency}")

