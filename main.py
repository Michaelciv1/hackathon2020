import random
import discord
from alpha_vantage.timeseries import TimeSeries
import requests
import json
import os
from keep_alive import keep_alive
from datetime import date
from datetime import timedelta 

client = discord.Client()
ts = TimeSeries(os.getenv('KEY'))
today = date.today() - timedelta(days = 1)

async def get_stock(message,letters):
  company, meta = ts.get_daily(symbol = letters)
  embedVar = discord.Embed(title="Title", description="Desc", color=0xEC2B14)
  embedVar.add_field(name="Open", value=company['2020-12-31']['1. open'], inline=False)
  embedVar.add_field(name="High", value=company['2020-12-31']['2. high'], inline=False)
  embedVar.add_field(name="Low", value=company['2020-12-31']['3. low'], inline=False)
  embedVar.add_field(name="Close", value=company['2020-12-31']['4. close'], inline=False)
  await message.channel.send(embed=embedVar)
  return(company['2020-12-31'])

def get_randomDog():
  url = "https://dog.ceo/api/breeds/image/random"
  response = requests.get(url)
  json_data = json.loads(response.text)
  return json_data['message']

def get_dogTwoWordBreed(variation, breed):
  url = "https://dog.ceo/api/breed/"+breed+"/"+variation+"/images"
  response = requests.get(url)
  json_data = json.loads(response.text)
  return json_data['message'][random.randint(0,len(json_data['message']))]

def get_dogOneWordBreed(breed):
  url = "https://dog.ceo/api/breed/"+breed+"/images/random"
  response = requests.get(url)
  json_data = json.loads(response.text)
  return json_data['message']

def get_cat():
  response = requests.get("https://api.thecatapi.com/v1/images/search")
  json_data = json.loads(response.text)
  return json_data[0]['url']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  msg = message.content.lower()
  sender = message.author

  if sender == client.user:
    return

  if msg.startswith("!dog"):
    split_msg = msg.split("!dog ")[1]
    if "random" in split_msg:
      await message.channel.send(get_randomDog())
      return
    elif "pitbull" in split_msg:
      await message.channel.send(file=discord.File('./images/pitbull.jpg'))
      return
    elif " " in split_msg:
      breed = split_msg.split(" ")
      first_half_breed = breed[0]
      second_half_breed = breed[1]
      await message.channel.send(get_dogTwoWordBreed(first_half_breed,second_half_breed))
    else:
      await message.channel.send(get_dogOneWordBreed(split_msg))

  if msg.startswith('!stonks'):
    split_msg = msg.split("!stonks ")[1]
    try:
      company, meta = ts.get_daily_adjusted(symbol = split_msg)
      if company[today.strftime("%Y-%m-%d")]['4. close'] > company[today.strftime("%Y-%m-%d")]['1. open']:
        color1 = 0x00FF00
      else: 
        color1 = 0xEC2B14
      embedVar = discord.Embed(title=split_msg.upper(), description="Trading data for " + split_msg.upper() + " for " + today.strftime("%B %d, %Y"),color=color1)
      embedVar.add_field(name="Open", value="$"+str(round(float(company[today.strftime("%Y-%m-%d")]['1. open']),2)),inline=False)
      embedVar.add_field(name="High", value="$"+str(round(float(company[today.strftime("%Y-%m-%d")]['2. high']),2)), inline=False)
      embedVar.add_field(name="Low", value="$"+str(round(float(company[today.strftime("%Y-%m-%d")]['3. low']),2)), inline=False)
      embedVar.add_field(name="Close", value="$"+str(round(float(company[today.strftime("%Y-%m-%d")]['4. close']),2)), inline=False)
      await message.channel.send(embed=embedVar)
    except KeyError:
      print("not found")

  if msg.startswith('cat please'):
    await message.channel.send(get_cat())

  if msg.startswith('WAP please'):
    await message.channel.send(get_cat())

  if msg.startswith('thank you bot'):
    await message.channel.send("my pleasure")

  if msg.startswith('money please'):
    await message.channel.send(file=discord.File('./images/moneyman.jpeg'))


keep_alive()
client.run(os.getenv('TOKEN'))

