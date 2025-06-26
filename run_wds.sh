echo "Preparing to run the server"

pip install -r requirements.txt
cd mybaseproject
python manage.py runserver
