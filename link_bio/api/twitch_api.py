import requests
import os
import dotenv
import time 
#importamos dotenv, os y requests

#creamos una claser de TwitchAPI
class TwitchAPI:

    #cargamos el entorno. Se le puede dar un "path" para que cargue si así se desea.
    dotenv.load_dotenv()

    #cargamos las variables del entorno previamente puestas en ".env".
    CLIENT_ID=os.environ.get("TWITCH_CLIENT_ID")
    CLIENT_SECRET=os.environ.get("TWITCH_CLIENT_SECRET")

    #definimos el constructor de la clase
    def __init__(self) -> None:
        self.token=None
        self.token_exp=0
        self.title=None

    #función para generar los tokens de twitch
    def gen_token(self):
        #hacemos un "post" usando "request" a "https://id.twitch.tv/oauth2/token".
        response=requests.post(
            "https://id.twitch.tv/oauth2/token",
            data={
                "client_id":self.CLIENT_ID,
                "client_secret":self.CLIENT_SECRET,
                "grant_type":"client_credentials"
                #Los datos a cargar en el post y usamos las variables de entorno que hemos creado y obtenido usando "os.environ.get()" de ".env".
            }
        )
        
        #Si la respuesta de "response" es "200 OK" guarda el json de los datos en la variable "data"
        #Accedemos al "acces_token" de los datos anteriormente guardados en "data" y lo asignamos a "token"
        #Accedemos al "expires_in" del json y le sumamos la hora del sistema. Guardamos esos datos en "token_expires"
        if response.status_code == 200:
            data=response.json()
            self.token=data["access_token"]
            self.token_exp=time.time() + data["expires_in"]
        else:
            self.token=None
            self.token_exp=0
        #De no dar "200 OK" vuelve a asignar los valores default de los tokens

    #Retorna "False" cuando el token está expirado o no está generado
    def token_valid(self) -> bool:
        if time.time() < self.token_exp:
            return True
        else:
            return False
    

    #Evalúa si el token está expirado o si no se ha generado y llama a la función para que lo genere
    def is_live(self,user:str) -> bool:
        
        if not self.token_valid():
            self.gen_token()

        #Hacemos un "get" usando "requests" y guardamos los datos en "response".
        response=requests.get(
            f"https://api.twitch.tv/helix/streams?user_login={user}", #le pasamos el usuario a la url de twitch
            headers={
                "Client-Id":self.CLIENT_ID,
                "Authorization":f"Bearer {self.token}"
            }
            #se le pasa el "client_id" y el "Authorization"
        )

        #Comprobamos que el status code de la respuesta sea "200 OK". Además, comprueba si existe data dentro del json de la respuesta, de no ser así, retornamos False

        if response.status_code == 200 and response.json()["data"]:
            return True
        else:
            return False
        


    def get_title(self,user:str,val:str):

        if self.is_live(user) == False:
            if val == "title":
                return "No estoy en vivo"
            else:
                return "Estate al pendiente de todos mis canales"
        else:
            response=requests.get(
            f"https://api.twitch.tv/helix/streams?user_login={user}",
            headers={
                "Client-Id":self.CLIENT_ID,
                "Authorization":f"Bearer {self.token}"})
            
            if response.status_code == 200 and response.json()["data"]:
                data=response.json()["data"]
                return data[0][val]