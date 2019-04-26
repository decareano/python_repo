animals = [
    {'type': 'penguin', 'name': 'step', 'age': 8},
    {'type': 'elephant', 'name': 'devon', 'age': 3},
    {'type': 'puma', 'name': 'moe', 'age': 5},
]

def a_sortin_problem(animals):
    print(animals)


a_sortin_problem(sorted(animals, key=lambda animal: animal['age']))
