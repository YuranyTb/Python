from Repaso import Repaso
class Repaso1(Repaso):
    email=""
    celular=""
    ndocumento=""

    email=input("Ingrese su email: ")
    celular=int(input("Ingrese su celular"))
    ndocumento=input("Ingrese su número de documento: ")

    def imprimirInformación(self):
        print("Los datos ingresados son: ",self.nombre, self.apellido, self.ndocumento, self.ciudad, self.dirección, self.celular, self.email)

        
            


