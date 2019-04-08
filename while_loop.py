#number = 2
#ab = input("Give me a number: ")
#while number < 10:
#   if number%2 == 0:
#      print("The number "+ str(number)+" is even")
#   else:
#      print("The number is"+ str(number)+" is odd")
#   number = number+1

def collatz(number):
   if number%2 == 0:
      print(number / 2)
      #return number / 2
   elif number%2 == 1:
      test_result = 3 * number + 1
      print(test_result)
      #return test_result

n = input("Give me a number: ")

while n != 1:
   n = collatz(int(n))   
