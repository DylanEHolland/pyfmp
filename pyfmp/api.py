import requests
import json

base_url = "https://financialmodelingprep.com/api/v3"

def endpoint(client, path, symbol):
    url = "%s/%s/%s?apikey=%s" % (
        base_url,
        path,
        symbol,
        client.key
    )

    response = requests.get(url)
    response = json.loads(response.text)
    if "Error Message" in response:
        raise RuntimeError(response.get("Error Message"))
    return response

def company_profile(client, company_ticker):
    url = "%s/profile/%s?apikey=%s" % (
        base_url,
        company_ticker,
        client.key
    )
    
    response = requests.get(url)
    response = json.loads(response.text)
    if "Error Message" in response:
        raise RuntimeError(response.get("Error Message"))

    return response

def income_statement(client, company_ticker, quarter = False):
    quarter_str = ""
    if quarter:
        quarter_str = "period=quarter%"
    url = "%s/income-statement/%s?%sapikey=%s" % (
        base_url,
        company_ticker,
        quarter_str,
        client.key
    )
    
    response = requests.get(url)
    response = json.loads(response.text)
    if "Error Message" in response:
        raise RuntimeError(response.get("Error Message"))

    return response

def balance_sheet(client, company_ticker):
    data = endpoint(client, "balance-sheet-statement", company_ticker)
    return data
