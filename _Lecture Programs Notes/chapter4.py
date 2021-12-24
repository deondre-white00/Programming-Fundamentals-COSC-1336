### While Loop ###

# Python program to illustrate  
# while loop  
count = 0
while (count < 3):      
    count = count + 1
    print("Hello Geek")  
  
print()

answer = 'Y'
while (answer == 'Y'):
    answer = input('Would you like more cake: "Y" or "N" ').upper()
    




### For Loop ###

startNum = int(input('Please enter the starting value in the range. '))
endNum = int(input ('Please enter the ending limit for the range. '))
stepVal = int(input('Please enter a step value for the range. '))

for num in range(startNum, endNum, stepVal):
    print('The number for this iteration is',num)


###  ###
grades = [92, 85, 100, 90]
total = 0

for num in grades:
    total = total + num
    print('The grade is', num)

average = total / 4
print('The test average is', average)



graded = [92, 85, 100, 90, 80, 88, 90, 88, 75, 74, 76, 92]

for nums in range():
    print('The grade is', nums)
