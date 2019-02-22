import numpy as np
import collections as col

#Gradient de la vraissemblance selon le vecteur Uu
def gradient_U(Aui, Uu, Vi, Lambda):
    membre_gauche = np.multiply(-2, np.multiply((Aui - np.vdot(Uu, Vi)), Vi))
    membre_droit = np.multiply(2*Lambda, Uu)
    return np.add(membre_gauche, membre_droit)

#Gradient de la vraissemblance selon le vecteur Vi
def gradient_V(Aui, Uu, Vi, Lambda):
    membre_gauche = np.multiply(-2, np.multiply((Aui - np.vdot(Uu, Vi)), Uu))
    membre_droit = np.multiply(2*Lambda, Vi)
    return np.add(membre_gauche, membre_droit)

#Fonction vraissemblance
def vraisemblance(A, U, V, Lambda):
    value = 0
    #On sélectionne les couples (ligne, colonne) de la matrice A qui ont une note
    a = np.where(A != 0)
    ligne = a[0]
    colonne = a[1]
    for k in range(len(ligne)):
        u = ligne[k]
        i = colonne[k]
        Uu = np.copy(U[u,:])
        Vi = np.copy(V[i,:])
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
    Uprec = np.copy(U0)
    Vprec = np.copy(V0)
    #Vecteurs dans lesquels on stocke les nouvelles valeurs de U et V
    U = np.zeros((nb_user, parameters), dtype=np.float64)
    V = np.zeros((nb_film, parameters), dtype=np.float64)
    #On sélectionne les couples (ligne, colonne) de la matrice A qui ont une note
    a = np.where(A != 0)
    ligne = a[0]
    colonne = a[1]
    ligne_distinct = col.Counter(ligne)
    col_distinct = col.Counter(colonne)
    #Calcul de la vraissemblance initiale
    vraisemblance_prec = vraisemblance(A, U0, V0,Lambda)
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
                vecteur_U = np.add(vecteur_U, gradient_U(A[u][i], Uprec[u,:], Vprec[i,:], Lambda))
            U[u, :] = np.add(Uprec[u,:], np.multiply(-eta, vecteur_U))
        print("matrice V")
        #On récupère les films qui ont été noté
        for i in col_distinct:
            indice_i = np.where(colonne == i)
            couple_ui = ligne[indice_i]
            vecteur_V = np.zeros(parameters)
            #Les utilisateurs qui ont noté le film i
            for u in couple_ui:
                vecteur_V = np.add(vecteur_V, gradient_U(A[u][i], Uprec[u,:], Vprec[i,:], Lambda))
            V[i, :] = np.add(Vprec[i,:], np.multiply(-eta, vecteur_V))
        rec = vraisemblance(A, U, V,Lambda)
        diff = abs(rec - vraisemblance_prec)
        print("L(A, Uprec, Vprec)")
        print(vraisemblance_prec)
        print("L(A, U, V)")
        print(rec)
        print("Diff")
        print(diff)
        if diff > epsilon :
            Uprec = U
            Vprec = V
            vraisemblance_prec = rec
        else:
            break
        k = k + 1
    return U, V

k = 1
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
