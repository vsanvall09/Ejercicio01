from Finanzas import finanzaaa
from Ingresos import Ingreso
from Egresos import Egreso

IngreObj = Ingreso()
EgreObj = Egreso()
FinanObj = finanzaaa()

def CrearProyectoFinanzas ():
        print("**Crear un nuevo proyecto de finanzas**")
        Nombre = input("Ingrese el propietario del proyecto:")
        FinanObj.CrearCuenta(Nombre)
        

def RealizaIngreso():
        pass

def RealizaEgreso():
        pass

def ShowIngresos():
        ingresos = IngreObj.GetAllIngresos()
        if len(ingresos)>0:
                pass
        else  :
           print("**No se han efectuado ingresos al proyecto**")

def ShowEgresos():
       egresos = EgreObj.GetAllEgresos()
       if len(egresos)>0:
               pass
       else:
                print("**No se han efecuado egresos en este proyecto")

def ShowAllOperations():
       operaciones = [IngreObj.GetAllIngresos , EgreObj.GetAllEgresos]
       if len(operaciones)>0:
               for operacion in operaciones:
                       print(operacion)
       else:
                print("\n**No se han realizado operaciones en este proyecto de finanzas**\n")


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
        
    elif opcion  == "4":
            ShowIngresos()
    elif opcion == "5":
            ShowEgresos()
    elif opcion == "6":
            ShowAllOperations()

    