age = input("how old are you?")
age = int(age)

if age >= 20:
    print("ok to ride")
else:
    print("no, too young")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print('sarah favorite language is ' + favorite_languages['sarah'].title() + '.')

