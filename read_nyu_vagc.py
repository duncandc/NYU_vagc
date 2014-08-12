#!/usr/bin/python

#Author: Duncan Campbell
#Written:  August 14, 2013
#Yale University
#Description: Read in ascii CFHTLS photo-z catalogues and save as HDF5 files.
#data from: ftp://ftpix.iap.fr/pub/CFHTLS-zphot-T0007/

###packages###
import sys
import glob
import gc
import h5py
import custom_utilities as cu
from astropy.io import fits
import os
import fnmatch
import numpy as np

def main():
    filepath = cu.get_data_path() + 'NYU_VAGC/'
    savepath = cu.get_output_path() + 'processed_data/NYU_VAGC/'

    filenames = os.listdir('/scratch/dac29/data/NYU_VAGC/')
    filenames = fnmatch.filter(filenames, '*.fits')

    '''
    #turn each catalogue into an hdf5 file
    for filename in filenames:
        print 'reading in:', filename
        hdulist = fits.open(filepath+filename)
        data = hdulist[1].data
        print 'saving as:', filename[:-5]+'.hdf5'
        f = h5py.File(savepath+filename[:-5]+'.hdf5', 'w')
        dset = f.create_dataset(filename[:-5], data=data)
        f.close()
        gc.collect()
        print 'done.'
    '''

    catalogues = ['kcorrect.none.model.z0.10','kcorrect.nearest.petro.z0.10',\
                  'kcorrect.nearest.model.z0.10','kcorrect.none.petro.z0.10',\
                  'object_catalog','object_sdss_imaging','object_sdss_spectro',\
                  'sersic_catalog', 'collisions.none', 'collisions.nearest']

    catalogue='object_catalog'
    f1 =  h5py.File(savepath+catalogue+'.hdf5', 'r')
    dset1 = f1.get(catalogue)
    catalogue='object_sdss_imaging'
    f2 =  h5py.File(savepath+catalogue+'.hdf5', 'r')
    dset2 = f2.get(catalogue)
    catalogue='object_sdss_spectro'
    f3 =  h5py.File(savepath+catalogue+'.hdf5', 'r')
    dset3 = f3.get(catalogue)
    catalogue='kcorrect.none.model.z0.10'
    f4 =  h5py.File(savepath+catalogue+'.hdf5', 'r')
    dset4 = f4.get(catalogue)
    catalogue='kcorrect.none.petro.z0.10'
    f5 =  h5py.File(savepath+catalogue+'.hdf5', 'r')
    dset5 = f5.get(catalogue)
    catalogue='kcorrect.nearest.model.z0.10'
    f6 =  h5py.File(savepath+catalogue+'.hdf5', 'r')
    dset6 = f6.get(catalogue)
    catalogue='kcorrect.nearest.petro.z0.10'
    f7 =  h5py.File(savepath+catalogue+'.hdf5', 'r')
    dset7 = f7.get(catalogue)
    catalogue='sersic_catalog'
    f8 =  h5py.File(savepath+catalogue+'.hdf5', 'r')
    dset8 = f8.get(catalogue)
    catalogue='collisions.none'
    f9 =  h5py.File(savepath+catalogue+'.hdf5', 'r')
    dset9 = f9.get(catalogue)
    catalogue='collisions.nearest'
    f10 =  h5py.File(savepath+catalogue+'.hdf5', 'r')
    dset10 = f10.get(catalogue)
    
    dset1_descr = dset1.dtype.descr
    dset2_descr = dset2.dtype.descr
    dset3_descr = dset3.dtype.descr
    dset4_descr = dset4.dtype.descr
    dset5_descr = dset5.dtype.descr
    dset6_descr = dset6.dtype.descr
    dset7_descr = dset7.dtype.descr
    dset8_descr = dset8.dtype.descr
    dset9_descr = dset9.dtype.descr
    dset10_descr = dset10.dtype.descr

    #KCORRECT and ABS mags
    d1 = (dset4.dtype.descr[7][0]+'_u.none.model.z0.10',dset4.dtype.descr[7][1])
    d2 = (dset4.dtype.descr[7][0]+'_g.none.model.z0.10',dset4.dtype.descr[7][1])
    d3 = (dset4.dtype.descr[7][0]+'_r.none.model.z0.10',dset4.dtype.descr[7][1])
    d4 = (dset4.dtype.descr[7][0]+'_i.none.model.z0.10',dset4.dtype.descr[7][1])
    d5 = (dset4.dtype.descr[7][0]+'_z.none.model.z0.10',dset4.dtype.descr[7][1])
    d6 = (dset4.dtype.descr[5][0]+'_u.none.model.z0.10',dset4.dtype.descr[5][1])
    d7 = (dset4.dtype.descr[5][0]+'_g.none.model.z0.10',dset4.dtype.descr[5][1])
    d8 = (dset4.dtype.descr[5][0]+'_r.none.model.z0.10',dset4.dtype.descr[5][1])
    d9 = (dset4.dtype.descr[5][0]+'_i.none.model.z0.10',dset4.dtype.descr[5][1])
    d10 = (dset4.dtype.descr[5][0]+'_z.none.model.z0.10',dset4.dtype.descr[5][1])
    #KCORRECT and ABS mags
    d11 = (dset5.dtype.descr[7][0]+'_u.none.petro.z0.10',dset5.dtype.descr[7][1])
    d12 = (dset5.dtype.descr[7][0]+'_g.none.petro.z0.10',dset5.dtype.descr[7][1])
    d13 = (dset5.dtype.descr[7][0]+'_r.none.petro.z0.10',dset5.dtype.descr[7][1])
    d14 = (dset5.dtype.descr[7][0]+'_i.none.petro.z0.10',dset5.dtype.descr[7][1])
    d15 = (dset5.dtype.descr[7][0]+'_z.none.petro.z0.10',dset5.dtype.descr[7][1])
    d16 = (dset5.dtype.descr[5][0]+'_u.none.petro.z0.10',dset5.dtype.descr[5][1])
    d17 = (dset5.dtype.descr[5][0]+'_g.none.petro.z0.10',dset5.dtype.descr[5][1])
    d18 = (dset5.dtype.descr[5][0]+'_r.none.petro.z0.10',dset5.dtype.descr[5][1])
    d19 = (dset5.dtype.descr[5][0]+'_i.none.petro.z0.10',dset5.dtype.descr[5][1])
    d20 = (dset5.dtype.descr[5][0]+'_z.none.petro.z0.10',dset5.dtype.descr[5][1])
    #KCORRECT and ABS mags
    d21 = (dset6.dtype.descr[7][0]+'_u.nearest.model.z0.10',dset6.dtype.descr[7][1])
    d22 = (dset6.dtype.descr[7][0]+'_g.nearest.model.z0.10',dset6.dtype.descr[7][1])
    d23 = (dset6.dtype.descr[7][0]+'_r.nearest.model.z0.10',dset6.dtype.descr[7][1])
    d24 = (dset6.dtype.descr[7][0]+'_i.nearest.model.z0.10',dset6.dtype.descr[7][1])
    d25 = (dset6.dtype.descr[7][0]+'_z.nearest.model.z0.10',dset6.dtype.descr[7][1])
    d26 = (dset6.dtype.descr[5][0]+'_u.nearest.model.z0.10',dset6.dtype.descr[5][1])
    d27 = (dset6.dtype.descr[5][0]+'_g.nearest.model.z0.10',dset6.dtype.descr[5][1])
    d28 = (dset6.dtype.descr[5][0]+'_r.nearest.model.z0.10',dset6.dtype.descr[5][1])
    d29 = (dset6.dtype.descr[5][0]+'_i.nearest.model.z0.10',dset6.dtype.descr[5][1])
    d30 = (dset6.dtype.descr[5][0]+'_z.nearest.model.z0.10',dset6.dtype.descr[5][1])
    #KCORRECT and ABS mags
    d31 = (dset7.dtype.descr[7][0]+'_u.nearest.petro.z0.10',dset7.dtype.descr[7][1])
    d32 = (dset7.dtype.descr[7][0]+'_g.nearest.petro.z0.10',dset7.dtype.descr[7][1])
    d33 = (dset7.dtype.descr[7][0]+'_r.nearest.petro.z0.10',dset7.dtype.descr[7][1])
    d34 = (dset7.dtype.descr[7][0]+'_i.nearest.petro.z0.10',dset7.dtype.descr[7][1])
    d35 = (dset7.dtype.descr[7][0]+'_z.nearest.petro.z0.10',dset7.dtype.descr[7][1])
    d36 = (dset7.dtype.descr[5][0]+'_u.nearest.petro.z0.10',dset7.dtype.descr[5][1])
    d37 = (dset7.dtype.descr[5][0]+'_g.nearest.petro.z0.10',dset7.dtype.descr[5][1])
    d38 = (dset7.dtype.descr[5][0]+'_r.nearest.petro.z0.10',dset7.dtype.descr[5][1])
    d39 = (dset7.dtype.descr[5][0]+'_i.nearest.petro.z0.10',dset7.dtype.descr[5][1])
    d40 = (dset7.dtype.descr[5][0]+'_z.nearest.petro.z0.10',dset7.dtype.descr[5][1])

    d_sersic = (dset8.dtype.descr[2][0]+'_r',dset7.dtype.descr[5][1])

    dtype = np.dtype([dset1_descr[0],dset1_descr[1],dset1_descr[2],dset10_descr[3],dset3_descr[28],\
                      dset10_descr[9],dset10_descr[7],dset3_descr[37],dset3_descr[38],dset3_descr[0],d_sersic,\
                      d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,\
                      d21,d22,d23,d24,d25,d26,d27,d28,d29,d30,d31,d32,d33,d34,d35,d36,d37,d38,d39,d40])
    N_columns = len(dtype)
    i=0
    print ' ' 
    for name in dtype.descr: 
        print i, name
        i=i+1
   
    data = np.recarray((len(dset1), ), dtype=dtype)

    data[data.dtype.descr[0][0]] = dset1[data.dtype.descr[0][0]] #ID
    data[data.dtype.descr[1][0]] = dset1[data.dtype.descr[1][0]] #ra
    data[data.dtype.descr[2][0]] = dset1[data.dtype.descr[2][0]] #dec

    data[data.dtype.descr[3][0]] = dset10[data.dtype.descr[3][0]] #z 
    data[data.dtype.descr[4][0]] = dset3[data.dtype.descr[4][0]]  #zerr
    data[data.dtype.descr[5][0]] = dset10[data.dtype.descr[5][0]] #ztype
    data[data.dtype.descr[6][0]] = dset10[data.dtype.descr[6][0]] #neighbor used
    data[data.dtype.descr[7][0]] = dset3[data.dtype.descr[7][0]]  #vdisp
    data[data.dtype.descr[8][0]] = dset3[data.dtype.descr[8][0]]  #vdisperr
    data[data.dtype.descr[9][0]] = dset3[data.dtype.descr[9][0]]  #SDSS_SPECTRO_TAG

    x=np.column_stack(dset8['SERSIC_N'])
    data[data.dtype.descr[10][0]] = x[0] #N_sersic r_band

    y=np.column_stack(dset4['KCORRECT'])
    x=np.column_stack(dset4['ABSMAG'])
    for i in range(0,5): #7-11 + 3 etc...
        print i, data.dtype.descr[i+7+4][0]
        data[data.dtype.descr[i+7+4][0]] = y[i]
    for i in range(0,5): #12-16
        print i, data.dtype.descr[i+12+4]
        data[data.dtype.descr[i+12+4][0]] = x[i]
    y=np.column_stack(dset5['KCORRECT'])
    x=np.column_stack(dset5['ABSMAG'])
    for i in range(0,5): #17-21
        print i, data.dtype.descr[i+17+4]
        data[data.dtype.descr[i+17+4][0]] = y[i]
    for i in range(0,5): #22-26
        print i, data.dtype.descr[i+22+4]
        data[data.dtype.descr[i+22+4][0]] = x[i]
    y=np.column_stack(dset6['KCORRECT'])
    x=np.column_stack(dset6['ABSMAG'])
    for i in range(0,5): #27-31
        print i, data.dtype.descr[i+27+4]
        data[data.dtype.descr[i+27+4][0]] = y[i]
    for i in range(0,5): #32-36
        print i, data.dtype.descr[i+32+4]
        data[data.dtype.descr[i+32+4][0]] = x[i]
    y=np.column_stack(dset7['KCORRECT'])
    x=np.column_stack(dset7['ABSMAG'])
    for i in range(0,5): #37-41
        print i, data.dtype.descr[i+37+4]
        data[data.dtype.descr[i+37+4][0]] = y[i]
    for i in range(0,5): #42-46
        print i, data.dtype.descr[i+42+4]
        data[data.dtype.descr[i+42+4][0]] = x[i]

    #save the resultant table
    filename = 'nyu_vagc_dr7'
    f = h5py.File(savepath+filename+'.hdf5', 'w')
    dset = f.create_dataset(filename, data=data)
    f.close()
    


    
    



if __name__ == '__main__':
    main()
