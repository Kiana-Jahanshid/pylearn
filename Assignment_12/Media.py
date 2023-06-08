import pytube
class MediaClass :
    def __init__(self ,code , mediatype , name , director , imdb , url ,   year ,duration ,  casts ) :
        self.code = code
        self.name = name 
        self.director = director
        self.imdb_score = imdb 
        self.url = url
        self.duration = duration
        self.casts = casts #listi az actor hast  
        self.mediatype = mediatype
        self.year = year 


    def show_info(self) :
        info = self.name + "   --- mediatype:["+ self.mediatype +"]" + "  --- Director:["+ self.director +"]" + "  --- IMDB:["+ self.imdb_score +"]\n" \
                + "   --- url:[" + self.url + "]" +"   --- year:["+ self.year +"]" + "  --- Duration:["+ self.duration +"]\n"  \
                    + "  --- Casts:[" + self.casts + "]"                                                

        print(info)


    def download(self) :
        stream = pytube.YouTube(self).streams.first()
        stream.download(output_path= './'  ,   filename= 'media.mp4')


        