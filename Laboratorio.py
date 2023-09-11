import math as mt
from numpy import *
def sumacplx(c1, c2): #(-2,7.2)
    Real = c1[0]+c2[0]
    Imaginary = c1[1]+c2[1]
    return (Real, Imaginary)

def restacplx(c1, c2): #(8,-3.2)
    Real = c1[0]-c2[0]
    Imaginary = c1[1]-c2[1]
    return (Real, Imaginary)

def multcplx(c1, c2): #(-25.4,5.6)
    Real = c1[0]*c2[0]-c1[1]*c2[1]
    Imaginary = c1[0]*c2[1]+c1[1]*c2[0]
    return (Real, Imaginary)

def divcplx(c1, c2): #(-2.254901961, -12.54901961)
    Real = (c1[0]*c2[0]+c1[1]*c2[1])/(c2[0]**2+c2[1]**2)
    Imaginary = (c1[1]*c2[0]-c1[0]*c2[1])/(c2[0]**2+c2[1]**2)
    return (Real, Imaginary)

def modcplx(c1, c2):
    modulo = mt.sqrt(c1**2 + c2**2)
    return modulo



def conjugadoclpx(c1): #(3, -2)
    Real = c1[0]
    Imaginary = -c1[1]
    return (Real, Imaginary)

def invrcplx(c1):
    Real = -c1[0]
    Imaginary = -c1[1]
    return (Real, Imaginary)

def fasecplx(c1): #-0.588 rad o -33.69°

    '''Arctan(imaginary/real)'''

    fasec1 = mt.atan2(c1[1], c1[0])
    return fasec1


def suma_vectores(v1, v2):
    
    if len(v1) != len(v2):
        raise ValueError("Los vectores no tienen el mismo tamaño")
    
    res = [(0,0) for i in range(len(v1))]
    for i in range(len(v1)):
        res[i] = sumacplx(v1[i], v2[i])
    
    return res

def inverso_aditivo(v1):


    for i in range(len(v1)):
        v1[i] = invrcplx(v1[i])
        
    return v1

def multiplicacion_vector(v1, escalar):

    for i in range (len(v1)):
        v1[i] = multcplx(v1[i],escalar)
        
    return v1

def suma_matrices(v1, v2):
    
    if len (v1) != len (v2):
        raise ValueError("Los vectores no tienen el mismo tamaño")
    
    for i in range(len(v1)):
        for j in range(len(v2)):
            v1[i][j] = sumacplx(v2[i][j],v1[i][j])
    
    return v1

def inverso_aditivo_matriz(v1):


    for i in range(len(v1)):
        for j in range(len(v1[0])):
            v1[i][j] = invrcplx(v1[i][j])
            
    return v1

def transpuesta_matriz(v1):
    matriz = []
    for i in range(len(v1)):
        matriz.append([])
        for j in range(len(v1[0])):
            matriz[i].append((0,0))
    
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            matriz[i][j] = v1[j][i]
            
    return matriz

def conjugada_matriz(v1):
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            v1[i][j] = conjugadoclpx(v1[i][j])
    
    return v1

def producto_puntoMatriz(v1,v2):
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            resultado = v1[i][j]*v2[i][j]
    return resultado

def producto_cruzMatriz(v1,v2):
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            resultado = v1[(i + 1) % len(v1[i])][j] * v2[(i + 2) % len(v1[i])][j] - v1[(i + 2) % len(v1[i])][j] * v2[(i + 1) % v1[i]][j]

    return resultado


def accion_matriz(v1,m1):
    if len(v1) != len(m1[i]):
        print("El vector y la matriz no son compatibles")
        
    else:   
        for i in range(len(v1)):
            resultado = v1[i]*m1[i][j]
        
        return resultado 

def producto_int(v1, v2):
    resultado = np.dot(v1,v2)
    
    return resultado

def norma_vector(v1):
    resultado = np.linalg.norm(v1)
    
    return resultado    
    
    
def producto_tensor(m1, m2):
    fila1 = len(m1)
    columna1 = len(m1[0])
    fila2 = len(m2)
    columna2 = len(m2[0])
    
    matriz = [[(0,0) for k in range(columna1*columna2)] for j in range(fila1*fila2)]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = producto_puntoMatriz[(m1[i//fila1], m2[j//columna2])],(m2[i%fila2],[j%columna2])

    return matriz


def main():
    c1 = (3,2)
    c2 = (-5,5.2)
   
        # Funciones Basicas (lab1)
    print ("Funciones complejas basicas\n")
    print ("La dupla dada es:", "[",c1, c2, "]\n")
    print ("Suma: ", sumacplx (c1,c2))
    print ("Resta: ", restacplx(c1,c2))
    print ("Multiplicacion: ", multcplx(c1,c2))
    print ("Division: ", divcplx(c1,c2))
    

    v1 = [(1, 2), (3, 3), (4, 4), (5, 5)]
    v2 = [(3, 2), (4, 2), (3, 2), (0, 8)]
    m1 = [[(1, 2), (3, 3)], [(4, 4), (5, 5)]] 
    m2 = [[(3, 5), (4, 5)], [(5, 5), (9, 4)]] 
    
        # Se guardan las funciones complejas entre matrices y vectores (lab2)
    print ("Funciones complejas basicas\n")
    print ("La sum de vectores es: ", suma_vectores (v1,v2))
    print("El inverso es: ", inverso_aditivo(v1))
    print("La multiplicacion de vectores es: " ,multiplicacion_vector(v1,(2,0)))
    print("La transpuesta es: ", transpuesta_matriz(m1))
    print("La suma de las matrices es: ", suma_matrices(m1, m2))
    print("El producto tensor entre las matrices es: ", producto_tensor(m1, m2))
    """
    vector = [(2, 5), (3, 6)]
    vc = []
    for i in range (0, len(vector)):
        vc.append((0,0))
    print(vc)
    """
main()