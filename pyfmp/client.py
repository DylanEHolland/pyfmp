import os
import pyfmp.company as company
from pyfmp.api import stock_list

class fmp_client:
    key = None

    def __init__(self, **kwargs):
        key = kwargs.get('key')
        if key:
            self.key = key
        else:
            if 'FINANCIAL_MODELING_PREP_KEY' in os.environ:
                self.key = os.environ.get('FINANCIAL_MODELING_PREP_KEY')
            else:
                raise RuntimeError("Requires FINANCIAL_MODELING_PREP_KEY")
    
    def company(self, ticker):
        return company.company(ticker, self)

    def all_tickers(self):
        return stock_list(self)