import h5py as h5
import matplotlib.pyplot as plt
import numpy as np
import shrinking_sphere as ss
import massprofile as mp

data = h5.File('../data_files/snap.40_240.h5part','r')
fig,ax = plt.subplots()
mp.mass_at(data,0,ax)
fig.suptitle("Disk Mass: 5e9, Halo Mass: 1.203e12")
plt.savefig("../visuals/mass_profile_at.pdf")
fig,ax = plt.subplots()
ratio = mp.mass_cumulative(data,0,ax)
fig.suptitle("Disk Mass: 5e9, Halo Mass: 1.203e12")
data.close()
f = open("../output.txt","a")
f.write("\nM(80)/M(10): %s"%ratio)
f.close()
plt.savefig("../visuals/mass_profile_cumulative.pdf")

x = np.genfromtxt("../data_files/ORBIT",usecols=0) #kpc
y = np.genfromtxt("../data_files/ORBIT",usecols=1)
time = np.genfromtxt("../data_files/global.30", usecols=0)[1:] #Nbody time


n = 0
for i in range(0,241,20):
    data = h5.File(f'../data_files/snap.40_{i}.h5part','r')
    for j in range(0,100,10):
        coord = ss.Coordinates(data,j)
        center = coord.shrinking_sphere()
        x_rel = (coord.x-center[0])/1000 # convert to kpc
        y_rel = (coord.y-center[1])/1000

        plt.figure()
        plt.scatter(x[n]+x_rel,y[n]+y_rel,marker='.', s=0.5, color='g',label="Time: %s Myrs"%(n*2))
        plt.plot(0,0,'rx')
        plt.xlim(-15,15)
        plt.ylim(-15,15)
        plt.xlabel('x (kpc)')
        plt.ylabel('y (pkc)')
        plt.legend()
        plt.savefig("../visuals/pic%03d.png"%n,dpi=250)
        plt.close()
        n+=1
