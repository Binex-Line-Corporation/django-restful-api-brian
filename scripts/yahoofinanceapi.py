# Title: yahoofinanceapi.py
# Author: Brian Choi
# Updated: 12/21/2021
# Version: 1.0.0
# Purpose: Script for interacting with the Yahoo Finance API and saving the results

import requests
import json
from datetime import datetime

def api_call():
    # Specification at yahoofinanceapi.com
    url = "https://yfapi.net/v8/finance/spark"
    
    querystring = {"interval":"1d",
                    "range":"3mo",
                    "symbols":"AAPL"}
    
    # Key linked to choi.brian.97@gmail.com
    headers = {
        'x-api-key': "pR0VAXpFRZ3KsLZZuZII24tP5o3xLUe94ZY3G61b"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text, file=open(".\\scripts\\results\\2021_12_21_APPL.txt", "w"))

def save_results():
    with open(".\\scripts\\results\\2021_12_21_APPL.txt") as f:
        old_json = json.loads(f.read())

    new_json = []

    # Convert unix time to YYYY-MM-DD
    old_json['AAPL']['timestamp'] = [datetime.utcfromtimestamp(time).strftime("%Y-%m-%d") 
                                        for time in old_json['AAPL']['timestamp']]
    
    # Fill list with each day's stock prices
    for (converted_time, price) in zip(old_json['AAPL']['timestamp'], old_json['AAPL']['close']):
        new_json.append(dict(ticker="AAPL",
                            company_name="Apple",
                            date=converted_time,
                            opening_price=price,
                            closing_price=price))

    print(json.dumps(new_json, indent=4), file=open(".\\scripts\\results\\2021_12_21_APPL_FORMATTED.txt","w"))

def main():
    api_call()
    save_results()

if __name__ == "__main__":
    main()