class finanzaaa :
    def __init__(self):
        pass

    def CrearCuenta(self):
        name = input("Ingresa tu nombre para abrir tu cuenta financiera: ")
        print(f"esta cuenta pertenecera a: ", name, "\n")
class Ingresos:
    def __init__(self):
        self.Ing = []

    def NewMonto (self):
        monto = int(input("Ingresa el monto que se agregara: "))
        self.Ing.append(monto)
        self.sumaIngreso = 0
        self.sumaIngreso += monto

    def AllIngresos(self):
        for x in self.Ing:
            print(x)
 
class Egresos :
    def __init__(self):
        self.egresos = []

    def NewEgr(self):
        egreso = int(input("Registra tus Egresos: $"))
        self.egresos.append(egreso)
        self.sumaEgreso = 0
        self.sumaEgreso += egreso

    def AllEgresos (self):
        for x in self.egresos:
            print(x)




