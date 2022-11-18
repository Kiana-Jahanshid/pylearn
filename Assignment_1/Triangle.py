print("Enter First Side Of Triangle :")
a = float(input())
print("Enter Second Side Of Triangle :")
b = float(input())
print("Enter Third Side Of Triangle :")
c = float(input())

if (a<=0 or b<=0 or c<= 0 ):
    print("<<< ERROR : It CAN NOT be a triangle >>>")  
else :     
    if (a<b+c and b<a+c and c<a+b ):
        print("<<< It's a possible triangle >>>")

    else:  
        print("<<< It's NOT a possible triangle >>>")

