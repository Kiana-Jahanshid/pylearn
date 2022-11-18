time = input("enter your time in this format (h:m:s):\n")

string = time.split(":")
print(string)
hour , minutes , sec = string 
hour =int(hour)
minutes = int(minutes)
sec = int(sec)
seconds  = hour*3600 + minutes*60 + sec
print(seconds)
