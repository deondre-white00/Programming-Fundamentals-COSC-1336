
def calcSum(num1, num2):
    result1 = num1 + num2
    result2 = num1 * num2
    result3 = num1 / num2
    print (result1, result2, result3)

def main():
    firstNum = int(input("enter first num"))
    secondNum = int(input("enter second num"))
    calcSum(firstNum, secondNum)
    #print(result1, result2, result3)

main()

################# option two###################################

def calcSum2(num3, num4):
    result4 = num3 + num4
    result5 = num3 * num4
    result6 = num3 / num4
    return (result4, result5, result6)

def main2():
    firNum = int(input("enter first num"))
    secNum = int(input("enter second num"))
    firstresult, secondresult, thirdresult = calcSum2(firNum, secNum)
    print(firstresult, secondresult, thirdresult)

main2()
