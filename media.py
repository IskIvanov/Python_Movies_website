import webbrowser
import fresh_tomatoes

class media_1():
    def __init__ (self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

class Movie(media_1):
    def __init__ (self,movie_title,movie_storyline,poster_image,trailer_youtube):
        media_1.__init__(self,movie_title,movie_storyline,poster_image,trailer_youtube)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Shows(media_1):
    def __init__ (self,movie_title,movie_storyline,poster_image,trailer_youtube,
    show_season,show_episode):
        media_1.__init__(self,movie_title,movie_storyline,poster_image,trailer_youtube)
        self.show_season = season_url
        self.show_episode = episode_url
