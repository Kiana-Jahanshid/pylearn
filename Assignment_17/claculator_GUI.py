import sys
import PySide6
import math 
from PySide6.QtWidgets import QApplication , QMainWindow , QWidget
from PySide6.QtUiTools import QUiLoader


error = "ERROR"
global operand 

def my_multiply():
    global a , b ,c 
    global operand
    operand = '*'
    a = window.box.text()
    window.box.setText("")

def my_minus():
    global a , b ,c 
    global operand
    operand = str("-")
    a = window.box.text()
    window.box.setText("")

def my_sum():
    global a , b ,c
    global operand
    operand = "+"
    a = window.box.text()
    window.box.setText("")

def my_divide():
    global a , b ,c
    global operand
    operand = str("/")
    a = window.box.text()
    window.box.setText("")

def my_sin():
    global a 
    global operand
    operand = "sin"
    a = window.box.text()
    c = math.sin(int(a))
    window.box.setText(str(c))

def my_cos():
    global a 
    global operand
    operand = "cos"
    a = window.box.text()
    c = math.cos(int(a))
    window.box.setText(str(c))

def my_cot():
    global a 
    global operand
    operand = "cot"
    a = window.box.text()
    c = 1/(math.tan(int(a)))
    window.box.setText(str(c))

def my_sqrt():
    global a 
    global operand
    operand = "sqrt"
    a = window.box.text()
    c = math.sqrt(int(a))
    window.box.setText(str(c))

def my_tan():
    global a 
    global operand
    operand = "tan"
    a = window.box.text()
    c = math.tan(int(a))
    window.box.setText(str(c))

def my_log():
    global a 
    global operand
    operand = "log"
    a = window.box.text()
    c = math.log(int(a))
    window.box.setText(str(c))

def my_remain():
    global a , b 
    global operand
    operand = "%"
    a = window.box.text() 
    window.box.setText("")

def clear():
    window.box.setText("")


def result(c ):
        if operand == "-" :
            b = window.box.text()
            c = float(a) - float(b)
            window.box.setText(str(c))
        elif operand == "+" :
            b = window.box.text()
            c = float(a) + float(b)
            window.box.setText(str(c))
        elif operand == "*" :
            b = window.box.text()
            c = float(a) * float(b)
            window.box.setText(str(c))
        elif operand == "/" :
            b = window.box.text()
            c = float(a) / float(b)
            window.box.setText(str(c))            
        elif operand == "%" :
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
window = loader.load("mycalculator.ui")
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