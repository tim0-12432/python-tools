import pandas_datareader as pdr
import datetime
import cfgparser as config

def fetch(crypto):
    start_date = config.START_DATE
    end_date = datetime.datetime.now()
    return pdr.DataReader(f"{crypto}-{config.CURRENCY}", "yahoo", start_date, end_date)

def fetch_combined():
    start_date = config.START_DATE
    end_date = datetime.datetime.now()
    column_names = []

    first = True
    for crypto in config.CRYPTO:
        data = pdr.DataReader(f"{crypto}-{config.CURRENCY}", "yahoo", start_date, end_date)
        if first:
            combined = data[[config.METRIC]].copy()
            column_names.append(crypto)
            combined.columns = column_names
            first = False
        else:
            combined = combined.join(data[config.METRIC])
            column_names.append(crypto)
            combined.columns = column_names
    return combined

def fetch_worths():
    currency_values = []

    for crypto in config.CRYPTO:
        data = pdr.DataReader(f"{crypto}-{config.CURRENCY}", "yahoo")
        currency_values.append(data["Adj Close"].iloc[-1])

    return {"currency": config.CRYPTO, "value": currency_values}