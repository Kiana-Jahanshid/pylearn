class Fraction :
    
    def __init__(self, numerator , denominator):
        self.operand_1 = numerator 
        self.operand_2 = denominator 
        self.operator ="/"


    def divison(self , operand_1 , operand_2) : 
        ...

    def fraction_simplify(self , operand_1 , operand_2):
        ...

    def reverse_number(self , operand_2) :
        ...

    def makhraj_moshtarak(self , operand_1 , operand_2):
        ...
    
    def fr_multiply(self , operand_1 , operand_2):
        ...

    def fr_add(self , operand_1 , operand_2):
        ...

    def show(self):
         print(self.operand_1, self.operator ,self.operand_2)


fr = Fraction(7,8)
fr.show()