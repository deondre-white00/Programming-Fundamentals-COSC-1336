#############################################################################################################################
#
#
#       Name: DeonDre White
#       Date: 3/28/2021
#
#
#       Program Description: this program with calculate the cost of tuition per semester over the next 5 years
#
#
#       Lab 4
#
#       Version: 1.0.0
#
############################################################################################################################

tuition = 8000
percentage_increase = .03
year = 2021

while (year <= 2025):
    tuition = tuition + (tuition * percentage_increase)
    print('In',year, 'the tuition per semester will be ' + '$' + format(tuition, ',.2f') + '.')
    year += 1
