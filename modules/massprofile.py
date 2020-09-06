import numpy as np
import matplotlib.pyplot as plt
import h5py as h5
import shrinking_sphere as ss

def mass_at(data,step,ax,color='b',label=""):
    coord = ss.Coordinates(data,step)
    center = coord.shrinking_sphere()
    origin = np.array(center)
    data.close()
    # array of distance of each particle from CoM
    distance = np.sqrt((coord.x-origin[0])**2+(coord.y-origin[1])**2+(coord.z-origin[2])**2)
    bins = np.linspace(0,200,60) #starts at 0 because it's the distance from the center, last is the distance at the edge
    N,d = np.histogram(distance, bins=bins, weights=coord.m) # returns an array of  sums in each bin, d is the bin position number
    rightBinEdge = bins[1:] # [1:] starts at index 1
    ax.plot(rightBinEdge,N,color,label=label)
    ax.set_xlabel("radius (pc)")
    ax.set_ylabel("M(r)")
    ax.grid(True)
    if label != "":
        ax.legend()

def mass_cumulative(data,step,ax,color='b',label=""):
    coord = ss.Coordinates(data,step)
    center = coord.shrinking_sphere()
    data.close()
    origin = np.array(center)
    distance = np.sqrt((coord.x-origin[0])**2+(coord.y-origin[1])**2+(coord.z-origin[2])**2)
    bins = np.linspace(0,200,60) #starts at 0 because it's the distance from the center, last is the distance at the edge
    N,d = np.histogram(distance, bins=bins, weights=coord.m)  # returns an array of  sums in each bin, d is the bin position number
    N_cumulative = np.cumsum(N)
    rightBinEdge = bins[1:] # [1:] starts at index 1
    ax.plot(rightBinEdge,N_cumulative,color,label=label)
    ax.set_xlabel("radius (pc)")
    ax.set_ylabel("M(<r)")
    ax.grid(True)
    if label != "":
        ax.legend()
    return (np.interp(80,rightBinEdge,N_cumulative)/np.interp(10,rightBinEdge,N_cumulative))


#for actual iteration, precompute the distance of each star from CoM and set that to 'numbers'


# to find the center of bins
# bin_center = 0.5*(bins[1:]+bins[:-1])
# M(r) helps see where the bulk of the mass is contained

# half-mass radius (radius at which half the mass is contained)
# tidal radius - radius that defines the boundary of the globular cluster (where cumulative mass profile plateaus)
