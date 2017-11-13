#!/usr/bin/env python3
# DAILY
# Calculate Annual average, standard deviation
#
import netCDF4
import numpy as np
import j3

# directory path to downloaded netCDF
data_path='../../J3_DAILY'

# 
var='NHF'
ver='V1.0'
tr='DAILY'
sr='HR'
yr='2002'

fname = j3.misc.filename(var,tr,sr,ver,yr)
file=data_path + '/' + fname
print(file)

# open netCDF file
ncf = netCDF4.Dataset(file, 'r')

# print info
print(ncf.variables)

# define variable
#nhf = ncf.variables[var][:]
nhf = j3.read.data(ncf,var)

# list variable info
print(nhf)

## list variable info:
print(nhf.shape)
print(nhf.units)
print(nhf.missing_value)

# list a nhf values at a point
#print(nhf[:,359, 719])
ave1=np.ma.average(nhf[:,359, 719])
ave2=np.average(nhf[:,359, 719])
print(ave1,ave2)

# ave and std over all axis
ave=np.ma.average(nhf)
print(ave)
std=np.ma.std(nhf)
print(std)

# ave and std over time axis
ave2d=np.ma.average(nhf, axis=0)
std2d=np.ma.std(nhf, axis=0)
ave2d.shape
std2d.shape

# close netCDF file
ncf.close()
