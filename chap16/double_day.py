"""
Tenzin Choetso
Chapter 16 Exercise 16.7
"""

from datetime import datetime 

def day_today():
    dict_days = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    week = datetime.weekday(datetime.today())
    day = dict_days[week]
    return day

def time_birthday (birthday):
    date_today = datetime.today()
    birthday2 = datetime (date_today.year,birthday.month,birthday.day)
    if date_today >= birthday2:
       birthday2 = datetime (date_today.year+1, birthday.month, birthday.day)
       age = date_today.year- birthday.year
       till_birthday = birthday2 - date_today
       print 'Age:', age 
       print 'time till birthday', till_birthday

def double_day(birthday1, birthday2):
    delta = abs(birthday1 - birthday2)
    if birthday1 > birthday2:
        double_day = birthday1 + delta
    elif birthday2 > birthday1:
        double_day = birthday2 + delta 
    return datetime.date(double_day)

if __name__=="__main__":
    time_birthday(datetime(1993,9,20))
    print day_today()
    print double_day(datetime(2006,12,26),datetime(2003,10,11))




