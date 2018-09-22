import webbrowser


# This class is to be used to create movie objects.
class Movie():
    # Called upon initialization.
    # Gathers the information required for our movie object.
    def __init__(self, movie_tile, poster_image, trailer_youtube):
        self.title = movie_tile
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
