import web
import json
from datetime import datetime
import random

urls = (
    '/zodiaco/(.*)', 'Zodiaco',
)
app = web.application(urls, globals())

class Zodiaco:
    
    def GET(self, nacimiento):
        try:
            formato = "%d-%m"
            año = "%d-%m-%Y"
            nacimiento = datetime.strptime(nacimiento, año)
            dia = nacimiento.day
            mes = nacimiento.month
            resultado = datetime.strptime(str(dia)+"-"+str(mes), formato)
            indice = random.randint(0, 11)

            horoscopos = ["Debe modificar su conducta agresiva hacia los demás, si no la puede modificar del todo alterne esa agresividad con amor, o sea, si alguien te avienta el carro y más aún si está tuneado, insúltelo, arranque ese mofle escandaloso que suena hasta el cerro o rómpale el parabrisas con la llave de cruz, pero luego, pídale disculpas, dele un beso en la mejilla y dígale: “ta’ todo bien maestro”, si este responde con agresividad, no diga nada, dese vuelta tranquilamente y en el momento que crea oportuno también suéltele un trancazo con la llave de cruz para que aprenda a perdonar el ingrato.",
            "Una grata noticia recibirá esta semana, uno de sus hijos será becado para continuar con sus estudios en Venezuela (le aconsejo que le haga su buen itacate), trate por esto no hacer diferencias con su otro hijo, el ignorante burro bueno para nada.",
            "Cuidado con tu pareja si es que tienes si no mejor ya abandona el sitio. Puede haber una discusión, aunque después de 10 minutos ya no se acordarán porque discutían, pero quien es la mujer en la relación seguirá haciéndolo por gusto, ¡viva la toxicidad!",
            "Tendrá una visita inesperada, los jueves y viernes sentirá como si un loro le hablara al oído, no se confunda, ese loro es, nada más y nada menos que su linda y chismosa suegra, vendrá de visita y se quedará con usted un par de días, en lo posible, trate de no matarla.",
            "Demasiada confusión, es hora de terminar con está oscuridad, tráguese una lámpara prendida y todo su interior quedará iluminado, después prevéngase cómo poder sacarla para cuando se quede sin pilas.",
            "Las cosas estarán un tanto confusas en estos días. Sería aconsejable que evite chocar con sujetos extraños, mejor, choque con parientes así queda todo en familia (más aún si andan echando un ojo a los terrenos).",
            "Esta semana sentirá repulsión por cualquier tipo de carne, de esta manera, despertará al mundo vegetariano, a una nueva forma de vivir, el brócoli y las espinacas serán parte de este nuevo cambio (como Popeye), hasta que el primo de Monterrey les cae con media res, así que la pastura tendrá que esperar y, se armó la “carnita asada” kompa.",
            "En dos días será un día especial para salir a caminar por un río (o donde haya agua, no importa si es un charco), juegue con una piedrita, haga castillitos de arena o de grava, por un momento saque ese niño que hay en su interior, sobre todo si está embarazada. Además, esta semana es ideal para comenzar con los ejercicios físicos, baje esos kilitos demás, esos 57 kilitos que tiene demás, cumpla todas las promesas que hizo para este año y no sea como político en campaña.",
            "Durante los primeros días de la semana demuéstrele a esa persona especial cuánto la aprecia, después humíllela como siempre. Puede ser que las exigencias laborales afecten su estado de ánimo y entre en un pico de estrés, no se altere, recuerde que estrés por dos, son seis.",
            "Si tiene hijos Intégrese con ellos. Uno de ellos descubre que tiene talento con la música, específicamente con la percusión, aliente este talento, cómprele una batería y hágalo feliz y aunque vaya en contra de la felicidad de los vecinos, su desarrollo musical es más importante que la queja de tres viejas de lavadero todas locas. Viernes o sábado le caerá la policía a su casa preguntado si sabe algo de unos ruidos molestos, hágase como el tío “Lolo”, recuerde que si no tienen orden de allanamiento no pueden entrar a revisar si hay o no batería.",
            "Si usted no tiene pareja esto es para ti, este 14 de febrero la persona con la que has intentado que te pele llegará hacia ti, pasarán todo el día juntos, comerán unos tacos al pastor con un Jarrito sabor “rojo” haciendo la clásica “banquetera” y ambos comenzarán a quererse más y más cuando llega el momento más importante del día, ambos se quedarán mirando se acercarán y… ¡ring! ¡ring! suena el despertador y te das cuenta que todo fue un sueño pero no estés triste, eso nunca pasará, como astrónomo te lo digo, nunca te querrá mejor quiérete y deja de soñar esas cosas tontas, en lugar de andar pensando eso ponte a hacer tus tareas que ya casi llega la hora de entrega y no has hecho o ponte a hacer algo y deja de estar de flojo. ¡Ah! y ni si te ocurra hacer alguna fiesta con tus amigos, piensa en los demás y no seas “covidiota”. &#128544;",
            "En estos días entrará en estado de pánico al ser víctima de un robo a mano armada, tiene tres opciones: la primera: retar al delincuente, quitarle la pistola de juguete y entregarlo a la policía; la segunda: quedarse inmóvil con cara de tonto sorprendido, ándele así mero y dejar que el ratero actúe, y la tercera opción: gritar como la vieja castrosa del salón cuando ve una araña mientras corre como Naruto por toda la calle. Pero tampoco le voy a decir que la última opción es la que va a suceder.",]

            data = {}
            
            if resultado >= datetime.strptime("20-01",formato) and resultado <= datetime.strptime("18-02",formato) :
                data["zodiaco"] = "ACUARIO"
                data["fecha"] = "Enero 20 – Febrero 18"
                data["logo"] = "https://15f8034cdff6595cbfa1-1dd67c28d3aade9d3442ee99310d18bd.ssl.cf3.rackcdn.com//uploaded_thumb_medium/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-acuario.png"
                data["elemento"] = "Aire"
                data["color"] = "Azul, Verde-Azul, Gris, Negro"
                data["numeros"] = "4, 8, 13, 17, 22, 26"
                data["horoscopo"] = horoscopos[indice]

            elif resultado >= datetime.strptime("19-02",formato) and resultado <= datetime.strptime("20-03",formato) :
                data["zodiaco"] = "PISCIS"
                data["fecha"] = "Febrero 19 – Marzo 20"
                data["logo"] = "https://15f8034cdff6595cbfa1-1dd67c28d3aade9d3442ee99310d18bd.ssl.cf3.rackcdn.com//uploaded_thumb_medium/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-piscis.png"
                data["elemento"] = "Agua"
                data["color"] = "Mauve, Lila, Púrpura, Violeta, Verde mar"
                data["numeros"] = "3, 7, 12, 16, 21, 25, 30, 34, 43, 52"
                data["horoscopo"] = horoscopos[indice]                

            elif resultado >= datetime.strptime("21-03",formato) and resultado <= datetime.strptime("19-04",formato) :
                data["zodiaco"] = "ARIES"
                data["fecha"] = "Marzo 21 – Abril 19"
                data["logo"] = "https://b282c5de4f50ed30d5ce-25e9f6b52714e6c3d4dbb7e330152014.ssl.cf3.rackcdn.com//uploaded_thumb_medium/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-aries.png"
                data["elemento"] = "Fuego"
                data["color"] = "Rojo"
                data["numeros"] = "1, 9"
                data["horoscopo"] = horoscopos[indice]                
            
            elif resultado >= datetime.strptime("20-04",formato) and resultado <= datetime.strptime("20-05",formato) :
                data["zodiaco"] = "TAURO"
                data["fecha"] = "Abril 20 – Mayo 20"
                data["logo"] = "https://15f8034cdff6595cbfa1-1dd67c28d3aade9d3442ee99310d18bd.ssl.cf3.rackcdn.com//uploaded_thumb_medium/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-tauro.png"
                data["elemento"] = "Tierra"
                data["color"] = "Azul, Rosa, Verde"
                data["numeros"] = "2, 4, 6, 11, 20, 29, 37, 47, 56"
                data["horoscopo"] = horoscopos[indice]               

            elif resultado >= datetime.strptime("21-05",formato) and resultado <= datetime.strptime("20-06",formato) :
                data["zodiaco"] = "GÉMINIS"
                data["fecha"] = "Mayo 21 – Junio 20"
                data["logo"] = "https://b282c5de4f50ed30d5ce-25e9f6b52714e6c3d4dbb7e330152014.ssl.cf3.rackcdn.com//uploaded_thumb_medium/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-geminis.png"
                data["elemento"] = "Aire"
                data["color"] = "Verde, Amarillo"
                data["numeros"] = "3, 8, 12, 23"
                data["horoscopo"] = horoscopos[indice]               

            elif resultado >= datetime.strptime("21-06",formato) and resultado <= datetime.strptime("22-07",formato) :
                data["zodiaco"] = "CÁNCER"
                data["fecha"] = "Junio 21 – Julio 22"
                data["logo"] = "https://b282c5de4f50ed30d5ce-25e9f6b52714e6c3d4dbb7e330152014.ssl.cf3.rackcdn.com//uploaded_thumb_medium/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-cancer.png"
                data["elemento"] = "Agua"
                data["color"] = "Blanco"
                data["numeros"] = "2, 7, 11, 16, 20, 25"
                data["horoscopo"] = horoscopos[indice]                

            elif resultado >= datetime.strptime("23-07",formato) and resultado <= datetime.strptime("22-08",formato) :
                data["zodiaco"] = "LEO"
                data["fecha"] = "Julio 23 – Agosto 22"
                data["logo"] = "https://15f8034cdff6595cbfa1-1dd67c28d3aade9d3442ee99310d18bd.ssl.cf3.rackcdn.com//uploaded_thumb_medium/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-leo.png"
                data["elemento"] = "Fuego"
                data["color"] = "Oro, Naranja, Blanco, Rojo"
                data["numeros"] = "1, 4, 10, 13, 19, 22"
                data["horoscopo"] = horoscopos[indice]               
            
            elif resultado >= datetime.strptime("23-08",formato) and resultado <= datetime.strptime("22-09",formato) :
                data["zodiaco"] = "VIRGO"
                data["fecha"] = "Agosto 23 – Septiembre 22"
                data["logo"] = "https://15f8034cdff6595cbfa1-1dd67c28d3aade9d3442ee99310d18bd.ssl.cf3.rackcdn.com//uploaded_thumb_small/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-virgo.png"
                data["elemento"] = "Tierra"
                data["color"] = "Blanco, Amarillo, Beige, Verde Bosque"
                data["numeros"] = "5, 14, 23, 32, 41, 50"
                data["horoscopo"] = horoscopos[indice]                

            elif resultado >= datetime.strptime("23-09",formato) and resultado <= datetime.strptime("22-10",formato) :
                data["zodiaco"] = "LIBRA"
                data["fecha"] = "Septiembre 23 – Octubre 22"
                data["logo"] = "https://15f8034cdff6595cbfa1-1dd67c28d3aade9d3442ee99310d18bd.ssl.cf3.rackcdn.com//uploaded_thumb_small/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-libra.png"
                data["elemento"] = "Aire"
                data["color"] = "Azul verde"
                data["numeros"] = "6, 15, 24, 33, 42, 51, 60"
                data["horoscopo"] = horoscopos[indice]               

            elif resultado >= datetime.strptime("23-10",formato) and resultado <= datetime.strptime("21-11",formato) :
                data["zodiaco"] = "ESCORPIÓN"
                data["fecha"] = "Octubre 23 – Noviembre 21"
                data["logo"] = "https://15f8034cdff6595cbfa1-1dd67c28d3aade9d3442ee99310d18bd.ssl.cf3.rackcdn.com//uploaded_thumb_small/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-escorpio.png"
                data["elemento"] = "Agua"
                data["color"] = "Escarlata, Rojo"
                data["numeros"] = "9, 18, 27, 36, 45, 54, 63, 72, 81, 90"
                data["horoscopo"] = horoscopos[indice]              

            elif resultado >= datetime.strptime("22-11",formato) and resultado <= datetime.strptime("21-12",formato) :
                data["zodiaco"] = "SAGITARIO"
                data["fecha"] = "Noviembre 22 - Diciembre 21"
                data["logo"] = "https://15f8034cdff6595cbfa1-1dd67c28d3aade9d3442ee99310d18bd.ssl.cf3.rackcdn.com//uploaded_thumb_small/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-sagitario.png"
                data["elemento"] = "Fuego"
                data["color"] = "Violeta, Púrpura, Rojo, Rosa"
                data["numeros"] = "3, 12, 21, 30"
                data["horoscopo"] = horoscopos[indice]               

            else:
                data["zodiaco"] = "CAPRICORNIO"
                data["fecha"] = "Diciembre 22 – Enero 19"
                data["logo"] = "http://15f8034cdff6595cbfa1-1dd67c28d3aade9d3442ee99310d18bd.ssl.cf3.rackcdn.com//uploaded_thumb_small/e1182d7e88196d77ad6089c8af9f7aeb/signos-zodiaco-capricornio.png"
                data["elemento"] = "Tierra"
                data["color"] = "Marrón, Gris, Negro"
                data["numeros"] = "1, 4, 8, 10, 13, 17, 19, 22, 26"
                data["horoscopo"] = horoscopos[indice]               

            data["status"] = 200
            result = json.dumps(data)
            return result

        except:
            data = {}
            data["status"] = 400
            data["error"] = "Error en la fecha de nacimiento, usa '-' en lugar de '/' con formato DIA-MES-AÑO para ingresar una fecha, además usa números y no palabras. Verifica e intenta de nuevo"
            result = json.dumps(data)
            return result

if __name__ == "__main__":
    app.run()