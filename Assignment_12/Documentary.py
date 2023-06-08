from Media import MediaClass
class DocumentaryClass(MediaClass) :
    def __init__(self , lang , country):
        super().__init__()
        self.language = lang 
        self.country = country 
