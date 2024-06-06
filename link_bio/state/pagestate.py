import reflex as rx
from link_bio.api.api import live
from link_bio.api.twitch_api import TwitchAPI #se importa la API de Twitch

#inicializamos la API
TWITCH_API=TwitchAPI() 
var1="theakaleina"
var2="nexxuz"
USER=var2


#No funciona
"""class PageState(rx.State):

    is_live:bool

    async def check_live(self) -> bool:
        live_data = await live(USER)
        self.is_live = live_data
"""

def check_live() -> bool:
    return live(USER)

def titles(val):
    return TWITCH_API.get_title(USER,val)
