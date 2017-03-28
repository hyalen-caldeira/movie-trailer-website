import webbrowser

class Movie():
    """ This class provide a way to store movie related information """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, story, poster, trailer):
        self.title = title
        self.story_line = story
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
