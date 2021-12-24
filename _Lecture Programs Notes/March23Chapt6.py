filePath = 'C:\\Users\\PersonalWork\\Documents\\ACC\\2021 Spring\\Programming Fundamentals COSC-1336\\_Lecture Programs Notes\\'
fileName = 'numbers.txt'
fileName2 = 'numberOut.txt'

##create file object
inputFile = open(filePath + fileName, 'r')
outFile = open(filePath + fileName2, 'w')


##process file 
num1 = inputFile.readlines()

print(num1)##string value

outFile.write(num1)

##close the file
inputFile.close()
outFile.close()

# read and write to files
#try exception
#exceptions
