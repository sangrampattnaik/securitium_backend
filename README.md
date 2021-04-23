# Securitium Back End Test API

 Note - 1: python 3.8 or above should be installed

## step - 1
clone the project <br >
` git clone https://github.com/sangrampattnaik/securitium_backend.git`


## step - 2
create a virtual environment with name venv and activate <br >
`virtualenv venv` <br >
`source venv/bib/activate`


## step - 3
install depedancies <br >
`make initial-setup`


## step - 4
create databases <br >
`make migrate` <br >
or <br >

`python manage.py makemigrations`
`python manage.py migrate`

## step - 5
create admin <br >
`make superuser` <br >
or <br >
`python manage.py superuser`

## step - 6
runserver <br >
`make runserver` <br >
or <br >
`python manage.py runserver`

## step - 7
swagger documentaion <br >
`http://127.0.0.1:8000/swagger/`

or REDOC ducumentsion<br >
`http://127.0.0.1:8000/redoc/`

# How To use API
## after creating super admin follow the swagger documentaion 