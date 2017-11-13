#!/usr/bin/env python3
#
# read.py
#----------------------------------------------------------------------- 
def data(ncf, var):
   data = ncf.variables[var][:]
   return(data)

def unit(ncf, var):
   test = ncf.variables[var]
   unit = test.units
   return(unit)
 
   
    

   
