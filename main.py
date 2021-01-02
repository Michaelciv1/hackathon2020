import random
import discord
import requests
import json
import os
from keep_alive import keep_alive

client = discord.Client()

def get_dogGIF(breed):
  url = "https://dog.ceo/api/breed/"+str(breed)+"/images/random"
  response = requests.get(url)
  json_data = json.loads(response.text)
  return json_data['message']

def get_catGIF():
  response = requests.get("https://api.thecatapi.com/v1/images/search")
  json_data = json.loads(response.text)
  return json_data[0]['url']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  msg = message.content
  sender = message.author

  if sender == client.user:
    return

  if msg.startswith("!dog"):
    breed = msg.split("!dog ")[1]
    await message.channel.send(get_dogGIF(breed))
    print (breed)

  if msg.startswith('cat please'):
    await message.channel.send(get_catGIF())

  if msg.startswith('WAP please'):
    await message.channel.send(get_catGIF())

  if msg.startswith('money please'):
    await message.channel.send(file=discord.File('./images/moneyman.jpeg'))


keep_alive()
client.run(os.getenv('TOKEN'))

