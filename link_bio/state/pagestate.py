import reflex as rx
from link_bio.api.api import live
from link_bio.api.twitch_api import TwitchAPI #se importa la API de Twitch

#inicializamos la API
TWITCH_API=TwitchAPI() 
var1="thedanirep"
var2="nexxuz"
USER=var2



class PageState(rx.State):
    is_live:bool=False
    live_title:str="No estoy en directo"
    live_game_name:str="Estate al pendiente de mis canales"

    def check_live(self):
        self.is_live = live(USER)
        dict= TWITCH_API.get_title(USER)
        self.live_title=dict["title"]
        self.live_game_name=dict["game_name"]


    def title() -> dict:
        dict=TWITCH_API.get_title(USER)
        return dict


"""def check_live() -> bool:
    return live(USER)"""

"""def titles(val):
    return PageState.title(val)
"""