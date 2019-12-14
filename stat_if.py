name = "Alice"

if name == 'Alice':
	print('Hi, Alice.')
elif age < 12:
	print('You are not Alice, kiddo.')
elif age > 2000:
	print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
	print('You are not Alice, grannie.')


while True:
    print('enter your name:')
    name = input()
    if name == 'your name':
        break
print('thanks')

while True:
	print('Who are you?')
	name = input()
	if name != 'Joe':
		continue
	print('Hello, Joe. What is the password? (It is a fish.)')
	password = input()
	if password == 'swordfish':
		break
print('Access granted.')

print('my name is ')
for i in range(5):
    print('jim five times (' + str(i) + ')')

    
