a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el senguno numero: "))
operacion = input("Ingresa la operacion +,-,*,/: ")

if operacion == "+":
 ope = a + b 
 print("El resultado es: ", ope)
elif operacion == "-":
 ope2 = a - b
 print("El resultado es: ",ope2)
elif operacion == "*":
 ope3 = a * b
 print("El resultado es: ", ope3)
elif operacion == "/": 
 ope4 = a / b
 print("El resultado es: ", ope4)
 if b  != 0:
    resultado = a/ b
 else: resulatdo = "Error: divicion por cero "

else: resulatdo = "operacion no valida "