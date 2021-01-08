from animal import Animal
from stonks import Stonks
import discord
import os
from keep_alive import keep_alive

client = discord.Client()

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
      await message.channel.send(Animal.get_randomDog())
      return
    elif "pitbull" in split_msg:
      await message.channel.send(file=discord.File('./images/pitbull.jpg'))
      return
    elif " " in split_msg:
      breed = split_msg.split(" ")
      first_half_breed = breed[0]
      second_half_breed = breed[1]
      await message.channel.send(Animal.get_dogTwoWordBreed(first_half_breed,second_half_breed))
    else:
      await message.channel.send(Animal.get_dogOneWordBreed(split_msg))

  if msg.startswith('cat please'):
    await message.channel.send(Animal.get_cat())

  if msg.startswith('WAP please'):
    await message.channel.send(Animal.get_cat())

  if msg.startswith('!stonks'):
    stonksobject = Stonks(message.content.lower())
    await message.channel.send(embed = stonksobject.print_stockInfo())

  if msg.startswith('thank you bot'):
    await message.channel.send("my pleasure")

  if msg.startswith('money please'):
    await message.channel.send(file=discord.File('./images/moneyman.jpeg'))


keep_alive()
client.run(os.getenv('TOKEN'))

