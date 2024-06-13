import reflex as rx
from link_bio.api.api import live, featured,user_streamer
from link_bio.api.twitch_api import TwitchAPI #se importa la API de Twitch
from link_bio.model.featured import Featured

#inicializamos la API
TWITCH_API=TwitchAPI() 

class PageState(rx.State):
    is_live:bool=False
    live_title:str
    live_game_name:str

    feature_info:list[Featured]

    streamer:str

    async def check_live(self):

        #supabase db
        self.streamer=await user_streamer() #Get streamer name from db

        #get streamer live -> bool
        self.is_live = await live(self.streamer)
        
        #get stream info
        dict= TWITCH_API.get_title(self.streamer)
        self.live_title=dict["title"]
        self.live_game_name=dict["game_name"]


    async def feature_links(self):
        self.feature_info=await featured() #Highlights function 
