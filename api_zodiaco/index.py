import web
import requests
from datetime import datetime

render = web.template.render("api_zodiaco/")

class Index():

  def GET(self):
    datos = None
    return render.index(datos)

  def POST(self):
    form = web.input()
    nacimiento = form.nacimiento
    año = "%Y-%m-%d"
    nacimiento = datetime.strptime(nacimiento, año)
    dia = nacimiento.day
    mes = nacimiento.month
    anio = nacimiento.year
    resultado = str(dia)+"-"+str(mes)+"-"+str(anio)
    
    result = requests.get("https://pruebaapi.josluisluis4.repl.co/zodiaco/"+str(resultado))
    zodiaco = result.json()


    nombre = zodiaco["zodiaco"]
    fecha = zodiaco["fecha"]
    logo = zodiaco["logo"]
    elemento = zodiaco["elemento"]
    color = zodiaco["color"]
    numeros = zodiaco["numeros"]
    horoscopo = zodiaco["horoscopo"]

    imagen = "<img src=\""+logo+"\"  align='center' width='350' height='300'>"

    datos = {
      "nombre": nombre,
      "fecha": fecha,
      "logo": imagen,
      "elemento": elemento,
      "color": color,
      "numeros": numeros,
      "horoscopo": horoscopo
    }
    return render.index(datos)