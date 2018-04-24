import os
import io
import pandas as pd
import numpy as np
import farmhash
import time
import sqlite3
import json


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


# the good one
def populate_spicedb():
    
    if os.path.exists('/spicedata/.spicedb.sqlite'):
        os.remove('/spicedata/.spicedb.sqlite')
        
    # atm we only use one table in the database - mostly just for storage -> quick access
    # database format will be: | Mission | Kernel | File | Path | Hash | Newest |
    conn = sqlite3.connect('/spicedata/.spicedb.sqlite')
    c = conn.cursor()
    c.execute("CREATE TABLE SPICE (Mission TEXT, Kernel TEXT, File TEXT, Path TEXT, Hash TEXT, Newest INTEGER )")
    
    for root, subdir, files in os.walk('/spicedata'):
        for name in files: 
            if name[0] == '.':
                continue

            split = root.split('/') # indexes inside the docker container will be one more, as we start at root and split on '/'
            if len(split) >=5 and (split[4] in ['data', 'extras']):
                fhash = farmhash.hash64(str(io.open(root+'/'+name,'rb').read())) # spice data encoding is mixed, so read as binary
                c.execute("INSERT OR IGNORE INTO SPICE (Mission, Kernel, File, Path, Hash, Newest) VALUES ('{mn}', '{kn}', '{fn}', '{fp}', '{fh}', {new})"
                          .format(mn=missions_readable[split[2]], kn=split[5], fn=name, fp=root, fh=fhash, new=0))
            
    conn.commit()
    conn.close()
    print('Finished Indexing of SPICE data, stored in /spicedata/.spicedb.sqlite')


#
# Your scientists were so preoccupied with whether or not they could, they didn’t stop to think if they should
# this is terrible  ~ ~ ~ ~ ~ ~
#
# populates spice database with file info starting from /spicedata
# the spice database will be a hidden file: /spicedata/.spicedb.sqlite
# TODO: if a file is deleted, it should be removed from the db... but would that require confirming that all files still exist?
# ALSO: if we are reading the whole file as binary and hashing anyways, maybe we should just delete the whole db and repopulate every time???
#       there isnt a lot of value to knowing that we have changed a hash.. unless we want to report that the file has changed,
#       which i think we can assume the user would know about
def populate_spicedb_ugly():

    # atm we only use one table in the database - mostly just for storage -> quick access
    # database format will be: | Mission | Kernel | File | Path | Hash | Newest |
    conn = sqlite3.connect('/spicedata/.spicedb.sqlite')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS SPICE (Mission TEXT, Kernel TEXT, File TEXT, Path TEXT, Hash TEXT, Newest INTEGER )")

    # ooh spicy loops ~ maybe we should just os.walk this
    # we expect a specific directory structure: /spicedata/{mission}/data/{kernel}/{file}
    print('Begin Indexing of SPICE data from /spicedata directory')
    for mis in [m for m in os.listdir('/spicedata') if not m[0] == '.']:
        for ker in [k for k in os.listdir('/spicedata/'+mis+'/data') if not k[0] == '.']:
            print('Indexing Kernel [' + ker +  '] for Mission [' + missions_readable[mis] + ']')
            for file in [f for f in os.listdir('/spicedata/'+mis+'/data/'+ker) if not f[0] == '.']:

                fpath = '/spicedata/'+mis+'/data/'+ker+'/'
                if os.path.isdir(fpath+file): # cant hash a directory... although we arent expecting any at this level
                    continue
                fhash = farmhash.hash64(str(io.open(fpath+file,'rb').read())) # spice data encoding is mixed, so read as binary

                # check if the file already exists for a certain mission and kernel
                # if it already exists, we want to update the hash, otherwise, we insert the full row
                c.execute("SELECT * FROM SPICE WHERE Mission='{mn}' AND Kernel='{kn}' AND File='{fn}'".format(mn=missions_readable[mis], kn=ker, fn=file))
                row = c.fetchall()
                if row != []:
                    if row[0][4] != fhash:
                        c.execute("UPDATE SPICE SET Hash = '{hn}' WHERE Mission ='{mn}' AND Kernel='{kn}' AND File='{fn}'".format(hn=fhash, mn=missions_readable[mis], kn=ker, fn=file))
                else:
                    c.execute("INSERT OR IGNORE INTO SPICE (Mission, Kernel, File, Path, Hash, Newest) VALUES ('{mn}', '{kn}', '{fn}', '{fp}', '{fh}', {new})"
                          .format(mn=missions_readable[mis], kn=ker, fn=file, fp=fpath, fh=fhash, new=0))

        # grab metakernel files: /spicedata/{mission}/extras/mk/{file}... same process (Is there a way to combine regular kernels and metakernels logic?)
        print('Indexing Metakernels for Mission [' + missions_readable[mis] + ']')
        for file in [f for f in os.listdir('/spicedata/'+mis+'/extras/mk') if not file[0] == '.']:

            fpath = '/spicedata/'+mis+'/extras/mk/'
            if os.path.isdir(fpath+file):
                    continue
            fhash = farmhash.hash64(str(io.open(fpath+file,'rb').read()))

            # delish copypaste - pls get rid of me
            c.execute("SELECT * FROM SPICE WHERE Mission='{mn}' AND Kernel='mk' AND File='{fn}'".format(mn=missions_readable[mis], fn=file))
            row = c.fetchall()
            if row != []:
                if row[0][4] != fhash:
                    c.execute("UPDATE SPICE SET Hash = '{hn}' WHERE Mission ='{mn}' AND Kernel='mk' AND File='{fn}'".format(hn=fhash, mn=missions_readable[mis], fn=file))
            else:
                c.execute("INSERT OR IGNORE INTO SPICE (Mission, Kernel, File, Path, Hash, Newest) VALUES ('{mn}', '{kn}', '{fn}', '{fp}', '{fh}', {new})"
                      .format(mn=missions_readable[mis], kn='mk', fn=file, fp=fpath, fh=fhash, new=0))
            
    conn.commit()
    conn.close()
    print('Finished Indexing of SPICE data, stored in /spicedata/.spicedb.sqlite')


def create_dirdf(directory):
    if not os.path.exists(directory):
        return "Error: Directory '" + directory + "' does not exist."

    filenames = []
    hashvalues = []

    for root, subdir, files in os.walk(directory):
        for name in files:
            if not name[0] == ".": # ignore hidden files
                filepath = os.path.join(root, name)

                # hash full file contents
                # note: we dont know the encoding scheme for the spice data files, so we just read as binary
                # the labels and headers are all ascii, but the kernels are a mix of ascii and ???
                file = str(io.open(filepath,'rb').read())
                filenames.append(filepath.split(directory, 1)[1])
                hashvalues.append(farmhash.hash64(file))

                # parse file creation date
    df = pd.DataFrame(data=hashvalues, index = filenames, columns = ["Hash"])
    df.index.name = directory
    return df


def create_datedf(directory):
    if not os.path.exists(directory):
        return "Error: Directory '" + directory + "' does not exist."

    fnames = []
    dates = []

    for root, subdir, files in os.walk(directory):
        for name in files:
            if name.endswith(".lbl"): # only parse labels
                filepath = os.path.join(root, name)
                file = io.open(filepath,'r')
                line = file.readline()
                product_id = ""
                product_time = ""

                # check for file kernel being pointed to
                while line:
                    if line.startswith("PRODUCT_ID"):
                        product_id = line.split("= ")[1].strip()
                    if line.startswith("PRODUCT_CREATION_TIME"):
                        product_time = line.split("= ")[1].strip()
                    line = file.readline()

                if product_id and product_time:
                    fnames.append(product_id)
                    dates.append(product_time)

    df = pd.DataFrame(data=dates, index = fnames, columns = ["Hash"])
    df.index.name = directory
    return df


def make_user_ip_filepath_dict(user, ip, filepath):
    zipped = list(zip(ip, filepath))
    return dict(zip(user, zipped))

populate_spicedb()
