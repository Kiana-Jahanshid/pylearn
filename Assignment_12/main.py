from Media import MediaClass
from Film import FilmClass
from Series import SeriesClass
from Documentary import DocumentaryClass
from Clip import ClipClass
from Actor import ActorClass
import Media
global MEDIALIBRARY , media_list
MEDIALIBRARY = []

class Main :

    @staticmethod
    def read_from_db():
        global file , MEDIALIBRARY
        file = open ("database.txt" , "r")
        line = file.readline().rstrip("\n")
        for line in file :
            item = line.split("|")
            media_list = MediaClass(item[0] , item[1] , item[2] , item[3] , item[4] , item[5] , item[6], item[7]  , item[8])
            MEDIALIBRARY.append(media_list)        
            line = file.readline().rstrip("\n")

        file.close()

    
    @staticmethod
    def show_menu():
        print("\n0- show database ")
        print("1- Add media ")
        print("2- Edit media")
        print("3- Remove media")
        print("4- Search media")
        print("5- Download media")
        print("6- show menu list ")
        print("7- Exit ")


    @staticmethod
    def showdb():
        file = open ("database.txt" , "r")
        line = file.readline().rstrip("\n")
        for line in file :
            item = line.split("|")
            media_list = MediaClass(item[0] , item[1] , item[2] , item[3] , item[4] , item[5] , item[6], item[7]  , item[8])
            MEDIALIBRARY.append(media_list)        
            MediaClass.show_info(media_list)

        file.close()




    @staticmethod
    def add():
        print("please enter new media's informaton :")
        code = input("enter media's code :")
        mediatype = input("enter media's mediatype :")
        name = input("enter media's title :")
        director = input("enter media's director :")
        imdb = input("enter media's imdb score :")
        url = input("enter media's url (without https://):")
        year = input("enter media's year :")
        duration = input("enter media's duration (h:mm:ss):")
        casts = input("enter media's casts (separate each cast with comma) :")
        new_media_obj = Media.MediaClass(code , mediatype , name , director , imdb , url , year , duration , casts)
        MEDIALIBRARY.append(new_media_obj)
        file = open("database.txt" , "a")
        file.write("\n")
        media_str = code +"|"+ mediatype +"|"+ name +"|"+ director +"|"+ imdb +"|"+ url +"|"+ year +"|"+ duration +"|"+ casts
        file.write(media_str)
        file.close()        


    @staticmethod
    def search() :
        print(" which medai filed do you want to search based on ? ")
        print("code \nname \nmediatype \ndirector \nimdb score \ncasts")
        user_field  = input("enter your field :")
        flag = False
        if user_field == "name" :
            user_input = input("type media title :") #search by title
            for media in MEDIALIBRARY :
                if media.name == user_input :
                    MediaClass.show_info(media)
                    flag = True
            if flag == False :
                print("not found ")       
        elif user_field == "code" :
            user_input = input("type media code :") #search by code
            for media in MEDIALIBRARY :
                if media.code == user_input :
                    MediaClass.show_info(media) 
                    flag = True
            if flag == False :
                print("not found ")
        elif user_field == "director" :
            user_input = input("type media director :") #search by director
            for media in MEDIALIBRARY :
                if media.director == user_input :
                    MediaClass.show_info(media)
                    flag = True
            if flag == False :
                print("not found ")
        elif user_field == "mediatype" :
            user_input = input("type media mediatype:") #search by director
            for media in MEDIALIBRARY :
                if media.mediatype == user_input :
                    MediaClass.show_info(media)
                    flag = True
            if flag == False :
                print("not found ")


    @staticmethod
    def write_to_database():
        file = open("database.txt" , "w")#.close()
        i = 0
        for media in MEDIALIBRARY :
            file.write(MEDIALIBRARY[i]) 
            i+=1
        file.close()


    def edit(self):
        global media_list
        user_code = input("enter the media's code which you wana edit :")
        file = open ("Assignment_12/database.txt" , "r")
        print("which field of media do you want to edit ? ")
        print("code \nname \nmediatype \ndirector \nimdb score \nurl \nyear \nduration \ncasts")
        user_field = input("enter your field :")        
        for line in file :    
            item = line.split("|")
            media_list = MediaClass(item[0] , item[1] , item[2] , item[3] , item[4] , item[5] , item[6], item[7]  , item[8])     
            if media_list.code == user_code :
                if user_field == "name" :
                        media_list.name = input("enter new name :")
                elif  user_field == "code" :  
                        media_list.code = input("enter new code :")
                elif  user_field == "mediatype" :     
                        media_list.mediatype = input("enter new mediatype :")
                elif  user_field == "director" :     
                        media_list.director = input("enter new director :")
                elif  user_field == "imdb score" :     
                        media_list.imdb = input("enter new imdb :")
                elif  user_field == "url" :     
                        media_list.url = input("enter new url :")
                elif  user_field == "year" :     
                        media_list.year = input("enter new year :")
                elif  user_field == "duration" :     
                        media_list.duration = input("enter new duration :")
                elif  user_field == "casts" :     
                        media_list.casts = input("enter new cast :")
            
        #media_str = media_list.code +"|"+ media_list.mediatype +"|"+ media_list.name +"|"+ media_list.director +"|"+ media_list.imdb_score +"|"+ media_list.url +"|"+ media_list.year +"|"+ media_list.duration +"|"+ media_list.casts
        #Main.write_to_database()
        Main.showdb()
        print("\n data has been updated successfully ")





    def remove(self):
        deleteLine = input("enter your media line number you want to delete : ") 
        file = open ("database.txt" , "r")
        line = file.readline().rstrip("\n")
        for line in file :
            item = line.split("|")
            media_list = MediaClass(item[0] , item[1] , item[2] , item[3] , item[4] , item[5] , item[6], item[7]  , item[8])
            MEDIALIBRARY.append(media_list)    

        File = "database.txt"
        with open(File, 'r') as filedata:
            inputFilelines = filedata.readlines()
            lineindex = 1
            with open(File, 'w') as filedata:
                for textline in inputFilelines:
                    if lineindex != deleteLine:
                        filedata.write(textline)
                    lineindex += 1
        print("Line",deleteLine,'has been deleted successfully\n') 
        filedata.close()

  



print("~o~o~o~o~  Welcome to MoviePY STORE ~o~o~o~o~")
print("\t\tdata is loading ...")
Main.read_from_db()
obj = Main()
while True :

    Main.show_menu()
    user_choice = int(input("Enter your choice :"))

    if user_choice == 0 :
         Main.showdb()
    
    elif user_choice == 1 :
         Main.add()  
        
    elif user_choice == 2 :
         obj.edit()
                
    elif user_choice == 3 :
         obj.remove()

    elif user_choice == 4 :  
        Main.search()

    elif user_choice == 5 :
        user_input = input("enter 'media's title' which you want to download : ")
        for media in MEDIALIBRARY :
            if media.name == user_input :        
                MediaClass.download(media.url)
    
    elif user_choice == 6 :
        Main.show_menu()
    
    elif user_choice == 7 :
        Main.write_to_database()
        exit(0)
    else :
        user_choice = int(input("Wrong input , try again ... : "))


    
    