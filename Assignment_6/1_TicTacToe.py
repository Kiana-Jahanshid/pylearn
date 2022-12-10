import pyfiglet
import rich
from rich import print
import random
import time
#import colorama   // didn't work 
#import termcolor  // didn't work
start = time.time()
def show():
    for row in game_board :
        for cell in row :
            print(cell , end= " ")   
        print("")

def mytime():
     end = time.time()
     total_time = end - start
     print("\nTotal Duration : "+ str(total_time))

def selectplayer() :  
     if mode == 2 :
         print("~~~~ CPU wins ~~~~")  
     else :
         print("~~~~ player 2 wins ~~~~")

def check_game() :
    for j in range(3):
        for i in range(3):
            if game_board[i][0]=="[red]X[/]" and game_board[i][1]=="[red]X[/]" and game_board[i][2]=="[red]X[/]":      
                 print("~~~~ player 1 wins ~~~~")
                 mytime()
                 exit()
        if game_board[0][j]=="[red]X[/]" and game_board[1][j]=="[red]X[/]" and game_board[2][j]=="[red]X[/]":      
                print("~~~~ player 1 wins ~~~~")
                mytime()
                exit()
    if game_board[0][0]=="[red]X[/]" and game_board[1][1]=="[red]X[/]" and game_board[2][2]=="[red]X[/]":
         print("~~~~ player 1 wins ~~~~")
         mytime()
         exit()
    if game_board[0][2]=="[red]X[/]" and game_board[1][1]=="[red]X[/]" and game_board[2][0]=="[red]X[/]":
         print("~~~~ player 1 wins ~~~~")
         mytime()
         exit()     

    for j in range(3):
        for i in range(3): 
            if game_board[i][0]=="[blue]O[/]" and game_board[i][1]=="[blue]O[/]" and game_board[i][2]=="[blue]O[/]":      
                 selectplayer()
                 mytime()     
                 exit()      
        if game_board[0][j]=="[blue]O[/]" and game_board[1][j]=="[blue]O[/]" and game_board[2][j]=="[blue]O[/]":    
             selectplayer()
             mytime()    
             exit()
    if game_board[0][0]=="[blue]O[/]" and game_board[1][1]=="[blue]O[/]" and game_board[2][2]=="[blue]O[/]":
         selectplayer()
         mytime()
         exit()
    if game_board[0][2]=="[blue]O[/]" and game_board[1][1]=="[blue]O[/]" and game_board[2][0]=="[blue]O[/]":
         selectplayer()
         mytime()
         exit() 
       
def draw_check():
    c= 0
    for col in range(3):
        for row in range(3):
           if game_board [row][col] != "-":
               c+=1
    if c == 9 : 
      print ("~~~~ DRAW ~~~~")
      mytime()
      exit()   

title = pyfiglet.figlet_format("Tic Toc Toe" , font = "slant")
print(title)

print("palyer mode : \n 1_player VS palyer \n 2_player VS CPU ")
mode = int(input("which mode do you want to play ? 1 or 2  ?  "))

game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]

show()
while True :
    print("player 1")
    while True :
        row = int(input("row : "))
        col = int(input("col : "))
        if 0 <= row <= 2 and  0 <= col <= 2 :
            if game_board [row][col] == "-" :
                game_board [row][col] = "[red]X[/]"
                break
            else :
                print("wrong palce , try again :")
        else :
            print("input range must be 1 to 2 , try again :")

    show()
    check_game()
    draw_check()
    if mode == 1 : 
        print("player 2")
        while True :
            row = int(input("row : "))
            col = int(input("col : "))
            if 0 <= row <= 2 and  0 <= col <= 2 :
                if game_board[row][col] == "-" :
                    game_board[row][col] = "[blue]O[/]"
                    break
                else :
                    print("wrong place , try again : ")
            else :
                print("input range must be 1 to 2 , try again :")                 
        show()
        check_game()
        draw_check()

    elif mode == 2 :
        print(" CPU ")
        while True :
            row = random.randint(0,2)
            col = random.randint(0,2)
            if game_board[row][col] == "-" :
                game_board[row][col] = "[blue]O[/]"
                break
            else :
                print("wrong place , try again : ")              
        show()
        check_game()
        draw_check()       
