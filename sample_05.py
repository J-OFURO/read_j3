#!/usr/bin/env python3
import netCDF4
import numpy as np
import j3

# sample 05: read MON
# with cordinate variable

# directory path to downloaded netCDF
data_path='../../J3_MON'

# Data set info.
var='NHF'
ver='V1.0'
tr='MONTHLY'
sr='HR'
yr='2002'

# fname
fname = j3.misc.filename(var,tr,sr,ver,yr)
file=data_path + '/' + fname
print(file)

# open netCDF file
ncf = netCDF4.Dataset(file, 'r')

# print info
print(ncf.variables)

# read variables
nhf = ncf.variables[var]
lon = ncf.variables['longitude']
lat = ncf.variables['latitude']
time = ncf.variables['time']

# List a nhf values at a point
i=719
j=359

l=0
while l <= 11:
 print( time[l],lon[i],lat[j], nhf[l,j,i] )
 l += 1

# close netCDF file
ncf.close()
