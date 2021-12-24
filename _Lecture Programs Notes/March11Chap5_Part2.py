def convertMilesToKilometers():
    print('You chose to convert Miles to Kilometers.')
    miles = float(input('Enter the value for miles to convert to kilometers.'))
    kilometers = miles * MILES_TO_KILOMETER_CONV
    print ('There are', miles, 'miles in', kilometers, 'kilometers.')

def convertKilometersToMiles():
    kilometers = float(input('Enter the values for kilometers to convert to miles.'))
    miles = kilometers * KILOMETER_TO_MILE_CONV
    print ('There are',kilometers,'kilometers in',miles,'miles>')

MILES_TO_KILOMETER_CONV = 1.609344
KILOMETER_TO_MILE_CONV = 0.621371
