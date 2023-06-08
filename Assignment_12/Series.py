from Media import MediaClass
import pytube

class SeriesClass(MediaClass):
    def __init__(self , seasson , episode , country):
        super().__init__()
        self.numberOfSeassons = seasson
        self.numberOfEpisodes = episode
        self.country = country

    def show_info(self) :
        info = self.name + "   --- mediatype:["+ self.mediatype +"]" + "  --- Director:["+ self.director +"]" + "  --- IMDB:["+ self.imdb_score +"]\n" \
                + "   --- url:[" + self.url + "]" +"   --- year:["+ self.year +"]" + "  --- Duration:["+ self.duration +"]\n"  \
                    + "  --- Casts:[" + self.casts + "]"   +   "  --- seasson:[" + self.numberOfSeassons + "]"   +  "  --- episode:[" + self.numberOfEpisodes + "]"  + \
                        "  --- country:[" + self.country + "]"                                     

        print(info)


    def download(self) :
        stream = pytube.YouTube(self).streams.first()
        stream.download(output_path= './'  ,   filename= 'media.mp4')