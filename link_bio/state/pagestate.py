import reflex as rx
from link_bio.api.api import live, featured,user_streamer
from link_bio.api.twitch_api import TwitchAPI #se importa la API de Twitch

#inicializamos la API
TWITCH_API=TwitchAPI() 

class PageState(rx.State):
    is_live:bool=False
    live_title:str
    live_game_name:str
    feature_info:str
    streamer:str

    async def check_live(self):
        self.streamer=await user_streamer()
        self.is_live = await live(self.streamer)
        dict= TWITCH_API.get_title(self.streamer)
        self.live_title=dict["title"]
        self.live_game_name=dict["game_name"]


    async def title(self) -> dict:
        dict=TWITCH_API.get_title(self.streamer)
        return dict

    async def feature_links(select):
        featured_info=await featured()