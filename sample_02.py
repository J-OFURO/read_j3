#!/usr/bin/env python3
import netCDF4
import numpy as np
from j3 import misc

# sample 02: read Monthly, calculate average

# directory path to downloaded netCDF
data_path='../../J3_MON'

# variable name
var='NHF'
ver='V1.0'
tr='MONTHLY'
sr='HR'
yr='2002'

fname = misc.filename(var,tr,sr,ver,yr)
file=data_path + '/' + fname
print(file)

# open netCDF file
ncf = netCDF4.Dataset(file, 'r')

# print info
print(ncf.variables)

# define nhf
nhf = ncf.variables[var]

# List a nhf values at a point
print(nhf[:,359, 719])

# calculae average
print(np.average(nhf[:,359,718]))

# close netCDF file
ncf.close()
