#Importing some classes
import matplotlib.pyplot as mat
from datetime import datetime

#Initialization of data arrays
time_data = []
delt_data = []
cloc_data = []

temp_data = []
celc_data = []

pres_data = []
pasc_data = []

#Opening the text file
d = open('bmp280_data.txt','r')
bmp280_data = d.readlines()
d.close()

#Sorting out the data
for line in range(0,2442):
    time_data.append(datetime.strptime((bmp280_data[line])[11:26], '%H:%M:%S.%f'))
    delt_data.append(time_data[line]-time_data[0])
    cloc_data.append(delt_data[line].total_seconds())
    temp_data.append((bmp280_data[line])[27:38])
    pres_data.append((bmp280_data[line])[42:53])

for line in range(0,2442):
    celc_data.append(float(temp_data[line]))
    pasc_data.append(float(pres_data[line]))

#Making into some graphs
mat.figure(1)
mat.plot(cloc_data, celc_data)
mat.xlabel('Time (s)')
mat.ylabel('Temperature (C)')
mat.title("Temperature vs. Time")

mat.figure(2)
mat.plot(cloc_data, pasc_data)
mat.xlabel('Time (s)')
mat.ylabel('Pressure (kPa)')
mat.title("Pressure vs. Time")

mat.show()

print pasc_data
