from Finanzas import finanzaaa, Ingresos, Egresos
 

IngreObj = Ingresos()
EgreObj = Egresos()
FinanObj = finanzaaa()

def CrearProyectoFinanzas ():
       
        FinanObj.CrearCuenta()
        

def RealizaIngreso():
        IngreObj.NewMonto()
        

def RealizaEgreso():
       EgreObj.NewEgr()


def ShowIngresos():
        IngreObj.AllIngresos()

def ShowEgresos():
       EgreObj.AllEgresos()

def ShowAllOperations():
       print("\n")
       print("Los ingresos que se han realizado son: ")
       IngreObj.AllIngresos()
       print("Los egresos que se han realizado son: ")
       EgreObj.AllEgresos()
       print("\n")


def ShowMonto():
    pass
 

while True:
    print("Bienvenido a tu programa de Finanzas \n")
    print ("Menu:\n"  )
    print ("(0)- Salir del Menu")
    print ("(1)- Crear una cuenta")
    print ("(2)- Agregar monto a la cuenta")
    print ("(3)- Realizar un retiro de la cuenta")
    print ("(4)- Consultar ingresos realizados a la cuenta")
    print ("(5)- Consultar egresos realizados a la cuenta")
    print ("(6)- Consultar todas las transacciones realizadas en la cuenta")
    print ("(7)- Consultar monto activo")
    opcion = input("Opcion : ")
    
    if opcion == "0":
         
          break
    elif opcion == "1":
         CrearProyectoFinanzas()
    elif opcion == "2":
            RealizaIngreso()
    elif opcion == "3":
            RealizaEgreso()        
    elif opcion  == "4":
            print("Los ingresos realizados son:")
            ShowIngresos()
            print("\n")
    elif opcion == "5":
            print("Los egresos realizados son: ")
            ShowEgresos()
            print("\n")

    elif opcion == "6":
            ShowAllOperations()
    elif opcion == "7":
            pass
    

    