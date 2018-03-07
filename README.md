# Orchid 

## Development

This is currently a project in its initial stage of development. External contributions are welcome in the form of code reviews, critics and suggestions. One of the original purposes with this is to grow and consolidate my skills developing web applications, but if you'd like to contribute as a designer or developer, feel free to get in touch.


## The project

The idea is to build an **open-source** website where registered users can create profiles and post *original content* produced by them. The publications can be posted in the form of **pictures**, **audio**, **video**, **text**. Users will also be able to upload *short code scripts* which can be ran when visiting their profiles, generating a *personalised user experience* for each personal page. 

It'll also involve a separate section of **articles** to be posted for discussions, relating to the type of content vehiculed by the website.


# Tools

This application is built in Python using the Django framework for web applications. Styling and design use HTML5 and CSS.



# Instructions of use

## Installation

### Requirements
In your preferred virtual environment for this purpose, in the top directory of the repository (`orchid`), run in the bash shell:

    $ pip install -r requirements.txt

Add a file named `.env` in the top directory as well and manipulate environment variables from there.

### Storage and initial setup
The application uses Postgres as the default database, so make sure you have that installed. The version using during development was 9.6. 
You can change the `DATABASES` `ENGINE` in the base settings if you prefer to use a different database as well.

1. Create a new database named `orchid`, and set the DATABASE_URL in the `.env` file.

2. Run initial migrations for the app from the top directory:

    `$ application/manage.py runserver`


## Runing the application
Start the server from the top directory:

    $ application/manage.py runserver

Access the website at `localhost:8000`.


## Serving staticfiles


Collect static files in order to serve them from the `builds` directory. You can do this by running from the top directory:

    $ application/manage.py collectstatic

_This process will be changed soon as it's not ideal having to build the front-end when running the application locally._
