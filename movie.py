import webbrowser


# class movie with constructor and showTrailer method
class Movie():

    # initializes movie instance with title, storyline,
    # poster image, and trailer
    def __init__(self, movieTitle, movieStoryline,
                 posterImage, trailer_youtube_url):
        self.title = movieTitle
        self.storyline = movieStoryline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailer_youtube_url

    # opens the url that is specified in ()
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
