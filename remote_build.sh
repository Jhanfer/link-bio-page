source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
API_URL="https://ukory-web.up.railway.app" __LIVE_ROUTE="/live_stream/{user}" __REPO_ROUTE="/repo_ukory" reflex export --frontend-only #se añade la línea de variable de entorno para especificar la "api_url" al exportar el proyecto
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
rm -f remote_build.sh