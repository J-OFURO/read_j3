#!/usr/bin/env python3
from netCDF4 import MFDataset
import numpy as np
from j3 import misc

# sample 06: read Monthly, calculate average

# directory path to downloaded netCDF
data_path='../../J3_MON'

# variable name
var='NHF'
ver='V1.0'
tr='MONTHLY'
sr='HR'
yr='*'

fname = misc.filename(var,tr,sr,ver,yr)
file=data_path + '/' + fname
print(file)

nf = MFDataset("../../J3_MON/J-OFURO3_NHF_V1.0_MONTHLY_HR_200*.nc")
