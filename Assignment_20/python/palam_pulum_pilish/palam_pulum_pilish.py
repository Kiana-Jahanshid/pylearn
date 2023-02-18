import random
import sys
from PySide6.QtWidgets import QApplication , QMainWindow 
from ui_palam_pulum_pilish import Ui_MainWindow 
from functools import partial
  
class PalamPulumPilish(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)   
        
        self.front_hand = self.ui.front_btn
        self.back_hand = self.ui.back_btn
        self.win = self.ui.win_btn
        self.comp1_score = self.ui.com1_score
        self.comp2_score = self.ui.comp2_score
        self.player_score = self.ui.player_score_btn
        self.player_choice = self.ui.player_choice
        self.comp1_choice = self.ui.comp1_choice
        self.comp2_choice = self.ui.comp2_choice
        self.choice = ["🤚🏻" , "🖐🏻"]
        self.c1_counter = 0 
        self.c2_counter = 0
        self.player_counter = 0

        self.front_hand.clicked.connect(partial(self.play , "front"))
        self.back_hand.clicked.connect(partial(self.play , "back"))


    def play(self , input):
        global state_result
        state_result = input

        if state_result == "back" :
            self.player_choice.setText("🤚🏻")
        elif state_result == "front" :
            self.player_choice.setText("🖐🏻")

        comp1_result = self.choice[random.randint(0,1)]
        self.comp1_choice.setText(comp1_result)
        comp2_result = self.choice[random.randint(0,1)]
        self.comp2_choice.setText(comp2_result)

        if (state_result == "front" and comp1_result == self.choice[0] and comp2_result == self.choice[1]) or (state_result == "back" and comp1_result == self.choice[1] and comp2_result == self.choice[0]):
                self.player_counter += 1 
                self.c2_counter +=1
                self.player_score.setText("Player Score :" + str(self.player_counter))     
                self.comp2_score.setText("Computer2 Score :" + str(self.c2_counter))    
        elif   (state_result == "front" and comp1_result == self.choice[1] and comp2_result == self.choice[0]) or(state_result == "back" and comp1_result == self.choice[0] and comp2_result == self.choice[1]) :
                self.player_counter += 1 
                self.c1_counter +=1
                self.player_score.setText("Player Score :" + str(self.player_counter))     
                self.comp1_score.setText("Computer1 Score :" + str(self.c1_counter)) 
        elif   (state_result == "back" and comp1_result == self.choice[1] and comp2_result == self.choice[1] ) or (state_result == "front" and comp1_result == self.choice[0] and comp2_result == self.choice[0]):
                self.c2_counter += 1 
                self.c1_counter +=1
                self.comp2_score.setText("Computer2 Score :" + str(self.c2_counter))     
                self.comp1_score.setText("Computer1 Score :" + str(self.c1_counter)) 



        if self.player_counter== 5  :
            self.win.setText(" 💥🏆💥🏆💥 YOU Won 💥🏆💥🏆💥")
        elif self.c1_counter == 5 :
            self.win.setText("😎😎😎 Computer 1 Won 😎😎😎")
        elif self.c2_counter == 5 :
            self.win.setText("😝😝😝 Computer 2 Won 😝😝😝")
           

app = QApplication(sys.argv)
main_window = PalamPulumPilish()  
main_window.show()

app.exec()