from pyfmp.api import balance_sheet as bs
from datetime import datetime

columns = {
    'date': [datetime, None],
    'symbol': [str, None],
    'fillingDate': [datetime, None],
    'acceptedDate': [datetime, None],
    'period': [str, None],
    'cashAndCashEquivalents': [float, 0],
    'shortTermInvestments': [float, 0],
    'cashAndShortTermInvestments': [float, 0],
    'netReceivables': [float, 0],
    'inventory': [float, 0],
    'otherCurrentAssets': [float, 0],
    'totalCurrentAssets': [float, 0],
    'propertyPlantEquipmentNet': [float, 0],
    'goodwill': [float, 0],
    'intangibleAssets': [float, 0],
    'goodwillAndIntangibleAssets': [float, 0],
    'longTermInvestments': [float, 0],
    'taxAssets': [float, 0],
    'otherNonCurrentAssets': [float, 0],
    'totalNonCurrentAssets': [float, 0],
    'otherAssets': [float, 0],
    'totalAssets': [float, 0],
    'accountPayables': [float, 0],
    'shortTermDebt': [float, 0],
    'taxPayables': [float, 0],
    'deferredRevenue': [float, 0],
    'otherCurrentLiabilities': [float, 0],
    'totalCurrentLiabilities': [float, 0],
    'longTermDebt': [float, 0],
    'deferredRevenueNonCurrent': [float, 0],
    'deferredTaxLiabilitiesNonCurrent': [float, 0],
    'otherNonCurrentLiabilities': [float, 0],
    'totalNonCurrentLiabilities': [float, 0],
    'otherLiabilities': [float, 0],
    'totalLiabilities': [float, 0],
    'commonStock': [float, 0],
    'retainedEarnings': [float, 0],
    'accumulatedOtherComprehensiveIncomeLoss': [float, 0],
    'othertotalStockholdersEquity': [float, 0],
    'totalStockholdersEquity': [float, 0],
    'totalLiabilitiesAndStockholdersEquity': [float, 0],
    'totalInvestments': [float, 0],
    'totalDebt': [float, 0],
    'netDebt': [float, 0],
    'link': [str, None],
    'finalLink': [str, None],
}

class balance_sheet:
    sheets = None
    index = None
    keys = None

    def __init__(self, ticker, client):
        self.sheets = []
        for row in bs(client, ticker):
            self.sheets.append(individual_balance_sheet(**row))

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.sheets):
            raise StopIteration

        return self.sheets[self.index]

class individual_balance_sheet:
    data = None
    index = None
    keys = None

    def __init__(self, **data):
        self.index = -1
        self.data = {}
        # print(data.get('period'))
        # exit(-1)
        for key in data:
            #print("'%s':" % key, "[float, 0],") #data.get(key))
            if key in columns:
                value = data[key]
                print(key)
                if columns[key][0] != datetime:
                    self.data[key] = columns[key][0](value)
                else:
                    self.data[key] = datetime.strptime(
                        value.split(" ")[0],
                        "%Y-%m-%d"
                    )
        
        self.keys = list(self.data.keys())

    def __iter__(self):
        self.index = -1
        return self

    def __getattr__(self, key):
        if key in columns:
            return self.data.get(key)

    def __next__(self):
        if self.index < len(self.keys) - 1:
            self.index += 1
            key = self.keys[self.index]
            return key, self.data[key]
        
        raise StopIteration

    def __str__(self):
        return "<balance sheet (%s)>" % (
            self.acceptedDate
        )