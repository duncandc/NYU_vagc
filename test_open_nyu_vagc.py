#!/usr/bin/python

#Author: Duncan Campbell
#Written: August 14, 2013
#Yale University
#Description: Read in hdf5 CFHTLS photo-z catalogues and print out names

###packages###
import numpy as np
import h5py
import sys

def main():
  ###make sure to change these when running in a new enviorment!###
  #location of data directory
  filepath = '/scratch/dac29/output/processed_data/NYU_VAGC/'
  #################################################################

  filename = 'nyu_vagc_dr7'

  print filename
  f =  h5py.File(filepath+filename+'.hdf5', 'r')
  dset = f.get(filename)

  print 'number of objects:', len(dset)
  print dset.dtype.names #columns in table
  

if __name__ == '__main__':
  main()
