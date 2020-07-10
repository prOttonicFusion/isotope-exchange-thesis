import numpy as np


dataRootPath = '/home/otto/Drive2/isoEx_NVT/'

# Function for reading columnsToRead=[i,j,...] columns from file 'fname'
def readData(fname, columnsToRead):
    data = []
    print('Reading: {}'.format(fname))
    with open(fname) as f:
        f.readline() # skip header
        line = f.readline()
        while line:
            spltd = line.split()
            data.append([float(spltd[i]) for i in columnsToRead])
            line = f.readline()
    return np.array(data)
