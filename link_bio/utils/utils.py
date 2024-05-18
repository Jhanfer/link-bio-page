import reflex as rx


#common
preview="icons/favicon.ico"
_meta=[
    {"name":"og:type","content":"website"},
    {"name":"og:image","content":preview},
    {"name":"twitter:card","content":"summary_large_image"},
    {"name":"twitter:site","content":"@koryunderg"}]

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'"),


#index@
index_title="uKory; | Streamer y programador"
index_description="Hola, mi nombre es Jhan y soy un pequeño streamer y programador en Python. Actualmente, me dedico a estudiar más acerca de este increíble lenguaje..."
index_meta=[
    {"name":"og:title","content":index_title},
    {"name":"og:description","content":index_description}]
index_meta.extend(_meta)

#courses@
courses_title="uKory; | Cursos"
courses_description="Cursos que he realizado o que estoy realizando."
courses_meta=[
    {"name":"og:title","content":courses_title},
    {"name":"og:description","content":courses_description}]
courses_meta.extend(_meta)

#repos@
repos_title="uKory; | Repos"
repos_description="Repositorios donde iré subiendo los proyectos que voy realizando"
repos_meta=[
    {"name":"og:title","content":repos_title},
    {"name":"og:description","content":repos_description}]
repos_meta.extend(_meta)
