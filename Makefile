manage=./manage.py
python=python

runserver:
	@$(python) $(manage) runserver

initial-setup: 
	@pip install -r requirements.txt

superuser:
	@$(python) $(manage) createsuperuser
	

migrate:
	@$(python) $(manage) makemigrations
	@$(python) $(manage) migrate