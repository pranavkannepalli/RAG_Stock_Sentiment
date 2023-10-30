from GoogleNews import GoogleNews

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
    
# Input the stock symbol
stock_symbol = input("Enter the stock symbol: ")

# Call the scrape_yahoo_news function
stock_news = scrape_google_news(stock_symbol)
