KPL/MK

   This meta-kernel lists a subset of kernels from the meta-kernel
   clem_v01.tm provided in the data set CLEM1-L-SPICE-6-V1.0,
   covering the whole or a part of the customer requested time period
   from 1994-01-26T00:00:00.000 to 1994-05-07T00:00:00.000.

   The documentation describing these kernels can be found in the
   complete data set available at this URL

   ftp://naif.jpl.nasa.gov/pub/naif/pds/data/clem1-l-spice-6-v1.0/clsp_1000

   To use this meta-kernel users may need to modify the value of the
   PATH_VALUES keyword to point to the actual location of the data
   set's ``data'' directory on their system. Replacing ``/'' with ``\''
   and converting line terminators to the format native to the user's
   system may also be required if this meta-kernel is to be used on a
   non-UNIX workstation.

   This meta-kernel was created by the NAIF node's SPICE PDS data set 
   subsetting service version 1.2 on Fri Apr  6 09:59:30 PDT 2018.

 
   \begindata
 
      PATH_VALUES     = (
                         './data'
                        )
 
      PATH_SYMBOLS    = (
                         'KERNELS'
                        )
 
      KERNELS_TO_LOAD = (
                         '$KERNELS/lsk/naif0008.tls'
                         '$KERNELS/pck/pck00008.tpc'
                         '$KERNELS/pck/moon_pa_de403_1950_2198.bpc'
                         '$KERNELS/sclk/clem_nom.tsc'
                         '$KERNELS/fk/clem_v20.tf'
                         '$KERNELS/fk/moon_060721.tf'
                         '$KERNELS/fk/moon_assoc_me.tf'
                         '$KERNELS/ik/clem_astar_006.ti'
                         '$KERNELS/ik/clem_bstar_006.ti'
                         '$KERNELS/ik/clem_cpt_002.ti'
                         '$KERNELS/ik/clem_hires_008.ti'
                         '$KERNELS/ik/clem_lidar_005.ti'
                         '$KERNELS/ik/clem_lwir_008.ti'
                         '$KERNELS/ik/clem_nir_009.ti'
                         '$KERNELS/ik/clem_uvvis_008.ti'
                         '$KERNELS/spk/de414.bsp'
                         '$KERNELS/spk/clem_nrl.bsp'
                         '$KERNELS/spk/clem_jpl.bsp'
                         '$KERNELS/ck/clem_act_ck3.bc'
                        )
 
   \begintext
 

