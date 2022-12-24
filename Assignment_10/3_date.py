class Date :
    
    def __init__(self , d , m , y):

        self.day = d
        self.month = m
        self.year = y 


    def convert_jalali_to_Gregorian(self, year , month , day):
        ...

    def convert_lunar_to_solar(self , year , month , day) :
        ... 
    
    def convert_solar_to_lunar(self , year , month , day) :
        ...

    def age_calc(self , year , month , day) :
        ...

    def convert_Gregorian_to_Hijri(self ,year , month , day):
        ...

    def calendar(self ,year , month , day):
        ...