import link_bio.styles.constants as ct
import reflex as rx
from link_bio.api.twitch_api import TwitchAPI #se importa la API de Twitch

#inicializamos la API
TWITCH_API=TwitchAPI() 

def live(user:str) -> bool:
    return TWITCH_API.is_live(user)
    
async def repo() -> str:
    return "https://github.com/Jhanfer/link-bio-page"



