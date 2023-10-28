from google_news_query import scrape_google_news
from yahoo_news_query import scrape_yahoo_news
from cnbc_news_query import scrape_cnbc_news
from price_query import scrape_stock_data

def getData(stock_symbol):
    google = scrape_google_news(stock_symbol)
    print(google)

    yahoo = scrape_yahoo_news(stock_symbol)
    print(yahoo)

    cnbc = scrape_cnbc_news(stock_symbol)
    print(cnbc)

    news  = google + yahoo + cnbc

    price = scrape_stock_data(stock_symbol)
    print(price)

    return price, news

stock = input("Enter a stock symbol: ")
price, news = getData(stock)

print(price)
print(news)