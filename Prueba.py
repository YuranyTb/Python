from Persona import Persona
from Empleado import Empleado

Persona1=Persona("cc", 1016103908, "Yurany", "Tapia", 54, 1.54, 25, "Femenino")
Em=Empleado("cc", 1016103908, "Yurany", "Tapia", 54, 1.54, 25, "Femenino","",8, 4800, 0)

Persona1.pedirDatos()
Em.calcularHonorarios()
Em.imprimirEmpleado()
