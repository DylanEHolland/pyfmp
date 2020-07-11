from requests.api import get
from .profile import company_profile, float_columns
from .income_statement import income_statement

class company:
    ticker = None
    client = None

    def __init__(self, ticker, client):
        self.ticker = ticker
        self.client = client

    def balance_sheet(self):
        pass

    def cash_flow(self):
        pass

    def income_statement(self):
        return income_statement(self.ticker, self.client)

    def profile(self):
        return company_profile(self.ticker, self.client)