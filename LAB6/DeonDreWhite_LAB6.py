#############################################################################################################################
#
#
#       Name: DeonDre White
#       Date: 4/18/2021
#
#
#       Program Description: Write a program that asks the user for a
#       filename and reads the numbers from the file
#       and then calculates the average of all the numbers stored in the file.
#
#       Lab 6
#
#       Version: 1.0.0
#
################################################################################
d = 0
count = 0


def openPro():
    try:
        fileName = input('Enter the name and ext of the file you want to read: ')
        f = open(fileName,'r')
        for x in f:
            convertInt = int(x)
            global d
            global count
            d = d + convertInt
            count += 1
        avg = d/count
        print(avg)
    except IOError:
        print("Trouble opening file. Try again.")
    except ValueError:
        print('File must have only numbers. Try again.')

openPro()
