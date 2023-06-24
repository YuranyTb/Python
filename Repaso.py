class Repaso:
    nombre=""
    apellido=""
    ciudad=""
    dirección=""

  

    def pedirDatos(self):
        self.nombre=input("Ingrese su nombre: ")    
        self.apellido=input("Ingrese su apellido: ") 
        self.ciudad=input("Ingrese la ciudad, donde reside: ")
        self.dirección=input("Ingrese su dirección: ")

    def mostrarDatos(self):
        print("Los datos ingresados son: ",self.nombre, self.apellido, self.ciudad, self.dirección)    

    def validaciónCiudad(self):
        if self.ciudad == "Bogotá":
            print("La mejor ciudad")
        else:
            print("Bienvenido a la mejor ciudad, Bogotá")    



