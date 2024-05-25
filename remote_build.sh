source .link_bio\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
API_URL="https://api.ukory.es" reflex export --frontend-only #se añade la línea de variable de entorno para especificar la "api_url" al exportar el proyecto
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
