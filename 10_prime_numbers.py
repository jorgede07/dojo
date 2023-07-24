
number = 1

number_calc_2 =  number

#aquí tambien ponía lo de todos así que lo he limitado hasta el 10k

while number <10000 :

    number_calc_2 =  number

    if number == 1:
        number_calc = 2
        number = 2
        print (1)
    
        number_calc = number-1
    

    number_calc_2 %= number_calc

    number_calc -= 1

    

    if number_calc_2 ==0 :
        number += 1
        number_calc = number-1
        

    

    if number_calc == 1 :

        print (number)
        number += 1
        number_calc = number-1
        


    


    





    


    

