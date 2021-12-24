import March11Chap5_Part2

def main():
    welcomeMsg = 'Welcome to metric conversion program.\n'
    print(welcomeMsg)
    displayMenu()
    menuSelection = input('\nPlease make a selection from the menu.\t')
    menuSelection = menuSelection.upper()

    while menuSelection != 'X':
        if menuSelection == 'K':
            March11Chap5_Part2.convertMilesToKilometers()
        elif menuSelection == 'M':
            March11Chap5_Part2.convertKilometersToMiles()
        else:
            print('You selected an invalid menu option.')
        displayMenu()
        menuSelection = input('\nPlease make a selection from the menu.\t')
        menuSelection = menuSelection.upper()

    print('Good bye. Thank you.')
    exit()

def displayMenu():
    print('Select K to convert miles to kilometers.')
    print('Select M to convert kilometers to miles.')
    print('Select X to exit the program.')




main()

    
