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
  def __init__(self, message):
    split_msg = message.split(" ")
    self.symbol = split_msg[1]
    self.company, self.meta = ts.get_daily(symbol = self.symbol)
    self.name = self.get_companyInformation()
    self.date = today 
    self.open = self.company[today.strftime("%Y-%m-%d")]['1. open']
    self.high = self.company[today.strftime("%Y-%m-%d")]['2. high']
    self.low = self.company[today.strftime("%Y-%m-%d")]['3. low']
    self.close = self.company[today.strftime("%Y-%m-%d")]['4. close']
    self.color = self.set_color()

  def get_companyInformation(self):
    url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol="+ self.symbol + "&apikey=" + os.getenv('KEY')
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['Name']

  def set_color(self):
    if self.company[today.strftime("%Y-%m-%d")]['4. close'] > self.company[today.strftime("%Y-%m-%d")]['1. open']:
      return 0x00FF00
    else: 
      return 0xEC2B14

  def print_stockInfo(self):
    embedVar = discord.Embed(title=self.name, description="Trading data for " + self.symbol.upper() + " for " + str(today.strftime("%B %d, %Y").replace(' 0', ' ')),color=self.color)
    embedVar.add_field(name="Open", value="$"+str(round(float(self.open),2)),inline=False)
    embedVar.add_field(name="High", value="$"+str(round(float(self.high),2)), inline=False)
    embedVar.add_field(name="Low", value="$"+str(round(float(self.low))), inline=False)
    embedVar.add_field(name="Close", value="$"+str(round(float(self.close),2)), inline=False)
    return embedVar
