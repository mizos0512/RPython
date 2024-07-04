from io import open

def Lee_ficheros(fichero):
    personas=[]
    with open(fichero, 'r', encoding='utf-8') as fichero:
        cuerpo=fichero.readline().strip().split(';')
        for linea in fichero:
            valor=linea.strip().split(';')
            persona={cuerpo[i]:valor[i] for i in range(len(cuerpo))}   
            personas.append(persona)     
    return cuerpo, personas

def mostrar_lista_de_personas(cuerpo, persona):
   print(" ".join(cuerpo))
   for p in persona:
       print(" ".join([p[header] for header in cuerpo]))
  
        
if __name__ == '__main__':
    encabezado, person=Lee_ficheros('personas.txt')    
    mostrar_lista_de_personas(encabezado, person)        
