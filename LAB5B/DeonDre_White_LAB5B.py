#############################################################################################################################
#
#
#       Name: DeonDre White
#       Date: 3/28/2021
#
#
#       Program Description: Design and implement an application to convert temperatures from Fahrenheit to Celsius or Celsius to Fahrenheit.
#       Create a menu based application with 3 options, Convert Fahrenheit to Celsius, Convert Celsius to Fahrenheit,
#       and Exit.  You'll need a conditional loop and a sentinel value, (For Example: X to Exit).
#
#
#       Lab 5B
#
#       Version: 1.0.0
#
################################################################################



def lab5b():
        print('To convert Celsius to Fahrenheit enter 1')
        print('To convert Fahrenheit to Celsius enter 2')
        print('To end the program enter 3')
        try:
            choice = int(input('Enter your choice: '))
            options(choice)
        except:
            print('Invalid entry. The options are 1, 2 or 3. Try \n')
            lab5b()
            
       
         
        
def options(choice):
        while(choice != 3):
            if(choice == 1):
                temp = int(input('Enter tempeture: '))
                celToFahr(temp)
            elif(choice == 2):
                temp = int(input('Enter tempeture: '))
                fahrToCel(temp)
            elif(choice == 3):
                exit()
            else:
                print('Invalid entry. The options are 1, 2 or 3. Try again\n')
                print()
                lab5b()
            choice = int(input('Ente r your choice: '))
                
        
         


def celToFahr(temp):
    fahr = float(temp * 1.8 +32)
    print('The temp is:', fahr)
    print()

def fahrToCel(temp):
    cel = float((temp - 32) * 5/9)
    print('The tmep is:', cel)
    print()

lab5b()
