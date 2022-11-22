import random 

words_bank = ["life" , "computer" , "python" , "machine" , "mobile" , "technology" , "cat" , "programming", "keyboard" , "butterly" , "geek" , ]
user_mistakes = 0 
correct_chars = []
wrong_chars = []

x = random.randint( 0 , len(words_bank)-1)
word = words_bank[x]

#Remove Duplicate Characters from word
strlist = []
for i in range(len(word)):
    strlist.append(word[i])

newlist = []
j = 0
for i in range(len(strlist)):
    if word[i] not in newlist:
        newlist.insert(j, word[i])
        j += 1

word2 = ""
word2 = word2.join(newlist)


while user_mistakes < 6 :
    for i in range (len(word)) :
        if word[i] in correct_chars :
            print(word[i] , end=" ")
        else :    
            print("_ " , end="")

    if  len(word2) == (len(correct_chars)) :
        print("\n ~~~~~~~ you win ~~~~~~~~ ")
        break
    else :
        user_char = input("please write your guess : ")
        user_char = user_char.lower()
        if len (user_char) == 1 :

            if user_char in word :
                correct_chars.append(user_char)
                print("correct guess")
            else :
                wrong_chars.append(user_char)
                user_mistakes += 1
                print("wrong guess")    

        else :
            print(" XX you have entered more than one character XX")




if user_mistakes == 6 :
        print("Game Over")








