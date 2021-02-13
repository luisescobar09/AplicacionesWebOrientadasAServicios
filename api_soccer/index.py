import web
import requests
import json

render = web.template.render("api_soccer/")
class Index():

  def GET(self):
    partidos = None
    return render.index(partidos)

  def POST(self):
    form = web.input()
    liga = form.liga
    semana = int (form.jorna)

    api =('https://api.football-data.org/v2/competitions/'+liga+'/matches')
    headers = { 'X-Auth-Token': '7a3b0df07f7a4c949dfe74e24f679d79', 'Accept-Encoding': '' }

    result = requests.get(api, headers=headers)
    matches = result.json()
    items = matches["matches"]
    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    partidos=[] 
    for i in decoded:
      jor = i["matchday"]
      if jor == semana:
        partido = i["homeTeam"]["name"]+" VS "+i["awayTeam"]["name"]
        fecha = "Fecha "+i["utcDate"].replace("T"," ").replace("Z","")+" UTC"
        marcador = "Marcador: "+str(i["score"]["fullTime"]["homeTeam"])+"-"+str(i["score"]["fullTime"]["awayTeam"])    
        if marcador.count("None") == 2:
          marcador = "Por disputarse"
        else:
          marcador = "Marcador: "+str(i["score"]["fullTime"]["homeTeam"])+"-"+str(i["score"]["fullTime"]["awayTeam"])
        datos = {
          "matchday": "Jornada "+str(semana),
          "partido": partido,
          "fecha" : fecha,
          "marcador" : marcador
          }
        partidos.append(datos)
        
    return render.index(partidos)


