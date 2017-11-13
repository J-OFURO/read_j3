#!/usr/bin/env python3
import netCDF4
import numpy as np
import j3

# sample 01: read CLM
# directory path to downloaded netCDF
data_path='../../UPDATE/2017.05/J-OFURO3_CLM/DATA/V1.0'

# variable name
var='NHF'
ver='V1.0'
tr='CLM'
sr='HR'
yr=''

fname = j3.misc.filename(var,tr,sr,ver,yr)
file=data_path + '/' + fname
print(file)

# open netCDF file
ncf = netCDF4.Dataset(file, 'r')

# print info
print(ncf.variables)

# define nhf
nhf = j3.read.data(ncf,var)
nhf_unit = j3.read.unit(ncf,var)

# List a nhf values at a point
print(nhf[:,359, 719])
print(nhf_unit)

# close netCDF file
ncf.close()
