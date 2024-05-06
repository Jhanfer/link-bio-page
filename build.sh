.\.link_bio\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -rf public
zip -r frontend.zip -d public
rm -f frontend.zip
deactivate