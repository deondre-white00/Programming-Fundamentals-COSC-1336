#############################################################################################################################
#
#
#       Name: DeonDre White
#       Date: 2/28/2021
#
#
#       Program Description: program that mixes primary colors together to get
#                               secondary colors
#
#
#       Lab 3
#
#       Version: 1.0.0
#
############################################################################################################################
#module import
import time


#inputs/decision tree
print('The primary colors are Red, Blue and Yellow')

color_one = input('enter you first primary color:\n')
color_one = color_one.lower()
if color_one == 'red' or color_one == 'blue' or color_one == 'yellow':
    print('You entered ' + color_one)
else:
    print('You did not enter a valid option')
    time.sleep(3)
    exit()

color_two = input('enter you second primary color.\n')
color_two = color_two.lower()
if color_two == 'red' or color_two == 'blue' or color_two == 'yellow':
    print('You entered ' + color_two)
else:
    print('You did not enter a valid option')
    time.sleep(3)
    exit()


#color mixing instructions
if color_one == 'red':
    if color_two == 'blue':
        print(color_one + ' mixes with ' + color_two + ' makes purple.')

        
if color_one == 'red':
    if color_two == 'yellow':
        print(color_one + ' mixes with ' + color_two + ' makes orange.')

        
if color_one == 'blue':
    if color_two == 'yellow':
        print(color_one + ' mixes with ' + color_two + ' makes green.')
        
        
if color_one == 'blue':
    if color_two == 'red':
        print(color_one + ' mixes with ' + color_two + ' makes purple.')

        
if color_one == 'yellow':
    if color_two == 'red':
        print(color_one + ' mixes with ' + color_two + ' makes orange.')

        
if color_one == 'yellow':
    if color_two == 'blue':
        print(color_one + ' mixes with ' + color_two + ' makes green.')

