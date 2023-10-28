import requests
from bs4 import BeautifulSoup

def scrape_cnbc_news(stock_symbol):
    url = f"https://www.cnbc.com/quotes/{stock_symbol}?tab=news"

    response = requests.get(url)

    print(url)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Find and process stock-related news headlines
        headlines = soup.find_all("a", class_="LatestNews-headline")

        titles = []
        for headline in headlines:
            title = headline.text.strip()
            print("CNBC Stock News Title:", title)
            titles.append(title)
        
        return titles

    else:
        print("Failed to retrieve CNBC stock news headlines.")
        return []

# Input the stock symbol
stock_symbol = input("Enter the stock symbol: ")

# Call the scrape_yahoo_news function
stock_news = scrape_cnbc_news(stock_symbol)

#print(stock_news)