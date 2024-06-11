import link_bio.styles.constants as ct
import reflex as rx
from link_bio.api.twitch_api import TwitchAPI #se importa la API de Twitch
from link_bio.api.supabase_api import SupabaseAPI

#inicializamos la API de Twitch
TWITCH_API=TwitchAPI() 

#Inicializamos la API de Supabase
SUPABASE_API=SupabaseAPI()


async def live(user:str) -> bool:
    return TWITCH_API.is_live(user)
    
async def repo() -> str:
    return "https://github.com/Jhanfer/link-bio-page"


async def featured() -> list:
    return SUPABASE_API.fearured()

async def user_streamer() -> str:
    return SUPABASE_API.streamer_user()
