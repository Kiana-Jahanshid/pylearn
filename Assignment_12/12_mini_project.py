class Product :
    def __init__(self , code , name , price , count ):
        self.code = code 
        self.name = name 
        self.price = price 
        self.count = count 

    @staticmethod   
    def add():
        code = input("enter code : ")
        name = input("enter name : ")
        price = input("enter price :")
        count = input("enter count : ")
        new_product = Product( code , name , price , count )
        PRODUCTS.append(new_product)
    
    def edit(self):
        ...

    @staticmethod
    def search():
        ...

    def remove(self):
        ...

    def buy(self):
        ...

    @staticmethod
    def show_list(): #liste hame kala ha ro neshoon mide be ma 
        ...

    def show(self):
        ...



PRODUCTS = []

def read_from_db():
    file = open ("Assignment_12/database.txt" , "r")
    for line in file :
        result = line.split(",")
        #listi az obj ha
        my_object = Product(result[0] , result[1] , result[2] , result[3])
        PRODUCTS.append(my_object)        

    file.close()



def write_to_db():
    ...



def show_menu():
    print("1- Add product ")
    print("2-Edit ")
    print("3- Remove ")
    print("4- Search ")
    print("5- show list ")
    print("6- Buy ")
    print("7- Exit ")



print("Welcome to MoviePY STORE ")
print("data is loading ...")
read_from_db()
print(Product)

while True :

    show_menu()
    user_choice = int(input("Enter your choice :"))
    
    if user_choice == 1 :
        Product.add() #AVALIN BAR BAD AZ SEDA ZADANE ADD , PRODUCT SAKHTE MISHE 
    
    elif user_choice == 2 :
        code = int(input("enter product code : "))
        for obj in PRODUCTS :
            if obj.code == code :
                obj.edit()
                 
    elif user_choice == 3 :
        #obj darim ke mikaim removesh konim 
        code = int(input("enter product code : "))
        for obj in PRODUCTS : 
            if obj.code == code :                 
                obj.remove()

    elif user_choice == 4 : 
        #hadaf peyda kardane kalast , ama hanooz peydash nakarde ke , pas yek obj nemitoone in func ro ejra kone 
        #pas search ham mitoone yek static method bashe 
        #pas kole kelas product vazife dare search ro ejra kone 
        Product.search()


    elif user_choice == 5 :
        #liste hameye kala ha ro neshoonemoon mide 
        #pas in method dige nabayad ba yek kalalye khasi ejra beshe 
        #tavasote kelas bayad ejra beshe , pas statice
        Product.show_list()
    
    
    elif user_choice == 6 :
        #buy() #tavasote obj khas ejra mishe 
        ...
    
    elif user_choice == 7 :
        exit(0)
    else :
        print("Wrong choice , try again ... : ")
