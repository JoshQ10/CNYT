from sys import stdin
import unittest
import math

v1 = [1, 2]

v2 = [3, 4]

def add_vectores(v1, v2):
    
    if len v1 != len v2:
        raise ValueError("Los vectores no tienen el mismo tamaño")
    
    for i in range(len(v1)):
        v1[i] += v2[i]
    
    return v1

def inverso_aditivo(v1):

    inverso = []

    for i in range(len(v1)):
        inverso.append(v1[i] * -1)
        
    return inverso

def multiplicacion_escalar(v1, escalar):

    for i in range (len(v1)):
        v1[i] *= escalar
        
    return v1

def add_matrices(v1, v2):
    
    if len v1!= len v2:
        raise ValueError("Los vectores no tienen el mismo tamaño")
    
    for i in range(len(v1)):
        for j in range(len(v2)):
            v1[i][j] += v2[i][j]
    
    return v1

def inverso_aditivo_matriz(v1, v2):

    inverso = []

    for i in range(len(v1)):
        for j in range(len(v2)):
            inverso.append(v1[i][j] * -1)
        
    return

def transpuesta_vector(v1, v2):
    
    transpuesta = []

    for i in range(len(v1)):
        for j in range(len(v2)):




