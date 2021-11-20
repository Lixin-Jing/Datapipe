import os
import numpy as np
import pandas as pd

path_0 = "./data"
filelist  = os.listdir(path_0)

DataList = []
file_test = open('./data/Luepschen2005/Rampe1.fpv.txt','r')

for line in file_test:
    for value in line.split():
        DataList.append(value)

NewArray = np.array(DataList)
NewArray1 = NewArray.reshape(110900,6)

NewData = pd.DataFrame(NewArray1)
NewData.columns = ['Airway flow[l/s]','Real pressure[cmH2O]','CO2-conc.[Volt]',
                   'ext.flow[l/st]','rel.Lungvol.[Volt]','Triggersignal(Insp./Exsp.)']
NewData.to_excel('/Users/jinglixin/Desktop/Datapipe/data/A.xlsx',index=False)

file_test.close()


data_xls = pd.read_excel('A.xlsx',index_col=0)
data_xls.to_csv('A.csv',encoding='utf-8')


