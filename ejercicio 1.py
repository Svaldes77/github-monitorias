import random
def sum1(n):
    global first_numbers
    first_numbers = 0
    for i in range(0, 3):
        first_numbers += int(n[i])

def sum2(n):
    global second_number
    second_number = 0
    for i in range(3, 5):
        second_number += int(n[i])

def totalsum(n):
    print(f"el numero aleatorio es : {n}")
    if first_numbers == second_number:
        print(f"""
La suma de los primeros 3 digitos ({n[0:3]}) es igual a {first_numbers}
La suma de los ultimosd 2 digitos ({n[3:5]}) es igual a {second_number}

¡GENIAL👌! La comprobacion es valida""") 
    else:
        print(f"""
La suma de los primeros 3 digitos ({n[0:3]}) es igual a {first_numbers}
La suma de los ultimosd 2 digitos ({n[3:5]}) es igual a {second_number}

¡Rayos😡¡ la comprobacion es invalida""")


if __name__ == "__main__":
    n = str(random.randint(10000, 99999))
    sum1(n)
    sum2(n)
    totalsum(n)