
class Time :

    def __init__(self , h , m , s):

        self.hour = h
        self.minute = m
        self.second = s 
        self.fix()
        self.time = 12345


    def sum_times(self , other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour 

        result = Time(h_new , m_new  , s_new)
        return result 


    def sub_times(self , other) :
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour 
        result = Time(h_new , m_new  , s_new)
        return result 


    def second_to_time(self ):
        hour =self.second // 3600
        minute =(self.second %3600) // 60 +1
        second =(self.second %3600) % 60
        return Time(hour , minute , second)


    def time_to_second (self ) :
        
        hour = self.hour 
        minute  = self.minute 
        second  = self.second
        seconds = hour * 3600 + minute * 60 + second
        return Time(0,0,seconds)



    def GMT_to_tehran(self) :
        tehran_h = self.hour + 3
        tehran_m = self.minute + 30 
        tehran_s = self.second 
        return Time(tehran_h , tehran_m , tehran_s )



    def fix(self):
        if self.second >= 60 :
            self.second -= 60
            self.minute += 1 

        if self.minute >= 60 :       
            self.minute -= 60 
            self.hour += 1

        if self.second < 0 : 
            self.second += 60 
            self.minute -= 1

        if self.minute < 0 :
            self.minute += 60
            self.hour -= 1



    def show(self ):
 
        #print(self.hour , ":" , self.minute , ":" , self.second)
        print('{:d}:{:02d}:{:02d}'.format(self.hour , self.minute, self.second))
       
    def shownum(self):
        print(self.second)


print("first time :")
time1 = Time(3,75,17)
time1.show()

print("second time :")
time2 = Time(4,90,2)
time2.show()

print("sum of two times :")
time3 = time1.sum_times(time2)
time3.show()

print("subtraction of two times :")
time5 = time3.sub_times(time2)
time5.show() 

print("converted second to time :")
time4 = Time(0,0,4521)
time4 = time4.second_to_time()
time4.show()

print("converted time to second :")
time6 = time1.time_to_second()
time6.shownum()

print("converted GMT TO tehran time :")
time7 = time1.GMT_to_tehran()
time7.show()