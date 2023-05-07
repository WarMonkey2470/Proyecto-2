#Crear un programa para identificar la longitud de una palabra ingresada. 
#La palabra correcta debe tener entre cuatro y ocho letras. toma en cuenta las siguientes consideraciones:
#Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, se debe imprimir un mensaje que indique que la palabra es correcta
#Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: Hacen falta letras. Solo tiene N letras (siendo N el número de letras de la palabra)
#Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. Tiene N letras ((siendo N el número de letras de la palabra))
#Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. Tiene N letras ((siendo N el número de letras de la palabra))
palabra1 = input("Introduce la primera palabra: ")

if len(palabra1) < 2:
    palabra1 = "x" + palabra1

palabra = input("Introducce la segunda palabra: ") 
if len(palabra1) <4:
    print("tiene menos de cuatro letras")
elif len(palabra1) >8:
    print("Tiene mas de ocho caracteres")  
elif palabra1 ==8:
    print("La palabra esta en el rango")

else:
    print("Palabra icorrecta")



####################################################################################################



