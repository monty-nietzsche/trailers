class Movie:
    """ This class helps you organize your movies and gather relevant information about each movie."""

    def __init__(self, movie_title, movie_director, movie_genres, movie_storyline, movie_poster_url, movie_youtube_id, movie_imdb_id):
        self.title=movie_title
        self.director=movie_director
        self.genres=movie_genres
        self.storyline=movie_storyline
        self.poster_image_url=movie_poster_url
        self.trailer_youtube_id=movie_youtube_id
        self.imdb=movie_imdb_id

        
        
