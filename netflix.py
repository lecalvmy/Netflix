#!/usr/bin/env python3

# importing pandas module
import pandas as pd

# reading csv file from url
df = pd.read_csv("ratings.dat",
                 sep="::", #separator whitespace
                 header=None, #none header
                 engine='python')
 #df[colonne][ligne]
 #df[0] colonne user, df[1] colonne id film, df[2] colonne rate, df[3] colonne timestamp

data_training = pd.DataFrame()
data_test = pd.DataFrame()
user_nbRating = {}

#le numéro de l'utilisateur
currentUser = 1
#le nombre de film qu'il a aimé
ratingUser = 0
line = 0
while line < len(df) and df[0][line] == currentUser:
    ratingUser += 1
    line += 1
    if line < len(df) and df[0][line] != currentUser:
        user_nbRating[currentUser] = ratingUser
        ratingUser = 0
        currentUser = df[0][line]
#Pour le dernier utilisateur
user_nbRating[currentUser] = ratingUser
#print(user_nbRating)

# print(user_nbRating[6038])

ligne = 0
for user_id in user_nbRating:
    data_training_user = pd.DataFrame()
    data_test_user = pd.DataFrame()
    index = int(0.7 * user_nbRating[user_id])
    data_training_user = df.loc[ligne:index+ligne-1,]
    data_test_user = df.loc[index + ligne : ligne + user_nbRating[user_id],]
    data_training = pd.concat([data_training, data_training_user])
    data_test = pd.concat([data_test, data_test_user])
    ligne = ligne + user_nbRating[user_id]

#print(data_training)

data_training.to_csv('data_training.dat', sep=':',header=None, index = False)
data_test.to_csv('data_test.dat', sep=':',header=None, index = False)
