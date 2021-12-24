#############################################################################################################################
#
#
#       Name: DeonDre White
#       Date: 3/28/2021
#
#
#       Program Description: list numbers in a range and describe prime or not prime
#
#
#       Lab 5
#
#       Version: 1.0.0
#
################################################################################
import math
num1 = int(input('Enter start number: '))
num2 = int(input('Enter end number: '))
num3 = int(input('Enter a step value: '))

def is_prime(num1):
    for i in range(num1,  int(math.sqrt(num2))+1, num3):
        if(num2 % i) == 0:
            print(i, 'is not a prime number')
        else:
            print(i, 'is a prime number')
        ##verify(i)
        ##if verify == True:
            ##print(i, 'is not a prime number')
        ##elif verify == False:
            ##print(i, 'is a prime number')

       




        
    



is_prime(num1)

    


