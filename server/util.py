import json
import pickle
import numpy as np

__location=None
__data_columns=None
__model=None


def get_estimated_price(location,bhk,sq_ft,bath,balcony):
    try:
        loc=__data_columns.index(location.lower())
    except:
        loc=-1
    x=np.zeros(len(__data_columns))

    x[0]=bhk
    x[1]=sq_ft
    x[2]=bath
    x[3]=balcony
    if(loc>-1):
        x[loc]=1

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __location

def load_saved_artifacts():
    global __data_columns
    global __location
    global __model

    print("Loading the artifacts")
    with open('../model/columns.json','r') as f:
        __data_columns=json.load(f)['data_columns'] #now the variable contains all the data columns
        print(type(__data_columns))
        __location=__data_columns[4:]

    with open('../model/home_price_prediction.pickle','rb') as f: # since the model was saved as binary file we use 'rb'
        __model=pickle.load(f)

    print("Loading completed")


if __name__=='__main__':
    load_saved_artifacts()
    #print(get_estimated_price('1st block jayanagar',2,3000,1,1))