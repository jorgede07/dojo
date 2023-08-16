from random import shuffle

DOMINGUEZ_EDO = 0
RODRIGUEZ_DOMINGUEZ = 1
DOMINGUEZ_OLIVER = 2

todos = [
    ['Javi', DOMINGUEZ_EDO], 
    ['Carmen', DOMINGUEZ_EDO],
    ['Sergio', DOMINGUEZ_EDO],
    ['Jorge', DOMINGUEZ_EDO],
    ['Pepe', RODRIGUEZ_DOMINGUEZ],
    ['Concha', RODRIGUEZ_DOMINGUEZ],
    ['Pep', RODRIGUEZ_DOMINGUEZ],
    ['Javier', RODRIGUEZ_DOMINGUEZ],
    ['Ari', RODRIGUEZ_DOMINGUEZ],
    ['Juanjo', DOMINGUEZ_OLIVER],
    ['Sonia', DOMINGUEZ_OLIVER],
    ['Teresa', DOMINGUEZ_OLIVER],
    ['Vicky', DOMINGUEZ_OLIVER]
]

def check(todos) -> bool:
    for i in range(len(todos)):
        if todos[i][1] == todos[(i+1) % len(todos)][1]:
            return False
    return True

def print_beautiful(todos):
    for i in range(len(todos)):
        print(todos[i][0], '\t->', todos[(i+1) % len(todos)][0])

tries = 0
while not check(todos):
    shuffle(todos)
    tries += 1

print('Tries:', tries)
print('==========')
print_beautiful(todos)

