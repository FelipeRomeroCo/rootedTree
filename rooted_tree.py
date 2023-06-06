# Descripción del programa

print("En este programa vamos a crear un rooted tree y luego consultar si un vértice es ancestro de otro, Para esto deberá ingresar la cantidad de vértices del rooted tree, la cantidad de consultas que desea realizar, las relaciones de descendencia presentes entre vértices y por último las consultas que desea realizar. Luego de cada consulta se evaluará si el vértice (u) es ancestro del vértice (v) y se mostrará el mensaje correspondiente.")

# Solicitud de los datos iniciales, cantidad de vértices y número de consultas a realizar

n = int(input("Ingrese la cantidad de vértices: "))

while not (n >= 1 and n <= 10**5):
    print("Debe ingresar un número positivo menor o igual a 100,000.")
    n = int(input("Ingrese nuevamente la cantidad de vértices: "))

q = int(input("Ingrese la cantidad de consultas que desea realizar: "))

while not (q >= 1 and q <= 10**5):
    print("Debe ingresar un número positivo menor o igual a 100,000.")
    q = int(input("Ingrese nuevamente la cantidad de vértices: "))

# Solicitud del ingreso de las relaciones del árbol

lines = n - 1

print("Ahora debe ingresar " + str(lines) + " relaciones de descendencia entre vértices")

tree = []
count = 1
while count < n:
    print ("Relación n° " + str(count))
    u = int(input("Ingrese el número del vértice: "))
    
    while not (u >= 1 and u <= n):
        print("Debe ingresar un número positivo, menor o igual a " + str(n))
        u = int(input("Ingrese nuevamente el número del vértice: "))
    
    v = int(input("Ahora ingrese el número de su descendencia: "))
    
    while not (v >= 1 and v <= n):
        print("Debe ingresar un número positivo, menor o igual a " + str(n))
        v = int(input("Ingrese nuevamente el número su descendencia: "))
    
    if (count == 1):
        tree.append(u)
        tree.append(v)
    else:
        tree.append(v)
        
    count += 1
    
# Realizar las consultas de acuerdo al valor "q" ingresado previamente

countQuery = 1
while countQuery <= q:
    print("Consulta n° " + str(countQuery) )
    uQuery = int(input("Ingrese el número del vertice (u): "))
    while not (uQuery >= 1 and uQuery <= n):
        print("Debe ingresar un número positivo, menor o igual a " + str(n))
        uQuery = int(input("Ingrese nuevamente el número del vértice (u): "))
        
    vQuery = int(input("Ingrese el número del vertice (v): "))
    while not (vQuery >= 1 and vQuery <= n):
        print("Debe ingresar un número positivo, menor o igual a " + str(n))
        vQuery = int(input("Ingrese nuevamente el número del vertice (v): "))
        
# Verificar si el vértice u es ancestro del vértice v
    
    indexU = tree.index(uQuery)
    indexV = tree.index(vQuery)
    
    if indexU == indexV:
        print("El vértice u (" + str(uQuery) + ") Sí es ancestro del vértice v (" + str(vQuery) + ").")
    elif indexU < indexV:
        print("El vértice u (" + str(uQuery) + ") Sí es ancestro del vértice v (" + str(vQuery) + ").")
    else:
        print("El vértice u (" + str(uQuery) + ") No es ancestro del vértice v (" + str(vQuery) + ").")
    
    countQuery +=1
    
print("Programa finalizado.")