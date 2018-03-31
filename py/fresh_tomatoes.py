import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="css/main.css">
    <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="js/main.js"></script>

</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
   <body>
      <!-- Trailer Video Modal -->
      <div class="modal" id="trailer">
         <div class="modal-dialog" style="background-color:transparent !important;">
            <div>
               <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
               <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
               </a>
               <div class="modal-content" style="background-color:transparent !important;">
                  <div class="movie-info col-lg-3" id="movie-title"></div>
                  <div class="scale-media col-lg-9" id="trailer-video-container">
                  </div>
               </div>
            </div>
         </div>
      </div>
      <!-- Main Page Content -->
      <div class="container">
         <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <div class="container">
               <div class="navbar-header">
                  <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
               </div>
            </div>
         </div>
      </div>
      <div class="container">
         {movie_tiles}
      </div>
      <div class="myfooter">Udacity Nanodegree [Full Stack Developer] - Project 1 - Montasser Ghachem</div>
   </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-3 movie-tile text-center"
        data-trailer-youtube-id="{trailer_youtube_id}" data-title="{movie_title}" data-storyline="{movie_storyline}"
        data-director="{movie_director}" data-imdb="{movie_imdb}" data-genres="{movie_genres}"
        data-toggle="modal" data-target="#trailer">
            <img src="{poster_image_url}" width="220" height="342">
            <h3>{movie_title}</h3>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        # youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        # youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        # trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            movie_director=movie.director,
            movie_genres=movie.genres,
            movie_imdb=movie.imdb,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=movie.trailer_youtube_id
        )
    return content

def create_movies_page(movies):

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Put the webpage together
  whole_page= main_page_head + rendered_content

  return whole_page



def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('../fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
