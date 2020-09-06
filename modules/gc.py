import numpy as np
import matplotlib.pyplot as plt
import h5py as h5

time = np.genfromtxt("../data_files/global.30", usecols=1)[1:]
x = np.genfromtxt("../data_files/ORBIT",usecols=0)
y = np.genfromtxt("../data_files/ORBIT",usecols=1)
z = np.genfromtxt("../data_files/ORBIT",usecols=2)

plt.figure()
plt.plot(x,y)
plt.plot(x[0],y[0],'bo') #starting point of GC center
plt.plot(0,0,'rx') #origin aka center of MW
plt.xlabel('x [kpc]')
plt.ylabel('y [kpc]')
plt.xticks(np.arange(round(min(x)),round(max(x)+2),2))
plt.yticks(np.arange(round(min(y)),round(max(y)+2),2))
plt.savefig("../visuals/gc_path.pdf")

r = np.sqrt(x**2+y**2+z**2) #distance from MW

plt.figure()
plt.plot(time,r,'g')
plt.xlabel('Time [Myr]')
plt.ylabel('r [kpc]')
plt.savefig("../visuals/gc_time.pdf")
# plt.show()

apocenter = np.amax(r)
pericenter = np.amin(r)

frequency = 0 # calculated by the number of maximum points in the time graph
grad = np.gradient(r)
for i in range(len(grad)-1):
    if grad[i]>0 and grad[i+1]<0:
        frequency += 1

f = open("../output.txt","w+")
f.write("Apocenter: %s\n"%apocenter)
f.write("Pericenter: %s\n"%pericenter)
f.write("Frequency: %s"%frequency)
f.close()
