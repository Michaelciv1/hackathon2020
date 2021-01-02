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

def get_dogByBreed(variation, breed):
  url = "https://dog.ceo/api/breed/"+breed+"/images"
  print(url)
  response = requests.get(url)
  json_data = json.loads(response.text)

  #create a separate list from the main list of just the variations of the breed that we want
  #maybe try first and last index of the breed then just use random to pick and index for a random photo

  return json_data['message'][1]

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
    split_msg = msg.split("!dog ")[1]
    if "random" in split_msg:
      print(True)
      await message.channel.send(get_randomDog())
      return
    breed = split_msg.split(" ")
    first_half_breed = breed[0]
    second_half_breed = breed[1]
    await message.channel.send(get_dogByBreed(first_half_breed,second_half_breed))


  if msg.startswith('cat please'):
    await message.channel.send(get_catGIF())

  if msg.startswith('WAP please'):
    await message.channel.send(get_catGIF())

  if msg.startswith('money please'):
    await message.channel.send(file=discord.File('./images/moneyman.jpeg'))


keep_alive()
client.run(os.getenv('TOKEN'))

