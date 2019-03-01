
def prediction(U, V, Atest):
    MAE = 0
    MSE = 0
    #On sélectionne les couples (user, film) de la matrice A qui ont une note
    a = np.where(Atest != 0)
    user = a[0]
    film = a[1]
    nb_user = U.shape[0]
    for u in range(nb_user):
        d = 0
        indice_u = np.where(user == u)
        couple_ui = film[indice_u]
        MAE_u = 0
        MSE_u = 0
        for i in couple_ui:
            d = d+1
            MAE_u += abs(A[u][i] - np.vdot(U[u, :],V[i, :]))
            MSE_u += (A[u][i] - np.vdot(U[u, :],V[i, :]))**2
        MAE += MAE_u/d
        MSE += MSE_u/d
    return MSE, MAE
