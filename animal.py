import random
import requests
import json

class Animal:
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