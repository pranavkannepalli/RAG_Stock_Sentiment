# RAG_Stock_Sentiment

Scrape stock news headlines and ask an LLM to score sentiment toward the ticker.

**What it is**
A small Python pipeline: given a stock symbol, it scrapes headlines from Google News, Yahoo Finance, and CNBC (via `requests` + BeautifulSoup and the `GoogleNews` package) and pulls a current price off Yahoo. The headlines and price are stuffed into a chat prompt and sent to OpenAI `gpt-3.5-turbo`, which is instructed to return a sentiment score from -1 to 1. It is retrieval-then-generate in spirit: live news as context for the model.

**Run it**
`python main.py`, then enter a ticker at the prompt. Needs `openai`, `requests`, `beautifulsoup4`, and `GoogleNews`. Set your own OpenAI API key in `main.py` (the committed one is a placeholder). `news_queries/` holds the individual scrapers plus a `query_class` that combines them.

Note: the scrapers target specific site markup and the finance pages change often, so selectors may need updating. This is exploratory, not a trading tool.
