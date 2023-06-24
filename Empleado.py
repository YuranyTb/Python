from Persona import Persona
class Empleado(Persona):
    cargo=""
    valorhora=4800
    horastrabajadas=8
    departamento=""
    calcular=0

    def __init__(self, t, d, n, a, p, e, ed, s, c, vh, ht, dp):
        super().__init__(t, d, n, a, p, e, ed, s)
        self.cargo=c
        self.valorhora=vh
        self.horastrabajadas=ht
        self.departamento=dp
        

    def calcularHonorarios(self):
        self.calcular = (self.valorhora)*(self.horastrabajadas)-0,966

    def imprimirEmpleado(self):
        print("Los datos ingresados son: ",self.tipoDoc, self.documento, self.nombre, self.apellido, self.cargo, self.horastrabajadas, self.valorhora, " y el total a pagar es ",self.calcular) 
        



        

