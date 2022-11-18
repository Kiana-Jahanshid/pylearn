sec = int(input("enter time input (in seconds) :"))

if sec >= 86400 :
    print("\n<< time value has exceeded from day limit ! >>")
else :    
    dayseconds = 3600 * 24 
    sec = sec % dayseconds 
    hour = int(sec / 3600 )
    sec = sec % 3600
    minutes = int(sec / 60  )
    sec = sec % 60 
    minutes = format(minutes , '02')
    sec =format(sec , '02')

    print( hour ,":", minutes ,":", sec  )
