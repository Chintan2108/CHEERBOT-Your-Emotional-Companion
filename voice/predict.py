import math
import pandas as pd

def euDis(x, y):
    return (pow(x-y))

def load(filename, train="True"):
    if(train):
        df = pd.read_csv('\\train\\' + filename)
    else:
        df = pd.read_csv('\\test\\' + filename)
    data = [[] for i in range(3)]
    data[0].extend(df['hz'])
    data[1].extend(df['time-gaps'])
    data[2].extend(df['state'])
    return data

def predict(train, test):
    for i in test:
        #calculate distance here and find min
        i[0]
        
        

