import qrcode 

name = input("\nEnter your name :")
phone = input("Enter your phone number :")

img = qrcode.make( "name : " + name +"\n"+ "phone number :" + phone)
img.save("qrcode.png")
