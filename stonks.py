import discord
from alpha_vantage.timeseries import TimeSeries
import requests
import json
import os
from datetime import date
from datetime import timedelta 

ts = TimeSeries(os.getenv('KEY'))
today = date.today() - timedelta(days = 1)

class Stonks: 
  def __init__(self, message, letters, date):
    self.company, self.meta = ts.get_daily(symbol = letters)
    self.symbol = letters
    self.message = message
    self.date = date 
    self.open = self.company[date]['1. open']
    self.high = self.company[date]['2. high']
    self.low = self.comapny[date]['3. low']
    self.close = self.company[date]['4. close']

  def get_companyInformation(self):
    url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol="+ self.symbol + "&apikey=" + os.getenv('KEY')
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['Name']
