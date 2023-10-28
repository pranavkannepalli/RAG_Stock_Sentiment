import requests
from bs4 import BeautifulSoup

# Function to scrape recent news for a stock
def scrape_yahoo_news(stock_symbol):
    # Define the URL for the stock news on Yahoo Finance
    url = f"https://finance.yahoo.com/quote/{stock_symbol}?p={stock_symbol}"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the elements containing news headlines and links
        news_elements = soup.find_all("h3", {"class": "Mb(5px)"})
        
        # Initialize a list to store news headlines and links
        news_list = []

        # Extract news headlines and links
        for idx, news in enumerate(news_elements):
            headline = news.text
            link = news.find("a")["href"]
            news_list.append(headline)
            print(f"{idx + 1}. {headline}")
            print(f"   Link: https://finance.yahoo.com{link}\n")

        # Return the list of news headlines and links
        return news_list

    else:
        return []

# Input the stock symbol
stock_symbol = input("Enter the stock symbol: ")

# Call the scrape_yahoo_news function
stock_news = scrape_yahoo_news(stock_symbol)    
