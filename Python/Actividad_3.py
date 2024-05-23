#######################################################################
# Dado un par de números reales que reciba como entrada. Elaborar un  #
# código que  calcule e imprima todas las operaciones básicas:        #
# Suma, Resta, Multiplicación, Divición (en punto flotante y entera), # 
# Módulo y Potencia.                                                  #
#######################################################################

n1= float(input("Introduzca el primer número: "))
n2= float(input("Introduzca el segundo número: "))
print()
print("La suma de {} y {} es: {}".format(n1, n2, n1+n2))
print("La resta de {} y {} es: {}".format(n1, n2, n1-n2))
print("La multiplicación de {} y {} es: {}".format(n1, n2, n1*n2))
print("La división flotante de {} y {} es: {}".format(n1, n2, n1/n2))
print("La división entera de {} y {} es: {}".format(n1, n2, n1//n2))
print("El módulo de {} y {} es: {}".format(n1, n2, n1%n2))

#### SALIDA ####

#Introduzca el primer número: 13
#Introduzca el segundo número: 2

# La suma de 13.0 y 2.0 es: 15.0
# La resta de 13.0 y 2.0 es: 11.0
# La multiplicación de 13.0 y 2.0 es: 26.0  
# La división flotante de 13.0 y 2.0 es: 6.5
# La división entera de 13.0 y 2.0 es: 6.0  
# El módulo de 13.0 y 2.0 es: 1.0