#!/usr/bin/env python3
import numpy as np

matrixA = np.loadtxt('matrixA.txt',delimiter=" ", dtype = int)
a = np.where( matrixA != 0)
ligne = a[0]
colonne = a[1]

def produitScalaire(U, V):
    somme = 0
    for k  in range(len(U)):
        somme += (U[k] * V[k])
    return somme

def laplacien(A, U, V, ligne, colonne, Lambda ) :
    value = 0
    for k in range(len(ligne)):
        u = ligne[k]
        i = colonne[k]
        Uu = U[u]
        Vi = V[i]
        scalar = produitScalaire(Uu, Vi)
        norme1 = produitScalaire(Uu, Uu)
        norme2 = produitScalaire(Vi, Vi)
        value += ((A[u][i] - scalar)^2 + Lambda*(norme1 + norme2))
    return value
