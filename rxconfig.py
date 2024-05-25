import reflex as rx

config = rx.Config(
    app_name="link_bio",
    api_url="https://api.ukory.es", # se añade la api url crada en railway 
    cors_allowed_origins=[
        "https://www.ukory.es",
        "http://localhost:3000"
    ] # se añade el "cors_allowed_origins" para permitir desde donde se va apoder conectar el backend
)