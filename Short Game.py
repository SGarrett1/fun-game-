# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 14:34:36 2019

@author: sg00898
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd
import math
Location = "gamescript.csv"
df = pd.read_csv(Location, header=None)


statement= df.iloc[0][1]
option1 = df.iloc[0][2]
option2 = df.iloc[0][3]
option3 = df.iloc[0][4]
loc1= df.iloc[0][5]
loc2 = df.iloc[0][6]
loc3 = df.iloc[0][7]
image=df.iloc[0][8]


def decision(statement, option1, option2, option3, loc1, loc2, loc3, image):
    print(statement)
    print('Do you a: ', option1, ' or: ', option2, ' or: ', option3)
    try:
        b=input('')
        if b=='1':
            loc=loc1
        elif b=='2':
            loc=loc2
        elif b=='3':
            loc=loc3
        a=loc-1
    except:
        print('Press something else spax')
        decision(statement, option1, option2, option3, loc1, loc2, loc3)
    
    #Loads relevant line from excel file 
    statement= df.iloc[a][1]
    option1 = df.iloc[a][2]
    option2 = df.iloc[a][3]
    option3 = df.iloc[a][4]
    loc1= df.iloc[a][5]
    loc2 = df.iloc[a][6]
    loc3 = df.iloc[a][7]
    image=df.iloc[a][8]

    #Prints images 
    if type(image) != str:
        decision(statement, option1, option2, option3, loc1, loc2, loc3, image)
    if type(image) !=None:
        img=mpimg.imread(str(image))
        plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
        plt.imshow(img)
        plt.show()
    
    decision(statement, option1, option2, option3, loc1, loc2, loc3, image)

decision(statement, option1, option2, option3, loc1, loc2, loc3, image)























#
#
#dfList = df.iloc[0][1]
#print('statement1', dfList)
#dfList = df.iloc[0][2]
#print('Option1', dfList)
#dfList = df.iloc[0][3]
#print('Option2', dfList)
#dfList = df.iloc[0][4]
#print('Option3', dfList)
#dfList = df.iloc[0][5]
#print('loc1', dfList)
#dfList = df.iloc[0][6]
#print('loc2', dfList)
#dfList = df.iloc[0][7]
#print('loc3', dfList)














