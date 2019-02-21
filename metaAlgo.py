import numpy as np

for k in  {5,10,20,30,50,100,150,200,500,1000}:
    #Matrice d'apprentissage
    A = np.loadtxt('matrixA.txt',delimiter=" ", dtype = int)
    #Matrice de test
    Atest = np.loadtxt('matrixAtest.txt',delimiter=" ", dtype = int)
    #Apprentissage
    #descente pour trouver U* et V*
    descenteGradient()
    #Test
    #calcul MSE, MAE
    MSE, MAE = prediction(U, V, Atest)
