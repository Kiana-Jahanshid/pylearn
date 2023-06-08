from Media import MediaClass
class FilmClass (MediaClass):
    def __init__(self , country , genre) :
        super().__init__()
        self.country = country 
        self.genre = genre