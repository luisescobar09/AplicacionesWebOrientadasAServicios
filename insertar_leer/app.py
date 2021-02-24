import web
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

urls = (
    '/data?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros:

    json_file = {}

    def GET(self):

        parametros = web.input()
        action = parametros.action

        if action == "get".replace(" ",""):
            return self.Leer()
        elif action == "put".replace(" ",""):
            nombre = parametros.nombre
            nacimiento = parametros.nacimiento
            return self.Ingresar(nombre, nacimiento)
        else:
            data = {}
            data["result"] = "Acción no encontrada."
            data["status"] = 404 
            return json.dumps(data)


    def Ingresar (self, nombre, nacimiento):
        try:
            fecha_nacimiento = datetime.strptime(nacimiento, "%d-%m-%Y")
            edad = relativedelta(datetime.now(), fecha_nacimiento)
            edad = (f"{edad.years} años.")
            persona = {}
            persona["nombre"] = nombre
            persona["fecha_nacimiento"] = nacimiento
            persona["edad"] = edad
            
            try:
                with open("static/datos.json") as file:
                    self.json_file = json.load(file)
                    self.json_file["personas"].append(persona)
                    with open("static/datos.json","w") as file:
                        json.dump(self.json_file, file)
                        data = {}
                        data["success"] = "Persona agregada correctamente."
                        data["status"] = 200
                        return json.dumps(data)
            except:
                data = {}
                data["error"] = "Error al intentar leer o escribir en archivo."
                data["status"] = 404
                return json.dumps(data)
            
        except:
            data = {}
            data["error"] = "Verifica datos. Error en nombre o fecha"
            data["status"] = 404
            return json.dumps(data)

    def Leer(self):
        with open("static/datos.json") as file:
            self.json_file = json.load(file)
            return json.dumps(self.json_file)

if __name__ == "__main__":
    app.run()