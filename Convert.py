import os
import numpy as np
import pandas as pd



path_0 = "./data"
filelist  = os.listdir(path_0)

DataList = []
file_test = open('/Users/jinglixin/Desktop/Datapipe/data/Luepschen2005/Rampe1.fpv.txt','r')

for line in file_test:
    for value in line.split():
        DataList.append(value)

NewArray = np.array(DataList)
NewArray = NewArray.reshape(110900,6)

NewData = pd.DataFrame(NewArray)
NewData.columns = ['Airway flow[l/s]','Real pressure[cmH2O]','CO2-conc.[Volt]',
                   'ext.flow[l/st]','rel.Lungvol.[Volt]','Triggersignal(Insp./Exsp.)']

NewFile = pd.ExcelWriter('Ramp1FPV.xlsx')
NewData.to_excel(NewFile,float_format='%.5f')







"""
file_write = open('./data/Luepschen2005/Rampe1FPV.csv','a')
file_write.write("Airway flow[l/s]       Real pressure[cmH2O]       CO2-conc.[Volt]       ext.flow[l/st]       rel.Lungvol.[Volt]       Triggersignal(Insp./Exsp.) ")
file_write.write('\n')
for line in DataList:
    file_write.write(line)
    file_write.write('\n')
file_write.close()
print("Alles erfolgreich")


"""


"""

for files in filelist:
    dir_path = os.path.join(path_0,files)
    file_name = os.path.splitext(files)[0]
    file_type = os.path.splitext(files)[1]

    if file_type == ".fpv":

new_dir = os.path.join(path_0,str(file_name)+'fpv'+'.csv')

file_test2 = open(new_dir,'wb')
for lines in file_test.readlines():
    lines = lines.decode()
    str_data = ",".join(lines.split('.'))
    file_test2.write(str_data.encode("utf-8"))
"""
file_test.close()




