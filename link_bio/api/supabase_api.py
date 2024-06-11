import os
import dotenv 
from supabase import create_client, Client #se importa de "supabase" el "create_client" y "Client"

class SupabaseAPI():

    dotenv.load_dotenv()#cargamos las variables de entorno

    #asignamos las variables de entorno
    url:str=os.environ.get("SUPABASE_URL") 
    key:str=os.environ.get("SUPABASE_KEY")

    #aignamos supabase
    supabase:Client=create_client(url,key)

    #definimos la función
    def fearured(self) -> list:
        #asignamos los datos a "response" que traemos de mi tabla de supabase llamada "Featured"
        response=self.supabase.table("Featured").select("*").execute()
        
        #creamos una lista vacía
        featured_data=[]  

        #comprobamos que la respuesta tenga datos e iteramos los elementos para añadirlos sobre una lista
        if len(response.data) > 0:
            for feature_item in response.data:
                featured_data.append(feature_item)
        return featured_data
    
    #función para obtener el usuario de SUPABASE
    def streamer_user(self) -> str:
        response=self.supabase.table("Streame_name").select("*").execute()
        data=[]
        if len(response.data) > 0:
            for item in response.data:
                data.append(item)
        return data[0]["name"]