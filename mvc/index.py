import web
import requests
import json

render = web.template.render("mvc/")

class Index():

  def GET(self):
    datos = None
    return render.index(datos)

  def POST(self):
    form = web.input()
    book_name = form.book_name

    result = requests.get("https://www.googleapis.com/books/v1/volumes?q="+book_name)
    book = result.json()
    items = book["items"]
    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    title = "Título: "+(decoded[0]["volumeInfo"]["title"]) #titulo del libro
    try:
      for j in range (len(decoded[0]["volumeInfo"]["authors"])):
        author = "Autor(es): "+(decoded[0]["volumeInfo"]["authors"][j]) #autor
    except Exception as error:
      author = "No hay autor disponible."
    try:
      image = (decoded[0]["volumeInfo"]["imageLinks"]["smallThumbnail"])#imagen del libro
    except Exception as error:
      image = "http://books.google.com.mx/googlebooks/images/no_cover_thumb.gif" #imagen alternativa  
    url = (decoded[0]["volumeInfo"]["infoLink"]) #enlace para comprar
    titulo = "<h1 class='text-center'>"+title+"<h1>"
    autor = "<h2 class='text-center'>"+author+"<h2>"
    imagen = "<img src=\""+image+"\"  align='center' width='300' height='350'>"
    link ="<a target='blank' class='text-center text-danger' href='"+url+"'>¡Compralo ahora!</a>"

    datos = {
      "titulo": titulo,
      "autores": autor,
      "imagen": imagen,
      "url": link
    }
    return render.index(datos)
