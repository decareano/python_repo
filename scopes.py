# scopes.py

# Scope A
a = 1
b = 16
c = 'abc'

def outer():
    # Scope B
    c = 24
    d = 'Hello, World!'
    print(c)
    def inner():
        # Scope C
        e = 'I like'
        f = 'fried chicken'
    print(e)
    return(e)
# (Implicit) Scope D
print('Hello!')

