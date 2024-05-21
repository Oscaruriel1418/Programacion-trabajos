a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo nuemro: "))
c = float(input("Ingresa el tercer numero: "))

if a > b and a > c:
    print("El mayor es: ",a )
elif b > c: 
    print("El mayor es: ",b)
else: 
    print("El mayor es: ",c)