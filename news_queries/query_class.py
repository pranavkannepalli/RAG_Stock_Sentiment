import requests
from bs4 import *
from GoogleNews import GoogleNews

class query_class:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
    
    def getData(self):
        google = self.scrape_google_news()
        yahoo = self.scrape_yahoo_news()
        cnbc = self.scrape_cnbc_news()
        news  = google + yahoo + cnbc

        price = self.scrape_stock_data()

        return price, news

    def scrape_cnbc_news(self):
        url = f"https://www.cnbc.com/quotes/{self.stock_symbol}?tab=news"

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
    
    def scrape_google_news(stock_symbol):
        # Create an instance of GoogleNews
        googlenews = GoogleNews()

        # Define your search query
        query = f"{stock_symbol} stock news"

        # Search for news articles
        googlenews.search(query)

        # Get top news hits
        top_news = googlenews.results()

        articles = []
        # Display the top news hits
        for article in top_news[:20]:
            print("Title:", article['title'])
            articles.append(article)
        
        return articles

    def scrape_yahoo_news(self):
        # Define the URL for the stock news on Yahoo Finance
        url = f"https://finance.yahoo.com/quote/{self.stock_symbol}?p={self.stock_symbol}"

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
    
    def scrape_stock_data(self):
        # Define the URL of the stock page on Yahoo Finance
        url = f"https://finance.yahoo.com/quote/{self.stock_symbol}"

        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the element containing the stock price
            price_element = soup.find("div", {"class": "D(ib) Mend(20px)"})
            if price_element:
                stock_price = price_element.text
            else:
                return "Stock price not found."

            # Find other relevant data on the page and extract as needed

            # Return the stock data
            return f"Stock Symbol: {self.stock_symbol}\nStock Price: {stock_price}"
        else:
            return "Failed to retrieve data. Please check the stock symbol and try again."