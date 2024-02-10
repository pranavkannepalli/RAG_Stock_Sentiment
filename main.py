from news_queries import query_class
import openai

stock_symbol = input("Pick a valid stock symbol to see relevant info: ")
query = query_class.query_class(stock_symbol)
price, articles = query.getData()
print(price)
print(articles)

openai.api_key = "{redacted}"

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role":"system", "content":"You are a helpful assistant that returns a double from -1 to 1 representing the sentiment towards a stock when given news headlines."},
        {"role":"user", "content":f"What is the current stock price of {stock_symbol}"},
        {"role":"assistant", "content":f"Here are the details: {price}"},
        {"role":"user", "content":f"Here are the news headlines: {articles}"},
    ]
)

print(response)

