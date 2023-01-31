import sys
import math 
import PySide6
from PySide6.QtWidgets import QApplication 
from PySide6.QtUiTools import QUiLoader


def my_multiply():
    global a , b ,c 
    global operator
    operator = '*'
    a = window.box.text()
    window.box.setText("")

def my_minus():
    global a , b ,c 
    global operator
    operator = str("-")
    a = window.box.text()
    window.box.setText("")

def my_sum():
    global a , b ,c
    global operator
    operator = "+"
    a = window.box.text()
    window.box.setText("")

def my_divide():
    global a , b ,c
    global operator
    operator = str("/")
    a = window.box.text()
    window.box.setText("")

def my_sin():
    global a  , c
    global operator
    operator = "sin"
    a = window.box.text()
    c = math.sin(int(a))
    window.box.setText(str(c))

def my_cos():
    global a ,c
    global operator
    operator = "cos"
    a = window.box.text()
    c = math.cos(int(a))
    window.box.setText(str(c))

def my_cot():
    global a , c
    global operator
    operator = "cot"
    a = window.box.text()
    c = 1/(math.tan(int(a)))
    window.box.setText(str(c))

def my_sqrt():
    global a , c
    global operator
    operator = "sqrt"
    a = window.box.text()
    c = math.sqrt(int(a))
    window.box.setText(str(c))

def my_tan():
    global a , c
    global operator
    operator = "tan"
    a = window.box.text()
    c = math.tan(int(a))
    window.box.setText(str(c))

def my_log():
    global a , c
    global operator
    operator = "log"
    a = window.box.text()
    c = math.log(int(a))
    window.box.setText(str(c))

def my_remain():
    global a , b 
    global operator
    operator = "%"
    a = window.box.text() 
    window.box.setText("")

def clear():
    window.box.setText("")


def result(c ):
        if operator == "-" :
            b = window.box.text()
            c = float(a) - float(b)
            window.box.setText(str(c))
        elif operator == "+" :
            b = window.box.text()
            c = float(a) + float(b)
            window.box.setText(str(c))
        elif operator == "*" :
            b = window.box.text()
            c = float(a) * float(b)
            window.box.setText(str(c))
        elif operator == "/" :
            b = window.box.text()
            if b == 0 :
                window.box.setText("ERROR")            
            elif b != 0 :
                c = float(a) / float(b)
                window.box.setText(str(c))            
        elif operator == "%" :
            b = window.box.text()
            c = float(a) % float(b)
            window.box.setText(str(c))



def one():
    num = window.box.text()  
    window.box.setText(num +"1")
def two():
    num = window.box.text()  
    window.box.setText(num +"2")
def three():
    num = window.box.text()  
    window.box.setText(num +"3")    
def four():
    num = window.box.text()  
    window.box.setText(num +"4") 
def five():
    num = window.box.text()  
    window.box.setText(num +"5") 
def six():
    num = window.box.text()  
    window.box.setText(num +"6") 
def seven():
    num = window.box.text()  
    window.box.setText(num +"7") 
def eight():
    num = window.box.text()  
    window.box.setText(num +"8") 
def nine():
    num = window.box.text()  
    window.box.setText(num +"9") 
def zero():
    num = window.box.text()  
    window.box.setText(num +"0") 
def dot():
    num = window.box.text()  
    window.box.setText(num +".") 


#define an app
myapp = QApplication([])

loader = QUiLoader()
window = loader.load("Assignment_17\mycalculator.ui")
window.show()


window.multiply.clicked.connect(my_multiply)
window.sum.clicked.connect(my_sum)
window.minus.clicked.connect(my_minus)
window.divide.clicked.connect(my_divide)
window.remainder.clicked.connect(my_remain)
window.sin.clicked.connect(my_sin)
window.cos.clicked.connect(my_cos)
window.cot.clicked.connect(my_cot)
window.tan.clicked.connect(my_tan)
window.log.clicked.connect(my_log)
window.sqrt.clicked.connect(my_sqrt)
window.clear.clicked.connect(clear)
window.result.clicked.connect(result)
window.one.clicked.connect(one)
window.two.clicked.connect(two)
window.three.clicked.connect(three)
window.four.clicked.connect(four)
window.five.clicked.connect(five)
window.six.clicked.connect(six)
window.seven.clicked.connect(seven)
window.eight.clicked.connect(eight)
window.nine.clicked.connect(nine)
window.zero.clicked.connect(zero)
window.dot.clicked.connect(dot)


#for keeping window open 
myapp.exec()