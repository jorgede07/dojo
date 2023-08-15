from random import randint

def repartir():
    dominguez_edo = ['Javi', 'Carmen', 'Sergio', 'Jorge']
    check = dominguez_edo.copy()
    rodriguez_dominguez = ['Pepe', 'Concha', 'Pep', 'Javier', 'Ari']
    dominguez_oliver = ['Juanjo', 'Sonia', 'Teresa', 'Victoria']

    all_families = [dominguez_edo, rodriguez_dominguez, dominguez_oliver] 

    regalador_family = all_families[0]
    regalador = regalador_family.pop(0)
    solucion = [regalador]
    familia_regalado = []

    todos_juntos = [k for family in all_families for k in family]

    try:
        while len(todos_juntos) > 0:
            # print(regalador)
            otras_familias = [persona for family in all_families for persona in family if family != regalador_family]
            regalado = otras_familias[randint(0, len(otras_familias)-1)]
            index = -1
            for family in all_families:
                for person in family:
                    if person == regalado:
                        familia_regalado = family
                        index = familia_regalado.index(regalado)
                        break
            regalador = regalado
            regalador_family = familia_regalado
            solucion.append(regalador_family.pop(index))
            todos_juntos = [k for family in all_families for k in family]

        # print(regalador)
    except ValueError:
        return repartir()
    
    try:
        assert len(solucion) == 13
    except AssertionError:
        return repartir()
        

    try:
        # print('----')
        check.index(solucion[len(solucion)-1])
    except ValueError:
        return solucion
    else:
        return repartir()
        
sol = repartir()

print('==========')
print(sol)
print('==========')
