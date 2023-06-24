class Persona:
    tipoDoc=""
    documento=""
    nombre=""
    apellido=""
    peso=""
    estatura=""
    edad=""
    sexo=""
    
    def __init__(self, t,d,n,a,p,e,ed,s):
        self.tipoDoc=t
        self.documento=d
        self.nombre=n
        self.apellido=a
        self.peso=p
        self.estatura=e
        self.edad=ed
        self.sexo=s

    def pedirDatos(self):
        self.tipoDoc=input("Ingrese el tipo de documento ")
        self.documento=int(input("Ingrese el número de documento ")) 
        self.nombre=input("Ingrese su nombre ") 
        self.apellido=input("Ingrese su apellido ") 
        self.peso=int(input("Ingrese su peso ")) 
        self.estatura=int(input("Ingrese su estatura ")) 
        self.edad=int(input("Ingrese su edad ")) 
        self.sexo=(input("Ingrese su genero ")) 

    def mostrarPersona(self):
        print("Los datos ingresados son: ",self.tipoDoc, self.documento, self.nombre, self.apellido, self.peso, self.estatura, self.edad, self.sexo)    

    def calcularImc(self):
        pesoActual= (self.peso)/(self.estatura)*self.estatura
        return pesoActual
    
    def mayorEdad(self):
        if self.edad >=18:
            print("El paciente es mayor de edad")
        else:
            print("El paciente no es mayor de edad")
                

        

        
        








        