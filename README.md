# Gif-Search
Implementing the use of Flask, Requests and Jinja learned in class to create a local running website that uses the Tenor API

## Structure
```
gif_search
| - static: Style Sheets
    | - style.css
| - templates: HTML files for Framework
    | - base.html
    | - gif.html
    | - index.html
| - app.py: Flask Framework
```

## Authors
[Omar Sagoo](https://github.com/omarsagoo)

[Luke Parker](https://github.com/)

## Required Modules
Modules required to run this application: Request and Flask
```
~$ pip3 install requests flask

```


## How to Run Flask
To run, open the folder containing `app.py` in a Terminal instance, and run:

```
~$ export FLASK_ENV=development
~$ flask run
```

## Rubric
[Project rubirc here](https://docs.google.com/document/d/1u8zn_w9kQceK1y0f0F6QEWWgP8T7KRsQvQOIvlzyMi0/edit)

## Resources

You may find the following resources helpful in your development process:

1. [Tenor API Documentation](https://tenor.com/gifapi/documentation) - useful for understanding which URL we want to visit in order to make an API request for GIFs
2. [BEW 1.1 Lesson on Flask](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/#/./Lessons/03-Intro-to-Flask/README)
3. [BEW 1.1 Lesson on Templates](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/#/./Lessons/04-Flask-Templating/README)
4. [BEW 1.1 Lesson on APIs](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/#/./Lessons/05-URLs-HTTP-REST-and-Reading-Errors/README)

