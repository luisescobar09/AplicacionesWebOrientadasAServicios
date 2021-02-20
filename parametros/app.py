import web
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

urls = (
    '/datos?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros:

    def GET(self):
        try:
            parametros = web.input()
            nombre = parametros.nombre
            nacimiento = parametros.nacimiento

            fecha_nacimiento = datetime.strptime(nacimiento, "%d-%m-%Y")
            edad = relativedelta(datetime.now(), fecha_nacimiento)
            edad = (f"{edad.years} años.")
            data = {}

            data["nombre"] = nombre
            data["fecha_nacimiento"] = nacimiento
            data["edad"] = edad
            data["status"] = 200

            archivo = open("static/datos.txt","a")
            archivo.write("\nNombre: "+data["nombre"]+"\n")
            archivo.write("Fecha de nacimiento: "+data["fecha_nacimiento"]+".\n")
            archivo.write("Edad: "+data["edad"]+"\n")
            archivo.close()
            return json.dumps(data)
            
        except:
            data = {}
            data["error"] = "Verifica datos. Error 404 not found"
            data["status"] = 404
            return json.dumps(data)

if __name__ == "__main__":
    app.run()