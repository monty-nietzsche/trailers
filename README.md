# About Movie Trailers
A web project to browse new movies and see their trailers.
This project is the first project in the Nanodegree as a Full-Stack Developer by #Udacity.

# Files Content
It is writte in python and consists of a python file 'index.py' and folders:
- css : Storing css files (containing main.css)
- js : Storing js files (containing main.js)
- py : Storing py files (containing media.py and fresh_tomatoes.py)
- data: Storing data files (containing movies.dat)

# Running the code
Running the code to generate the movie trailers webpage is easy:
1- Clone the repository on your PC or Mac
2- Run 'index.py' using python IDLE or any other software using a python environment. 
3- The generated webpage will appear in your default browser
4- Please comment if any errors occur.

# Algorithm details
index.py is the mastermind and is responsible for creating index.html and running it in browser. 
movies.dat is a csv file i.e. a database of movies containing title, director, genres, storyline, link to youtube trailer, link to poster as well as imdb.id which allows the web application to create a link to the imdb website to read more about the movie.
media.py contains the Movie class that is used to generate instances of the movies (obtained from the database) as well as the html code.

The main steps of this python project are:
- index.py reads the database and imports the movies' list.
- index.py uses this list to generate an array of objects, instances of the class Movie (in py.media).
- index.py sends the array of objects to the function create_movies_page in py.fresh_tomatoes.py.
- index.py receives the html code returned/sent by the function create_movies_page and saves it to the file 'index.html'.
- index.py opens the newly created page 'index.html' in the default browser.

# Important: 
All information as well as the pictures used in this project are collected from the website: www.movie-list.com
