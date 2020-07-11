from requests.api import get
from pyfmp.company.profile import company_profile, float_columns
from pyfmp.company.income_statement import income_statement
from pyfmp.company.balance_sheet import balance_sheets

class company:
    ticker = None
    client = None

    def __init__(self, ticker, client):
        self.ticker = ticker
        self.client = client

    def balance_sheets(self):
        return balance_sheets(self.ticker, self.client)

    def cash_flow(self):
        pass

    def income_statements(self):
        return income_statement(self.ticker, self.client)

    def profile(self):
        return company_profile(self.ticker, self.client)