class Fraction :
    
    def __init__(self, numerator , denominator):
        self.num = numerator 
        self.denom = denominator 
        self.operator ="/"



    def sum(self ,frac2 ) : 
        num_res = self.num * frac2.denom + self.denom * frac2.num
        denom_res = self.denom * frac2.denom
        answer = Fraction(num_res , denom_res)
        return answer


    def mul(self  , frac1 ):
        result_num = frac1.num * frac2.num
        result_denom = frac1.denom * frac2.denom
        answer = Fraction(result_num , result_denom)
        return answer 


    def sub(self , frac1) :
        num_res = self.num * frac2.denom + self.denom * frac2.num
        denom_res = self.denom * frac2.denom
        answer = Fraction(num_res , denom_res)
        return answer


    def division(self , frac2):
        div_soorat =  frac1.num * frac2.denom 
        div_makhraj = frac1.denom * frac2.num 
        answer = Fraction(div_soorat , div_makhraj )
        return answer


    def fraction_to_number(self):
        
        number = self.num / self.denom 
        #number = Fraction(number , 1)
        return number 


    def bmm(self ):
        if self.num > self.denom : 
            n = self.denom
        else: 
            n = self.num 
        for i in range(1, n+1): 
            if((self.num % i == 0) and (self.denom % i == 0)): 
                    bmm = i  

        return bmm 


    def simplify(self ):

        BMM = Fraction.bmm(self)
        simplified_soorat= int(self.num / BMM )
        simplified_makhraj = int(self.denom / BMM )
        simplified_fraction = Fraction(simplified_soorat , simplified_makhraj)
        return simplified_fraction 


    def show(self):

         print(self.num, self.operator ,self.denom)


frac1 = Fraction(2,3)
print('first fraction :' )
frac1.show()

frac2 = Fraction(7,5)
print('second fraction :')
frac2.show()

frac3 = Fraction(18,12)
print('third fraction :')
frac3.show()

fr_sub = frac2.sub(frac1)
print('subtraction :')
fr_sub.show()

multiply =  frac2.mul(frac1 )
print('multiply : ')
multiply.show()

#f_sum = frac1.sum(frac1 , frac2)
f_sum = frac1.sum( frac2 )
print('sum')
f_sum.show()

fr_div = frac1.division(frac2)
print('division')
fr_div.show()
#number.show()

print ("fraction to number :\n" , frac2.fraction_to_number())


f_simplify = frac3.simplify()
print('simplify :')
f_simplify.show()