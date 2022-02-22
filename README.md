# Django Ariadne Starter Project

![alt text](https://static.djangoproject.com/img/logos/django-logo-negative.png)
![alt text](https://ariadnegraphql.org/docs/assets/icon.png)


Django Ariadne Starter Project is meant to help developers and anyone who wants to try and test graphql POWERS without much fuss.

This project can be also used as a boilerplate for starting an API project using GraphQl

## Why GraphQl?
GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.

## Why Ariadne?
### Schema First
Describe your GraphQL API using Schema Definition Language and connect your business logic using a minimal amount of Python boilerplate.

### Simple
A small and easy-to-learn Pythonic API with simplicity as the guiding force behind its design.

### Open Design
Easily add new features to the library, and replace or extend existing ones. Integrate with any web framework you like.

## Why Django?
Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. ... Django helps developers avoid many common security mistakes by providing a framework that has been engineered to "do the right things" to protect the website automatically.


# How To Use ?
To start developing your own GraphQl API you can use this project like such:

### Prerequisites 
To be able to use this code you need `Python3` / Your Prefered IDE (Mine is VS Code)

### Download Repository
Download the github repository into your workspace

    git clone https://github.com/iPalmTech/django_ariadne_starter.git

### Install Requirements
We need to nstall the requirements, so open your project and run

    cd django_ariadne_starter/
    pip install -r requirements.txt

### Run Server
When everything is installed you might run your server with the following command 

    python3 manage.py runserver

### Access Your Server

You might visit http://localhost:8000/ 

And for the graphql view you might visit http://localhost:8000/graphql