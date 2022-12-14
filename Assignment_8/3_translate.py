import gtts
import os 

def read_from_file():
    global WORDS_BANK
    f = open("Assignment_8/translate.txt" , "r")
    file_content = f.read().split("\n")   
    WORDS_BANK = []
    for i in range(0,len(file_content)-1,2):
        my_dict = {"en" : file_content[i] , "fa": file_content[i+1]}
        WORDS_BANK.append(my_dict)
    f.close()


def translate_english_to_persian() :
    user_en_text = input("enter your english text : ")
    user_input = user_en_text.split(" ")
    print(user_input)
    output = ""
    for user_word in user_input :
        for word in WORDS_BANK :
            if user_word == word["en"] :
                output = output + word["fa"] + " "
                break
        else :
            output = output + user_word + " "
    
    print(output + ".")  
    sound = gtts.gTTS(output , lang = "ur" , slow = False )
    sound.save("Assignment_8/voice_fa_1.mp3")



def translate_persian_to_english() :

     user_text = input("enter your persian text : ")
     user_input = user_text.split(" ")
     user_input = user_text.split(".")
     print(user_input)
     output = ""
     for user_word in user_input : 
         for word in WORDS_BANK : 
             if user_word == word["fa"] :
                 output = output + word["en"] + " "
                 break
         else :
             output = output + user_word + " "

     print(output + ".")  
     sound2 = gtts.gTTS(output , lang = "en" , slow = False )
     sound2.save("Assignment_8/voice_en_1.mp3")



   
def add_word( ) :
        en_word = input("enter new english word : ")
        fa_word = input("enter it's persian meaning : ")
        new_word = {"en" : en_word , "fa" : fa_word}
        WORDS_BANK.append(new_word)
        f = open("Assignment_8/translate.txt" , "a")
        f.write("\n")
        f.write(en_word + "\n")
        f.write(fa_word)
        f.close()


def show_menu() :
    print("\n\n~o~o~o~o~  welcome to my translator  ~o~o~o~o~")
    print("1_translate english to persian ")
    print("2_translate persian to english ")
    print("3_add a new word to database ")
    print("4_exit")


read_from_file()
file_path = "D:/pylearn/Assignment_8/translate.txt"
isFile = os.path.isfile(file_path)
print(isFile)
if isFile == True :
    while True :
        show_menu()     
        choice = int(input("enter your choice : "))

        if choice == 1 :
            translate_english_to_persian()
        elif choice == 2 :
            translate_persian_to_english()
        elif choice == 3 :
            add_word()
        elif choice == 4 :
            exit(0)
else : 
    print("file didnt exist in the path ")



# text to voice :
mytext = "i am kiana a python programmer"

x = gtts.gTTS(mytext , lang = "en" , slow = False )
x.save("Assignment_8/voice1.mp3")

"ur"  "ar"