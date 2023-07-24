from itertools import count
from unittest.util import _count_diff_all_purpose


year = float(input("select a year: ")) 
year_calc = year
year_calc %= 4

def leap_years(year) :
    count_years = 0
    while count_years <4 :
        year += 4
        print (year)
        count_years += 1


if year_calc == 0 :
    leap_years(year)

else :
    while year_calc != 0 :
       year -= 1
       year_calc = year 
       year_calc %= 4
    leap_years(year)
   

