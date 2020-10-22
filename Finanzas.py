class finanzaaa :
    def __init__(self):
        self.cuenta = []
        self.IdCuenta = 0
       
    def CrearCuenta (self, Nombre):
        self.IdCuenta +=1
        IdProyect = self.IdCuenta
        cuentaDic = {"Id" : IdProyect, "Nombre": Nombre}
        self.cuenta.append(cuentaDic)
    def GetCuentas (self):
        return self.cuenta

    

        
    
    
    