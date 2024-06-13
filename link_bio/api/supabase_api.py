import os
import dotenv 
from supabase import create_client, Client #se importa de "supabase" el "create_client" y "Client"
from link_bio.model.featured import Featured

class SupabaseAPI():

    dotenv.load_dotenv()#cargamos las variables de entorno

    #asignamos las variables de entorno
    url:str=os.environ.get("SUPABASE_URL") 
    key:str=os.environ.get("SUPABASE_KEY")
    supabase:Client

    #funcion para actualizar los datos de supabase y hacer que no pete el back xd
    def act_data(self):
        #aignamos supabase
        if self.url and self.key:
            self.supabase:Client=create_client(self.url,self.key)
        else:
            pass

    #definimos la función
    def fearured(self) -> list[Featured]:

        self.act_data()
        #asignamos los datos a "response" que traemos de mi tabla de supabase llamada "Featured"
        response=self.supabase.table("Featured").select("*").execute()
        
        #creamos una lista vacía
        featured_data=[]  

        #comprobamos que la respuesta tenga datos e iteramos los elementos para añadirlos sobre una lista
        if len(response.data) > 0:
            for featured_item in response.data: #itera
                featured_data.append( #añade los datos a una lista con formato Featured
                    Featured(
                        title=featured_item["title"],
                        image=featured_item["image"],
                        url=featured_item["url"]
                    )
                )
        return featured_data
    
    #función para obtener el usuario de SUPABASE
    def streamer_user(self) -> str:
        self.act_data()
        response=self.supabase.table("Streame_name").select("*").execute()
        data=[]
        if len(response.data) > 0:
            for item in response.data:
                data.append(item)
        return data[0]["name"]
    

    def feature_bool(self):
        self.act_data()

