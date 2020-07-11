import pyfmp
import pyfmp.company

def test_client_init():
    client = pyfmp.client()
    
    assert type(client.key) == str
    assert type(client.company("AAPL")) == pyfmp.company.company

def test_company_profile():
    firm = pyfmp.client().company("AAPL")
    profile = firm.profile()
    
    for key, value in profile:
        if key in pyfmp.company.float_columns:
            assert type(value) == float
        else:
            print("%s:" % key, value)

def test_company_income_statement():
    firm = pyfmp.client().company("AAPL")
    statements = firm.income_statement()

    for row in statements:
        for key, value in row:
            print("\t", key + ":", value)
        print("\n===\n")

def test_company_balance_sheet():
    firm = pyfmp.client().company("AAPL")
    for row in firm.balance_sheet():
        for key, value in row:
            print("\t", key + ":", value)
        print("\n\n")