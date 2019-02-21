#!/usr/bin/env python3

# importing pandas module
import pandas as pd
import numpy as np
# reading csv file from url
df = pd.read_csv("data_training.dat",
                 sep=":", #separator whitespace
                 header=None)

nb_film = 4000
nb_user = 6040
matrixA = np.zeros((nb_user, nb_film))

for line in range(0,len(df)):
    matrixA[df[0][line] - 1 ][df[1][line] - 1] = df[2][line]

np.savetxt('matrixA.txt', matrixA,  fmt='%i')
