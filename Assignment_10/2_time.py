
class Time :

    def __init__(self , h , m , s):

        self.hour = h
        self.minute = m
        self.second = s 


    
    def GMT_TO_CET(self,hour,minute,second):
        ...

    def CST_TO_GMT(self,hour,minute,second):
        ...

    def stopwatch(self ,hour,minute,second) :
        ... 
    
    def convert_day_to_sec(self , hour , minute , second) :
        ...

    def convert_sec_to_hour(self, hour , minute , second) :
        ...

    def countDown_Timer (self , hour , minute , second):
        ...


#current_time = Time( 15 , 22 , 30)
#print(current_time.hour , current_time.minute  , current_time.second)