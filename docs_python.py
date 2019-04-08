x = int(input("enter number"))

if x < 0:
        x = 0
        print("negative to zero change: ")
elif x == 0:
        print('zero')
    

words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word, len(word))

   
numbers = [45, 22, 14, 65, 97, 72]

#for i in range(len(numbers)):
#    if numbers[i]%3 == 0 and numbers[i]%5 == 0:
#        numbers[i] = 'fizzbuzz'
#    elif numbers[i]%3 == 0:
#        numbers[i] = 'fizz'
#    elif numbers[i]%5 == 0:
#        numbers[i] = 'buzz'



for i, num in enumerate(numbers):
    if num%3 == 0 and num%5 == 0:
        #import pdb; pdb.set_trace()
        numbers[i] = 'fizzbuzz'
    elif num%3 == 0:
        numbers[i] = 'fizz'
        print(num)
    elif num%5 == 0:
        numbers[i] = 'buzz'
#        print(num)

numbers1 = [4,2,6,8,9]
def square(x):
    return x*x



