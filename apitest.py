import requests


r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
rparsed = r.json()
btcdic = None
for i in rparsed:
    if 'symbol' in i and i['symbol'] == 'BTC':
        btcdic = i
        break
if btcdic is None:
    raise Exception("BTC is not found in response")
priceusd = btcdic['price_usd']
print(priceusd)