#Entradas: Tres numeros enteros
#Salidas: Producto y Promedio de los numeros de entrada
#Restricciones: Numeros enteros y la suma de los dos primeros numeros debe ser mayor que el tercer numero.
def numQuiz(a, b , c):
    x = a
    y = b
    z = c
    if(x + y > z):
        Producto = x * y * z
        Promedio = (x + y +z )/ 3
        print("El Producto es" , Producto," y El Promedio es" , Promedio )
    else:
        print("Sus numeros no cumplen los con requerimientos de trabajo, vuelva a intentarlo :/")
            
def Hey():
    print("Hey :)")
    
     
        
