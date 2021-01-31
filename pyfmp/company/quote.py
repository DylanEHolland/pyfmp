from pyfmp.api import quote as fetch_quote

{
    'symbol': 'IHORX', 
    'name': 'The Hartford International Opportunities Fund Class R3', 
    'price': 19.96, 
    'changesPercentage': -2.68, 
    'change': -0.549998, 
    'dayLow': None, 
    'dayHigh': None, 
    'yearHigh': 20.72, 
    'yearLow': 11.5, 
    'marketCap': None, 
    'priceAvg50': 20.047575, 
    'priceAvg200': 18.147373, 
    'volume': None, 
    'avgVolume': 0, 
    'exchange': 'MUTUAL_FUND', 
    'open': None, 
    'previousClose': 20.509998, 
    'eps': None, 
    'pe': None, 
    'earningsAnnouncement': None, 
    'sharesOutstanding': None, 
    'timestamp': 1611793133
}

columns = {
    'price': [float, 0],
    'open': [float, 0],
    'previousClose': [float, 0],
    'priceAvg50': [float, 0], 
    'priceAvg200': [float, 0],
    'pe': [float, 0],
    'volume': [float, 0]
}

class quote:
    data = None

    def __init__(self, company_ticker, client):
        data = fetch_quote(client, company_ticker) 
        if not data:
            raise AttributeError("Returned nothing !?")

        self.data = {}
        for key in data:
            if key in columns:
                #print(key, data[key], columns[key][0] == type(data[key]))
                self.data[key] = data[key]
    
    def __getattr__(self, key):
        if key in columns:
            return self.data.get(key)   