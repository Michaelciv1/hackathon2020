import random
import discord
import requests
import json
import os
from keep_alive import keep_alive

client = discord.Client()

def get_randomDog():
  url = "https://dog.ceo/api/breeds/image/random"
  response = requests.get(url)
  json_data = json.loads(response.text)
  print(json_data['message'])
  return json_data['message']

def get_dogTwoWordBreed(variation, breed):
  url = "https://dog.ceo/api/breed/"+breed+"/"+variation+"/images"
  print(url)
  response = requests.get(url)
  json_data = json.loads(response.text)
  return json_data['message'][random.randint(0,len(json_data['message']))]

def get_dogOneWordBreed(breed):
  url = "https://dog.ceo/api/breed/"+breed+"/images"
  print(url)
  response = requests.get(url)
  json_data = json.loads(response.text)
  return json_data['message'][1]

def get_cat():
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
    split_msg = msg.split("!dog ")[1]
    if "random" in split_msg:
      print(True)
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


  if msg.startswith('cat please'):
    await message.channel.send(get_cat())

  if msg.startswith('WAP please'):
    await message.channel.send(get_cat())

  if msg.startswith('money please'):
    await message.channel.send(file=discord.File('./images/moneyman.jpeg'))


keep_alive()
client.run(os.getenv('TOKEN'))

