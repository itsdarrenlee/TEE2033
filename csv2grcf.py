# This is python script to convert csv to grc readable format.
# The csv is obtained using Analog Discovery 2

import numpy as np
import csv
with open('yes_interference.csv') as f:
    reader = csv.reader(f, delimiter=',')
    rate = []
    tstart = []
    dat = np.array([])
    dat1 = np.array([])
    data = np.array([])
    data1 = np.array([])
    data2 = np.array([])
    i=0
    newFile=open("test.dat", "wb+")
    newFile1=open("time.dat", "wb+")
    for row in reader:
        dat = np.array(row[:])
        if (i==1) :
            tstart=float(row[0])
            dat1 = dat.astype(np.float)
            data=np.concatenate((data, dat1))
        elif (i>1) :
            dat1 = dat.astype(np.float)
            data=np.concatenate((data, dat1))
            if ((i%10000)==0) :
                data1 = data[1:len(data):2]
                data1.astype(np.float32).tofile(newFile)
                data2 = data[0:len(data):2]-tstart
                data2.astype(np.float32).tofile(newFile1)
                dat1 = np.array([])
                data = np.array([])
                data1 = np.array([])
                data2 = np.array([])
        i=i+1
    data1=data[1:len(data):2]
    data1.astype(np.float32).tofile(newFile)
    data2=data[0:len(data):2]-tstart
    data2.astype(np.float32).tofile(newFile1)
newFile.close()
newFile1.close()    
