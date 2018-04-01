class Movie:
    """ This class helps organize and gather relevant information about movies.
    The information gathered about each movie are the title, the director, the
    genre(s), a description of the plot or storyline as well as the youtube id
    of the trailer and a link to its poster. To get the youtube link to the
    trailer, you just 'https://youtu.be/' before it.
    Example: The movie 'The outsider' has a trailer_youtube_id of 'QNNcl2mEHzQ.
    The link to the youtube trailer is then 'https://youtu.be/QNNcl2mEHzQ'

    To know more about the movie, the class also includes the movie ID on IMDB.
    Once you have this id, you can create a link to access further information
    about the movie on IMDB.
    Example: The movie 'The outsider' has a IMDB id: tt2011311. It follows that
    the IMDB page of this movie is www.imdb.com/title/tt2011311."""

    def __init__(
        self,
        movie_title,
        movie_director,
        movie_genres,
        movie_storyline,
        movie_poster_url,
        movie_youtube_id,
        movie_imdb_id
    ):
        self.title = movie_title
        self.director = movie_director
        self.genres = movie_genres
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_id = movie_youtube_id
        self.imdb = movie_imdb_id
