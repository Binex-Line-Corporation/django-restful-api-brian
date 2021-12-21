# Title: api_post.py
# Author: Brian Choi
# Updated: 12/21/2021
# Version: 1.0.0
# Purpose: Script for a POST request with JSON data to Django REST API

import requests
import json

with open(".\\scripts\\results\\2021_12_20_APPL_FORMATTED.txt") as f:
    stocks = json.loads(f.read())

for stock in stocks:
    # Specification for this API is in the README.md
    response = requests.post("http://192.168.1.98:8000/api/v1/stocks/", data=stock)
    print(response.json(), file=open(".\\scripts\\results\\api_post_results.txt", "a"))