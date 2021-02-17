# URLshortener
URL shortener  - Django app  

## Deployment link
You may check app in action via this link - [uri.herokuapp.com/](https://uri.herokuapp.com/)  
Test credentials: test, test   

## Description
URL shortening app, that lets you create short links. 
User should be able to see:  
* list of created links  
* stats of each short URL (IPs, time and referer of each click)  

## Built with
[Django](https://www.djangoproject.com/) - The web framework used  
[Django URL shortener](https://github.com/ronaldgrn/django-link-shortener) - existing package have been modyfied for this project  

## How to run  
To run project locally, you would need to perform following steps:
1. Pull repo. 
2. In a root folder (one where ```manage.py``` located) run commands:  
```
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python createsuperuser
python manage.py runserver
```
3. Login via ```/admin``` page
4. Open ```/create``` page and create your first short link!  

## Things to do
* Social account login support  
* Delete link function   
* Pagination for links/visits   
* Endless scroll for pagination   
