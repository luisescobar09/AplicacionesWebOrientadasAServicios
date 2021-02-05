import requests
import json

api =('https://api.football-data.org/v2/competitions/PL/matches')
headers = { 'X-Auth-Token': '7a3b0df07f7a4c949dfe74e24f679d79', 'Accept-Encoding': '' }

result = requests.get(api, headers=headers)
#print(result.status_code)
matches = result.json()
#print(matches.keys())

items = matches["matches"]
encoded = json.dumps(items)
decoded = json.loads(encoded)
#print(decoded[1].keys())
'''
print("Fecha:",decoded[0]["utcDate"])
print(decoded[0]["homeTeam"]["name"],"VS",decoded[0]["awayTeam"]["name"])
print(str(decoded[0]["score"]["fullTime"]["homeTeam"])+"-"+str(decoded[0]["score"]["fullTime"]["awayTeam"]))'''

'''fecha = (decoded[300]["utcDate"])
today = datetime.now()
#print(today)
print(len(decoded))

print(fecha)
print(str(today) < fecha)'''

partidos=[]
for i in decoded:
  jornada= i["matchday"]
  partido = i["homeTeam"]["name"]+" VS "+i["awayTeam"]["name"]
  fecha = i["utcDate"]
  resultado_loc = str(i["score"]["fullTime"]["homeTeam"]) 
  resultado_vis = str(i["score"]["fullTime"]["awayTeam"])
  marcador = "Marcador: "+str(i["score"]["fullTime"]["homeTeam"])+"-"+str(i["score"]["fullTime"]["awayTeam"])

  datos = {
  "matchday": jornada,
  "partido": partido,
  "fecha" : fecha,
  "marcador" : marcador
  }
  partidos.append(datos)
for j in partidos:
  if j["matchday"] == 23:
    fecha = "Fecha: "+str(j["fecha"]).replace("T"," ").replace("Z","")+" UTC"
    print(fecha)
    print(str(j["matchday"])+".- "+str(j["partido"]))

    if j["marcador"].count("None") == 2:
      marcador = "Por disputarse"
      print(marcador)
    else:
      print(j["marcador"])



