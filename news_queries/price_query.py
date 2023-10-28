import requests
from bs4 import BeautifulSoup

# Function to scrape stock data
def scrape_stock_data(stock_symbol):
    # Define the URL of the stock page on Yahoo Finance
    url = f"https://finance.yahoo.com/quote/{stock_symbol}"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        print(response.text)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the element containing the stock price
        price_element = soup.find("div", {"class": "D(ib) Mend(20px)"})
        if price_element:
            stock_price = price_element.text
        else:
            return "Stock price not found."

        # Find other relevant data on the page and extract as needed

        # Return the stock data
        return f"Stock Symbol: {stock_symbol}\nStock Price: {stock_price}"
    else:
        return "Failed to retrieve data. Please check the stock symbol and try again."

# Input the stock symbol
stock_symbol = input("Enter the stock symbol: ")

# Call the scrape_stock_data function
stock_data = scrape_stock_data(stock_symbol)

# Display the stock data
print(stock_data)