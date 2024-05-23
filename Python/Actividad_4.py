############################################################################
# Dado el peso y la altura de un paciente. Elabore un código que calcule e #
# imprima el IMC (índice de masa corporal) además del nombre completo,     #
# sexo y edad del  Paciente. La fórmla del IMC con la que trabajaremos es: #
#                                                                          #
#                      IMC = Peso/Altura^2                                 # 
#                                                                          #
############################################################################

Nombre = input("Nombre del Paciente: ")
Sexo= input("Sexo 'M' o 'F': ")
edad= input("Edad: ")
Altura=float(input("Estatura en 'm': "))
Peso=float(input("Peso en 'kg': "))
print()
print("Paciente: {}".format(Nombre))
print("Sexo: {}".format(Sexo))
print("Edad: {}".format(edad))
print("Estatura: {}".format(Altura))
print("Peso: {}".format(Peso))
print()
print("IMC: {:.2f}".format(Peso/Altura**2))
print()

#### SALIDA ####

# Nombre del Paciente: Reinaldo Díaz Mizos
# Sexo 'M' o 'F': M
# Edad: 62
# Estatura en 'm': 1.79
# Peso en 'kg': 83

# Paciente: Reinaldo Díaz Mizos
# Sexo: M
# Edad: 62
# Estatura: 1.79
# Peso: 83.0

# IMC: 25.90