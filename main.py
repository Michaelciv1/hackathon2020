import random
import discord
import requests
import json
import os
from keep_alive import keep_alive

client = discord.Client()
print(os.getenv("TOKEN"))

def get_dogGIF():
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  json_data = json.loads(response.text)
  return json_data['message']

def get_catGIF():
  response = requests.get("https://api.thecatapi.com/v1/images/search")
  json_data = json.loads(response.text)
  return json_data[0]['url']

def encourage():
  response_list = ["No balls you won't", "I hope you do", "Good"]
  return random.choice(response_list)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('hello'):
      await message.channel.send('Hello!')

    if message.content.startswith('dog please'):
      await message.channel.send(get_dogGIF())

    if message.content.startswith('cat please'):
      await message.channel.send(get_catGIF())

    if message.content.startswith('I wanna kill myself'):
      await message.channel.send(encourage())

keep_alive()
client.run(os.getenv('TOKEN'))

