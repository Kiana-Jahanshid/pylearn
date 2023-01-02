class Complex :
    def __init__(self , real , image):
        self.real = real 
        self.image = image 

    def show(self):
        print(self.real , "+" , "i" , self.image)

    def sum(self , second_number):
        real_part = first_number.real + second_number.real 
        image_part = first_number.image + second_number.image
        return Complex(real_part , image_part)

    def multiply(self , first_number):
        real_part_of_answer = (first_number.real * second_number.real)-(second_number.image * first_number.image)
        image_part_of_answer = (first_number.real * second_number.image)+(first_number.image * second_number.real)
        return Complex(real_part_of_answer , image_part_of_answer)


    def sub(self , second_number) :
        real_part = (first_number.real - second_number.real)
        image_part = (first_number.image - second_number.image)
        return Complex(real_part , image_part)


first_number = Complex(5,8)
second_number = Complex(9,4)

print("\nFirst complex number : ", end="")
first_number.show()
print("Second complex number : ", end="")
second_number.show()
#add two numbers
print("\nSum of two complex numbers : ", end="")
add = first_number.sum(second_number)
add.show()

#multiply two numbers
print("\nMultiply of two complex numbers : ", end="")
mul = second_number.multiply(first_number)
mul.show()

#subtraction 
print("\nSubtraction of two complex numbers : ", end="")
subtraction = first_number.sub(second_number)
subtraction.show()