 # makes calculations into the float type
from __future__ import division

import h5py as h5
import matplotlib.pyplot as plt
import numpy as np

class Coordinates:
    def __init__(self,data,step):
        self.data = data
        self.step = step
        self.x = data[f'Step#{step}/X1'][:]
        self.y = data[f'Step#{step}/X2'][:]
        self.z = data[f'Step#{step}/X3'][:]
        self.m = data[f'Step#{step}/M'][:]

    def shrinking_sphere(self,plot_y=False,plot_z=False,save=False):
        # initial center of mass
        xcom = np.dot(self.x,self.m)/np.sum(self.m)
        ycom = np.dot(self.y,self.m)/np.sum(self.m)
        zcom = np.dot(self.z,self.m)/np.sum(self.m)

        # initial origin, set it to another variable to store
        origin = np.array([xcom,ycom,zcom])
        initialOrigin = origin

        # set the longest distance in the x-coordinates as initial radius
        radius = self.x.max()-self.x.min()
        # want just 1% of particles
        minParticles = len(self.m)*0.01
        currentParticles = len(self.m)
        newx = self.x
        newy = self.y
        newz = self.z
        newm = self.m

        while (currentParticles>minParticles):
            # find CoM with filtered particles
            xcom = np.dot(newx,newm)/np.sum(newm)
            ycom = np.dot(newy,newm)/np.sum(newm)
            zcom = np.dot(newz,newm)/np.sum(newm)
            radius = radius*0.95
            origin = np.array([xcom,ycom,zcom])
            # want to find the distance between the coordinate and the new origin (new CoM)
            distance = np.sqrt((newx-origin[0])**2+(newy-origin[1])**2+(newz-origin[2])**2)
            # find array of indices where the distance of each particle is less than the new radius
            mask = np.where(distance<=radius)[0]
            newx = newx[mask]
            newy = newy[mask]
            newz = newz[mask]
            newm = newm[mask]
            currentParticles = len(newm)

        def plot_xy():
            plt.figure()
            plt.scatter(self.x,self.y,marker='.', s=0.5, color='g')
            plt.scatter(origin[0],origin[1],marker='x', s=10, color='magenta')
            plt.show()
        def plot_xz():
            plt.figure()
            plt.scatter(self.x,self.z,marker='.', s=0.5, color='g')
            plt.scatter(origin[0],origin[2],marker='x', s=10, color='red')
            plt.show()
        if plot_y:
            plot_xy()
        if plot_z:
            plot_xz()
        # if save:
        #

        return origin

# def coord(data,step):
#     x = data[f'Step#{step}/X1'][:]
#     y = data[f'Step#{step}/X2'][:]
#     z = data[f'Step#{step}/X3'][:]
#     m = data[f'Step#{step}/M'][:]
#     data.close()
#     return np.array([x,y,z,m])




#last_step = len(data.keys())-1
#'Step#%d'%(last_step)
# loop through the steps in each file
