import numpy as np
import collections as col

#Gradient de la vraissemblance selon le vecteur Uu
def gradient_U(Aui, Uu, Vi, Lambda):
    return(-2 * (Aui - np.vdot(Uu, Vi))*Vi + 2 * Lambda * Uu)

#Gradient de la vraissemblance selon le vecteur Vi
def gradient_V(Aui, Uu, Vi, Lambda):
    return(-2 * (Aui - np.vdot(Uu, Vi))*Uu + 2 * Lambda * Vi)

#Fonction vraissemblance
def vraissemblance(A, U, V, Lambda) :
    value = 0
    #On sélectionne les couples (ligne, colonne) de la matrice A qui ont une note
    a = np.where(A != 0)
    ligne = a[0]
    colonne = a[1]
    for k in range(len(ligne)):
        u = ligne[k]
        i = colonne[k]
        Uu = U[u, :]
        Vi = V[i, :]
        scalar = np.vdot(Uu, Vi)
        norme1 = np.vdot(Uu, Uu)
        norme2 = np.vdot(Vi, Vi)
        value += ((A[u][i] - scalar)**2 + Lambda*(norme1 + norme2))
    return value

def descenteGradient(A, U0, V0, eta, Lambda, epsilon):
    #Le nombre d'utilisateur
    nb_user = U0.shape[0]
    #Le nombre de film
    nb_film = V0.shape[0]
    #Le paramètre k
    parameters = U0.shape[1]
    #Initialisation des vecteurs pour la descente du gradient
    Uprec = U0
    Vprec = V0
    #Vecteurs dans lesquels on stocke les nouvelles valeurs de U et V
    U = np.zeros((nb_user, parameters), dtype=np.float64)
    V = np.zeros((nb_film, parameters), dtype=np.float64)
    #On sélectionne les couples (ligne, colonne) de la matrice A qui ont une note
    a = np.where(A != 0)
    ligne = a[0]
    colonne = a[1]
    print("ligne")
    print(ligne)
    print("colonne")
    print(colonne)
    ligne_distinct = col.Counter(ligne)
    col_distinct = col.Counter(colonne)
    #Calcul de la vraissemblance initiale
    vraissemblance_prec = vraissemblance(A, U0, V0,Lambda)
    k = 0
    while True:
        print(k)
        print("matrice U")
        #On récupère les utilisateurs qui ont noté un film
        for u in ligne_distinct:
            indice_u = np.where(ligne == u)
            couple_ui = colonne[indice_u]
            vecteur_U = np.zeros(parameters)
            #Les films que a noté l'utilisateur i
            for i in couple_ui:
                vecteur_U = vecteur_U  + gradient_U(A[u][i], Uprec[u,:], Vprec[i,:], Lambda)
            U[u, :] = Uprec[u,:] - eta * vecteur_U
        print("matrice V")
        #On récupère les films qui ont été noté
        for i in col_distinct:
            indice_i = np.where(colonne == i)
            couple_ui = ligne[indice_i]
            vecteur_V = np.zeros(parameters)
            #Les utilisateurs qui ont noté le film i
            for u in couple_ui:
                vecteur_V = vecteur_V + gradient_U(A[u][i], Uprec[u,:], Vprec[i,:], Lambda)
            V[i, :] = Vprec[i,:] - eta*vecteur_V
        rec = vraissemblance(A, U, V,Lambda)
        diff = abs( rec - vraissemblance_prec )
        print("L(A, Uprec, Vprec)")
        print(vraissemblance_prec)
        print("L(A, U, V)")
        print(rec)
        print("Diff")
        print(diff)
        if diff > epsilon :
            Uprec = U
            Vprec = V
            vraissemblance_prec = rec
        else:
            break
        k = k + 1
    return U, V

#essaie
# matrixA = np.loadtxt('matrixA.txt',delimiter=" ", dtype = int)
# print("chargement des données")
# nb_film = 4000
# nb_user = 6040

# k = 5
# A = np.array([[1,2,3],[0,0,4],[0,0,1], [4,3,2]], dtype=int)
# U_init = np.random.rand(4, k).astype(np.float64)
# V_init = np.random.rand(3, k).astype(np.float64)
# eta = 0.1
# Lambda = 0.001
# epsilon = 0.001
# a = np.where(matrixA != 0)
# ligne = a[0]
# colonne = a[1]
# k = 5
# U_init = np.random.rand(nb_user, k)
# V_init = np.random.rand(nb_film, k)
# print(U_init)
# print(V_init)
# print(vraissemblance(matrixA, U_init, V_init, ligne, colonne, Lambda))
# result = descenteGradient(matrixA, U_init, V_init, eta, Lambda, epsilon)
# print(result[0])
# print(result[1])

k = 5
A = np.array([[1,2,3],[0,0,4],[0,0,1], [4,3,2]])
V_init = np.random.rand(3, k).astype(np.float64)
U_init = np.random.rand(4, k).astype(np.float64)
eta = 0.1
Lambda = 0.1
epsilon = 0.001
print(A)
result = descenteGradient(A, U_init, V_init, eta, Lambda, epsilon)
print(result[0])
print(result[1])
