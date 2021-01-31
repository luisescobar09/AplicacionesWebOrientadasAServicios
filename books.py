import requests
import json

result = requests.get("https://www.googleapis.com/books/v1/volumes?q=la leyenda de la llorona")

book = result.json()

items = book["items"]
#print(items)
encoded = json.dumps(items)
decoded = json.loads(encoded)

print(items)

for i in range (len(items)):

  print(decoded[i]["volumeInfo"]["title"]) #titulo del libro

  try:
    for j in range (len(decoded[1]["volumeInfo"]["authors"])):
      print(decoded[i]["volumeInfo"]["authors"][j]) #autor
  except Exception as error:
    print("No hay autor disponible.")
  
  try:
    print(decoded[i]["volumeInfo"]["imageLinks"]["smallThumbnail"])#imagen del libro
  except Exception as error:
    print("http://books.google.com.mx/googlebooks/images/no_cover_thumb.gif") #imagen alternativa
    
  print(decoded[i]["volumeInfo"]["infoLink"]) #enlace para comprar