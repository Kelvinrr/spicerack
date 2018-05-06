import os
import io
import pandas as pd
import numpy as np
import farmhash
import time
import sqlite3
import json
import glob
import re
from datetime import datetime

# we only support the ros-e_m_a_c-spice-6-v1.0 directory for rosetta, there is another that exists in the naif db, 
# but it isnt used to populate our spicedb as we dont expect users to use that directory
missions_readable = {   "clem1-l-spice-6-v1.0"       : "clementine",
                        "co-s_j_e_v-spice-6-v1.0"    : "cassini_orbiter",
                        "dawn-m_a-spice-6-v1.0"      : "dawn",
                        "di-c-spice-6-v1.0"          : "deep_impact",
                        "dif-c_e_x-spice-6-v1.0"     : "epoxi",
                        "ds1-a_c-spice-6-v1.0"       : "deep_space_1",
                        "grail-l-spice-6-v1.0"       : "grail",
                        "hay-a-spice-6-v1.0"         : "hayabusa",
                        "jno-j_e_ss-spice-6-v1.0"    : "juno",
                        "lro-l-spice-6-v1.0"         : "lunar_reconnaissance_orbiter",
                        "mer1-m-spice-6-v1.0"        : "mer_1",
                        "mer2-m-spice-6-v1.0"        : "mer_2",
                        "mess-e_v_h-spice-6-v1.0"    : "messenger",
                        "mex-e_m-spice-6-v1.0"       : "mars_express",
                        "mgs-m-spice-6-v1.0"         : "mars_global_surveyor",
                        "mro-m-spice-6-v1.0"         : "mars_reconnaissance_orbiter",
                        "msl-m-spice-6-v1.0"         : "mars_science_laboratory",
                        "near-a-spice-6-v1.0"        : "near",
                        "nh-j_p_ss-spice-6-v1.0"     : "new_horizons",
                        "ody-m-spice-6-v1.0"         : "mars_odyssey",
                        "ros-e_m_a_c-spice-6-v1.0"   : "rosetta", 
                        "sdu-c-spice-6-v1.0"         : "stardust",
                        "vco-v-spice-6-v1.0"         : "venus_climate_orbiter",
                        "vex-e_v-spice-6-v1.0"       : "venus_express",
                        "vo1_vo2-m-spice-6-v1.0"     : "viking_orbiter"   }

# Reverse mission translations (readable->true)
missions_true = {value: key for key, value in missions_readable.items()}


# Parses config file for user settings
def configure():
    with open('/swaggerapp/config.txt', 'r') as f:
        ip = []
        user = []
        filepath  = []
        for line in f:
            research = line.split(': ')
            ip.append(research[0].strip())
            research = line.split(' ')
            user.append(research[1].strip())
            filepath.append(research[2].strip())
        return user, ip, filepath


# returns filename of newest kernel version
def newest_kernel(path, name):
    split = name.split('.')
    ext = split[-1]
    if re.search('_v[0-9]+', name):
        split = name.split('_v')
    elif re.search('v[0-9]+', name):
        split = name.split('v')
        
    # path/to/file/fname*.ext
    regex = path + '/' + split[0] + '*.' + ext 
    # glob returns filenames in alphabetical order, we can assume the last will be the highest version
    newest = glob.glob(regex)[-1]
    return newest.rsplit('/', 1)[1] # we just want the filename, as newest versions always exist in same dir as eachother


# indexes all kernel files from the /spicedata directory
# fileinfo stored in /spicedata/.spicedb.sqlite
# this method is called at the end of this init file
def populate_spicedb():

    # trash the old db bc its faster than comparing values and updating
    if os.path.exists('/spicedata/.spicedb.sqlite'):
        os.remove('/spicedata/.spicedb.sqlite')
        
    # database format will be: | Mission | Kernel | File | Path | Hash | Newest |
    conn = sqlite3.connect('/spicedata/.spicedb.sqlite')
    c = conn.cursor()
    c.execute("CREATE TABLE SPICE (Mission TEXT, Kernel TEXT, File TEXT, Path TEXT, Hash TEXT, Newest TEXT )")
    
    # we expect a specific directory structure: /spicedata/{mission}/{weirddir}/data/{kernel}/{file}
    print(datetime.now().strftime("%H:%M:%S") + ' - Begin Indexing of SPICE data from /spicedata directory')
    for root, subdir, files in os.walk('/spicedata'):
        for name in files:
            if name[0] == '.': # skip hidden files
                continue

            # full split format will be: ['', 'spicedata', 'clem1-l-spice-6-v1.0', 'clsp_1000', 'data', 'ck']
            split = root.split('/') 
            # not sure how this will react to having both rosettas...
            if len(split)>=6 and (split[5] in ['ck', 'ek', 'fk', 'spk', 'sclk', 'lsk', 'ik', 'pck', 'mk']): # we only care about kernel and mk files, which are always 4 dirs down 

                # issue: cant be sure that the -info.txt file will read first.... print could happen in the middle of the kernel directory
                if name.endswith('info.txt'): # we can expect a single ckinfo.txt, mkinfo.txt, etc in every kernel directory
                    print(datetime.now().strftime("%H:%M:%S") + ' - Indexing Kernel [' + split[5] + '] for Mission [' + missions_readable[split[2]] + ']')
                    continue 
                newest = newest_kernel(root, name)
                fhash = farmhash.hash64(str(io.open(root+'/'+name,'rb').read())) # spice data encoding is mixed, so read as binary
                c.execute("INSERT OR IGNORE INTO SPICE (Mission, Kernel, File, Path, Hash, Newest) VALUES ('{mn}', '{kn}', '{fn}', '{fp}', '{fh}', '{new}')"
                          .format(mn=missions_readable[split[2]], kn=split[5], fn=name, fp=root, fh=fhash, new=newest))
            # misc files    
            elif len(split) >= 4:
                fhash = farmhash.hash64(str(io.open(root+'/'+name,'rb').read())) # spice data encoding is mixed, so read as binary
                c.execute("INSERT OR IGNORE INTO SPICE (Mission, Kernel, File, Path, Hash, Newest) VALUES ('{mn}', 'misc', '{fn}', '{fp}', '{fh}', '{new}')"
                          .format(mn=missions_readable[split[2]], fn=name, fp=root, fh=fhash, new=name))
            
    conn.commit()
    conn.close()
    print(datetime.now().strftime("%H:%M:%S") + ' - Finished Indexing of SPICE data, fileinfo stored in /spicedata/.spicedb.sqlite')


def sqlselect_dictarray(sql_rows):
    dicts = []
    for row in sql_rows:
        dicts.append(sqlselect_dict(row))
    return dicts

# converts a SQL SELECT return format into an array of dicts
def sqlselect_dict(row):
    return {'mission': row[0],
            'kernel' : row[1],
            'file'   : row[2],
            'path'   : row[3],
            'hash'   : row[4],
            'newest' : row[5]}

def sqlselect_command(command):
    conn = sqlite3.connect('/spicedata/.spicedb.sqlite')
    c = conn.cursor()
    c.execute(command)
    rows = c.fetchall()
    conn.close()
    return rows

# takes a sql select output and creates a pandas dataframe
def sqlselect_dataframe(rows):
    df = pd.DataFrame(columns = ["mission", "kernel", "file", "path", "hash", "newest"])
    for i in range(len(rows)):
        df.loc[i] = rows[i]
    return df


def make_user_ip_filepath_dict(user, ip, filepath):
    zipped = list(zip(ip, filepath))
    return dict(zip(user, zipped))

populate_spicedb()
