numero=int(input("Digame cuantos numeros tiene el arreglo: "))

def sumar():
    numA={}
    if numero<1:
        print("Imposible")
    else:
        numeros=[]
        for i in range(numero):
            numA=input(f"Digite los numeros  {i+1}: ")
            numeros.append(numA)
            
        print(f"La lista de numeros creada es: {numeros}")
        

sumar()