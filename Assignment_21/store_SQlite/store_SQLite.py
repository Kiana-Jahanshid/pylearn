import qrcode
import sqlite3


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
     code = input("enter product code :") 
     name = input("enter product name :")
     price = input("enter product price :") 
     count = input("enter product count :")

     con.execute(f"INSERT INTO STORE (ID,name,price,count) VALUES({code} , '{name}' , {price} , {count})")
     con.commit()



def edit():
    id = int(input("enter your product'd ID , to start editting :"))
    field = str(input("which filed of prooduct do you want to edit (ID ? name ? price or count ?): "))

    if field =="ID":
        new_id = int(input("enter new product's id : "))
        con.execute(f"UPDATE store set {field}={new_id} WHERE ID = {id}")
        con.commit()        
    elif field =="name":
        new_name = str(input("enter new product's name : "))
        con.execute(f"UPDATE store set {field}='{new_name}' WHERE ID = {id}")
        con.commit() 
    elif field =="price" :
        new_price = int(input("enter new product's price : "))
        con.execute(f"UPDATE store set {field}={new_price} WHERE ID = {id}")
        con.commit() 
    elif field =="count" :
        new_count = int(input("enter new product's count : "))
        con.execute(f"UPDATE store set {field}={new_count} WHERE ID = {id}")
        con.commit() 



def remove():
    user_input = input("enter your product's ID you want to delete : ") 
    con.execute(f"DELETE from store where ID = {user_input}")
    con.commit()
    print("Remain products ar :")
    show_list()



def search():
    choice = str(input("which field do you want to search based on ? write your choice (ID or name) : "))
    if choice=="ID" :
        id = int(input("enter product ID :"))
        for row in curs.execute(f"SELECT * FROM store WHERE ID={id}"):
            print (row)
    elif choice == 'name' :
        name = int(input("enter product name :"))
        for row in curs.execute(f"SELECT * FROM store WHERE name={name}"):
            print (row)



def show_list():
    print("\n(code , name , price , count)")
    for row in curs.execute("SELECT * FROM store"):
        print(row)
    print("")



def buy():
    user_product = str(input("Enter your product's name you wana buy : "))
    user_count = int(input("how many of this product you wana buy ? "))
    for row in curs.execute(f"SELECT count FROM store WHERE name='{user_product}'").fetchall():
        count = (row[0])
    remain = int(count) - user_count
    if remain >= 0 :
        con.execute(f"UPDATE store set count={remain} WHERE name = '{user_product}'")
        con.commit() 
    elif remain < 0 :
        print("❌❌ NOT enough quantity to buy this product ❌❌")


def make_qrcode() :
    id = int(input("\nEnter product's ID to create qrcode form it :"))
    selected_product = curs.execute(f"SELECT * FROM store WHERE ID={id} ").fetchall()
    img = qrcode.make(selected_product)
    img.save("product_qrcode.png")



print("welcome to my store ")
global con
global curs
con = sqlite3.connect("store.db")
curs = con.cursor()

while True :
    show_menu()
    choice = int(input("Enter your choice :"))

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
        con.close()
        exit(0)
    else :
        print("choose again :")     
