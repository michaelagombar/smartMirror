from coinmarketcap import Market
coinmarketcap = Market()
x = coinmarketcap.ticker(convert='USD')[0]
y = coinmarketcap.ticker(convert='USD')[1]

print("Bitcoin: " + x['price_usd'] +'\n' + "ETH: " + y['price_usd'])