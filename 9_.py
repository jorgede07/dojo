#no sabia a que te referias con todos los numeros así que he puesto un input y que sustitulla solo el numero del input


number = float(input ("select a number: "))
number_3 = number % 3
number_5 = number % 5
if number_3 == 0:
    if number_5 ==0:
        print("Fizzbuzz")
 
    
else:
    if number_3 == 0 :
        print ("Fizz")
    
    if number_5 == 0:
        print ("Buzz")

    if number_3 and number_5 != 0 :
        print (number)
    

    
    




    


