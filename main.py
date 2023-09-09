from yahoo_data_fetcher import get_price


tickers = ["DIS", "KO", "PEP", "INTC", "F", "V"]

"""url= US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance"""


for t in tickers:
    get_price(ticker=t, verbose=True)