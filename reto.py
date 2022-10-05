def promedio_lista():
    nums=[]
    numero=int(input("Digame cuantos numeros tiene el arreglo: "))
    i=0
    while i < numero:
        numA=float(input(f"Digite los numeros  {i+1}: "))
        nums.append(numA)
        i+=1
    prom = sum(nums)/len(nums)
    print(f'el promedio es {prom}')
    print(f"La lista de numeros creada es: {nums}")

promedio_lista()