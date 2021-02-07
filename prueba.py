import requests
import json
liga = input("Ingresa Liga: ")
jornada = int(input("Ingresa jornada: "))
api =('https://api.football-data.org/v2/competitions/'+liga+'/matches')
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
  if i["matchday"] == jornada:
    partido = i["homeTeam"]["name"]+" VS "+i["awayTeam"]["name"]
    fecha = "Fecha "+i["utcDate"].replace("T"," ").replace("Z","")+" UTC"
    marcador = "Marcador: "+str(i["score"]["fullTime"]["homeTeam"])+"-"+str(i["score"]["fullTime"]["awayTeam"])    
    if marcador.count("None") == 2:
      marcador = "Por disputarse"
    else:
      marcador

    datos = {
      "matchday": jornada,
      "partido": partido,
      "fecha" : fecha,
      "marcador" : marcador
      }
    partidos.append(datos)
    #print(partidos)


for j in partidos:
  fecha = j["fecha"]
  print(fecha)
  game = j["partido"]
  print(game)
  marcador = j["marcador"]
  print(marcador)



