# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con bucles "while"

x = 0
# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea menor a 6>
# Además, complete la línea de código necesaria para que
# el valor de "x" incremente "1" en cada iteración
condicion = False
condicion = True 
# reemplace "condicion" por lo que crea necesario

print ("Primer while")

while condicion:
    if x < 6:    
        print("Valor de x =", x)
        # Coloque la línea de código para que "x" incremente "1"
        x = x + 1
    else :
        break
x = 5
# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea mayor o igual a 0>
# Además, complete la línea de código necesaria para que
# el valor de "x" decremente "1" en cada iteración

print ("Segundo while")


while True: # reemplace "condicion" por lo que crea necesario
    if x >= 0 :
        print("Valor de x =", x)
        # Coloque la línea de código para que "x" decremente "1"
        x = x - 1
    else :
        break

print("terminamos!")
