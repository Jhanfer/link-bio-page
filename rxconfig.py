import reflex as rx
import os
import dotenv

dotenv.load_dotenv()
__API_URL=os.environ.get("API_URL")

config = rx.Config(
    app_name="link_bio",
    api_url=__API_URL,
    cors_allowed_origins=[
        "https://www.ukory.es",
        "http://localhost:3000"
    ] # se añade el "cors_allowed_origins" para permitir desde donde se va apoder conectar el backend
)