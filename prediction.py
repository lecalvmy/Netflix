
def prediction(U, V, Atest):
    d = 0
    MAE = 0
    MSE = 0
    nb_user = U.shape[0]
    for u in range(nb_user):
        for Aui in Atest:
            d += 1
            MAE += abs(Aui - )
            MSE +=
    MAE /= (nb_user * d)
    return MSE, MAE
