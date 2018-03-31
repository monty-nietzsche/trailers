
import webbrowser
import os
import py.fresh_tomatoes
from py.media import Movie


##  [1]  IMPORT FILM DETAILS FROM FILE

# The movies' list exists in a file 'movies.dat'. The file is opened, and read line per line. Each line is transformed
# into a row in our movies' list where each movie has a row.
# The file is a semi-colon separated file. The entries are respectively: Movie Title, Movie Director, Movie Genres,
# Movie Storyline, Movie poster link, Movie Youtube id (not a full link),  IMDB id.
# An example: [The Outsider; MARTIN ZANDVLIET; CRIME,DRAMA,MYSTERY;An epic set in post-WWII Japan
# and centered on an American former G.I. who joins the yakuza.;https://www.movie-list.com/img/posters/big/
# outsider2018.jpg; QNNcl2mEHzQ;tt2011311

movies_list=[]
with open("data/movies.dat",'r') as movies:
    for line in movies:
        movie_details=[detail.strip() for detail in line.split(';')]
        movies_list.append(movie_details)

#  [2]  CREATE MOVIE OBJECTS
        
# Instead of creating individual Movie objects, they are created dynamically from the movies' list created above.
# We just need to get rid of brackets and send the content of each line to the constructor. We get rid of brackets
# through using (*movies_list[i]). Once an object is created, it is added to the array that contains all Movie objects.

my_movies=[]
for i in range(0,len(movies_list)):
    my_movies.append(Movie(*movies_list[i]))

# [3] SEND A REQUEST TO FRESH TOMATOES TO PREPARE PAGE, SAVE AND OPEN THE PAGE
    
# Once the objects' array is full, it is sent to the function  'create_movies_page' in fresh_tomatoes file which we have
# imported above. The function creates the page and sends back the webpage. All is needed now is to save the data received
# into a file 'index.html' and open it.

# Collect the webpage from fresh_tomatoes
whole_page=py.fresh_tomatoes.create_movies_page(my_movies)

# Create or overwrite the output file
output_file = open('index.html', 'w')

# Output the file
output_file.write(whole_page)
output_file.close()

# open the output file in the browser
url = os.path.abspath(output_file.name)
webbrowser.open('file://' + url, new=1) # open in a new tab, if possible



    
