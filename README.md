## NEWS MVP API
---
### __Postman collection__

[Collection](https://documenter.getpostman.com/view/16061399/UVkvJCnT)
### __Deployed to Heroku__

[Heroku Deploy](http://quiet-brook-63067.herokuapp.com/api/news/)

### __Getting started__

These instructions will get you a copy of the project up and running on your local
machine for development and testing purposes. 

---

#### __Prerequisites__

 This is a project written using Python, Django, and Django Rest Framework

#### __1. Clone the repository__
```
$ git clone https://github.com/BolotZhusupekov07/news-comments-app
```
#### __2. Create .env file 

$ SECRET_KEY = 
$ DEBUG = 
$ ALLOWED_HOSTS = 

$ DB_NAME =
$ DB_USER = 
$ DB_PASSWORD = 
$ DB_HOST = 
$ DB_PORT = 

#### __3. Build the Docker Image__
In terminal:

```
$ docker-compose build 
```

#### __4.Run the project__
Start the development server and ensure everything is running without errors.
```
$ docker-compose up
```
