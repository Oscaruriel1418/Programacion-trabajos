while True:
      
      print("\n1. Saludar\n2. Despedirse\n3. Salir")
      opcion=input("elige una opcion: ")
      if opcion =="1":
          print("Hola")
      elif opcion == "2":
          print("adios")
      elif opcion == "3":
          print("saliendo del menú")
          break
      else:
          print("opcion no valida")