import qrcode
PRODUCTS = []

def read_from_database():
    global f 
    f =open("Assignment_7\database.txt" , "r")
    for line in f :
        line = line.rstrip()
        result = line.split(",")
        my_dict = {"code" : result[0] ,"name" : result[1] ,"price": result[2] ,"count" : result[3] }
        PRODUCTS.append(my_dict)  
         
    f.close()

def space_remover():
     f =open("Assignment_7\database.txt" , "r")
     for line in f :
        line = line.rstrip()
        result = line.split(",")
        my_dict = {"code" : result[0] ,"name" : result[1] ,"price": result[2] ,"count" : result[3] }         
        new_dict = {
             key.replace(' ', ''): value for key, value in my_dict.items()
        }
        PRODUCTS.append(new_dict)


def write_to_database():
    open("Assignment_7\database.txt" , "w").close()
    file = open("Assignment_7\database.txt" , "a")
    # with open ("Assignment_7\database.txt" , "r+") as file :
    #     file.truncate(0)
    # file  = open("Assignment_7\database.txt" , "w")
    for product in PRODUCTS :
        file.write( f"{product['code']},{product['name']},{product['price']},{product['count']}\n")        
    file.close()


def show_menu():
     print("1_add ") 
     print("2_edit ")
     print("3_remove ")
     print("4_search ")
     print("5_show list ")   
     print("6_buy ")
     print("7_make qrcode")
     print("8_exit ")


def add():
     code = input("enter code :") 
     name = input("enter name :")
     price = input("enter price :") 
     count = input("enter count :")
     new_product={"code":code,"name":name,"price":price,"count":count}
     PRODUCTS.append(new_product)



def edit():
     product_code = input("enter your product's code :")
     for product in PRODUCTS :
         if product["code"] == product_code :
             print(product["code"] , "\t" , product["name"] , "\t" , product["price"] , "\t" , product["count"])     
     print("which field of product do you want to edit ? ")
     print("name") 
     print("price")
     print("count")
     product_field = input("enter field's name :")
     for product in PRODUCTS :
         if product["code"] == product_code :
             if product_field == "name" :
                     product["name"] = input("enter new name :")
             elif  product_field == "price" :  
                     product["price"] = input("enter new price :")
             elif  product_field == "count" :     
                     product["count"] = input("enter new count :")

             print(product["code"] , "\t" , product["name"] , "\t" , product["price"] , "\t" , product["count"])
             print("\n data has been updated successfully ")
    



def remove():
    user_input = input("enter your product code you want to delete : ") 
    index_count = 1 
    for product in PRODUCTS :
        if product["code"] == user_input :
             deleteLine = index_count
             break
        else :
             index_count +=1    

    File = "Assignment_7\database.txt"
    with open(File, 'r') as filedata:
        inputFilelines = filedata.readlines()
        lineindex = 1
        with open(File, 'w') as filedata:
            for textline in inputFilelines:
                if lineindex != deleteLine:
                    filedata.write(textline)
                lineindex += 1
    print("Line",deleteLine,'is deleted successfully\n')
    print("File Content After Deletion :")
    givenFile = open(File,"r")
    for line in givenFile:
        print(line)
        line = line.rstrip()   
    space_remover()
    filedata.close()




def search():
     user_input = input("type your keyword :")
     for product in PRODUCTS :
         if product["code"] == user_input  or product["name"] == user_input :
             print(product["code"] , "\t" , product["name"] , "\t" , product["price"])
             break 
     else :
         print("not found ")


def show_list():
     print("code\t name\t\tprice\t  count")
     for product in PRODUCTS :
         print(product["code"] , "\t" , product["name"] , "\t" , product["price"], "\t" , product["count"])   


def buy():
     read_from_database()
     shopping_cart = [] 
     total_price = 0
     while True :
        product_code = input("enter new product code : ")
        for product in PRODUCTS :
            if product["code"] == str(product_code) :
                user_count = int(input('how many ' + product["name"] + ' do you want to buy ? '))
                if int(product["count"]) < user_count :
                    print("xxxx Not Enough Quantity xxxx")
                    break
                elif  int(product["count"]) >= user_count :
                    product["count"] = int(product["count"]) - user_count
                    user_product = {"product_code" : product["code"] , "product_name" : product["name"] , "product_price" : product["price"] , "product_count" : user_count}
                    shopping_cart.append(user_product)
                    print("product added to your shopping cart.")
                    total_price += int(product["price"]) * user_count

                    choice = input("do you want to 'continue' shopping ? or 'quit' ? enter your choice : ")
                    if choice == "continue" :
                         break 
                    elif choice == "quit" :
                         print("code \t name \t price \t count ")
                         for user_product in shopping_cart :
                             print(str(user_product["product_code"])  + "\t" + user_product["product_name"] + "\t" + str(user_product["product_price"]) + "\t" + str(user_product["product_count"]) )
                         print("TOTAL PRICE : " , total_price)
                         exit()

        else :
            print ("product not found")
            break




def make_qrcode() :
     print("choose a code from below list :")
     show_list()
     code = str(input("\nEnter product's code number to create qrcode :"))
     for product in PRODUCTS :
         if code == product["code"] :
             product_info =("code=" + product["code"] +" \t "+ "name=" + product["name"] +" \t "+"price=" + product["price"] +" \t "+ "count=" + product["count"])
             print(product_info)
             img = qrcode.make(product_info)
             img.save("product_qrcode.png")



print("welcome to my store ")
print("loading . . . ")
read_from_database()
print("data loaded.")

while True :
    show_menu()
    choice = int(input("enter your choice :"))

    if choice == 1 :
        add()
    elif choice == 2 :
        edit()     
    elif choice == 3 :
        remove()
    elif choice == 4 :
        search()
    elif choice == 5 :
        show_list()
    elif choice == 6 :
        buy()
    elif choice == 7 :
        make_qrcode()    
    elif choice == 8 :
        write_to_database()
        exit(0)
    else :
        print("choose again :")     

