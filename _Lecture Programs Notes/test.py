import math

n = 20

def test():
    for counter in range(3, int(math.sqrt(n))+1, 2):
      result = n%counter
      print("The index is: " + str(counter) + " the number is " + str(n)
        + " and the resulting modulus is: " + str(result))
      if n%counter == 0:
           return False
      return True
    verify()


def verify():
    if test == True:
        print('is not a prime number')
    else:
        print('is a prime number')



