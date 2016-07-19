class Movie:

    """
    This class holds relevant data about the movie such as title and
    release year.

    Attributes:
        title (str): the title of the movie
        release_year (str): the release year of the movie
        actors (str): list of main actors in the movie
        rating (int): integer between 1 and 100 indicating the rating
        		of the movie
        poster_image_url (str): URL containing the image of the movie poster
        trailer_youtube_url (str): URL containing the youtube trailer for the
        		movie

    """

    def __init__(self, movie_title, movie_release_year, movie_actors,
                 movie_rating, movie_poster_image_url,
                 movie_trailer_youtube_url):
        """
        Args:
            movie_title (str): the title of the movie
            movie_release_year (str): the release year of the movie
            movie_actors (str): list of main actors in the movie
            movie_rating (int): integer between 1 and 100 indicating the
            		rating of the movie
            movie_poster_image_url (str): URL containing the image of the
            		movie poster
            movie_trailer_youtube_url (str): URL containing the youtube
          			trailer for the movie

        """

        self.title = movie_title
        self.release_year = movie_release_year
        self.actors = movie_actors
        self.rating = movie_rating
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url
