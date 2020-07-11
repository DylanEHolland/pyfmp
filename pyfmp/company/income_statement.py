from pyfmp.api import income_statement
from datetime import datetime

from ..api import income_statement as income_statement_request

columns = {
    'date': [datetime, None],
    'fillingDate': [datetime, None],
    'acceptedDate': [datetime, None],
    'period': [str, 0],
    'revenue': [float, 0],
    'costOfRevenue': [float, 0],
    'grossProfit': [float, 0],
    'grossProfitRatio': [float, 0],
    'researchAndDevelopmentExpenses': [float, 0],
    'generalAndAdministrativeExpenses': [float, 0],
    'sellingAndMarketingExpenses': [float, 0],
    'otherExpenses': [float, 0],
    'operatingExpenses': [float, 0],
    'costAndExpenses': [float, 0],
    'interestExpense': [float, 0],
    'depreciationAndAmortization': [float, 0],
    'ebitda': [float, 0],
    'ebitdaratio': [float, 0],
    'operatingIncome': [float, 0],
    'operatingIncomeRatio': [float, 0],
    'totalOtherIncomeExpensesNet': [float, 0],
    'incomeBeforeTax': [float, 0],
    'incomeBeforeTaxRatio': [float, 0],
    'incomeTaxExpense': [float, 0],
    'netIncome': [float, 0],
    'netIncomeRatio': [float, 0],
    'eps': [float, 0],
    'epsdiluted': [float, 0],
    'weightedAverageShsOut': [float, 0],
    'weightedAverageShsOutDil': [float, 0],
    'link': [str, 0],
    'finalLink': [str, 0],
}

class income_statement:
    symbol = None
    statements = None
    index = None

    def __init__(self, ticker, client):
        self.statements = []
        self.symbol = ticker

        for row in income_statement_request(client, ticker):
            self.statements.append(individual_income_statement(**row))

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.statements):
            raise StopIteration

        return self.statements[self.index]

    def __str__(self):
        return "<%s$ income statements>" % self.symbol

class individual_income_statement:
    data = None
    index = None
    keys = None

    def __init__(self, **data):
        self.index = -1
        self.data = {}
        for key in data:
            if key in columns:
                value = data[key]
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
        return "<income statement (%s)>" % (
            self.acceptedDate
        )