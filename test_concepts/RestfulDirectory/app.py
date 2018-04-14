import os.path
from flask import Flask
from flask import jsonify
import pandas as pd
import numpy as np
import farmhash
import sys

app = Flask(__name__)

# Define translation table for human readable mission names
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
                        "ro_rl-e_m_a_c-spice-6-v1.0" : "rosetta",
                        "ros-e_m_a_c-spice-6-v1.0"   : "rosetta", # Nothing matching this on naif website
                        "sdu-c-spice-6-v1.0"         : "stardust",
                        "vco-v-spice-6-v1.0"         : "venus_climate_orbiter",
                        "vex-e_v-spice-6-v1.0"       : "venus_express",
                        "vo1_vo2-m-spice-6-v1.0"     : "viking_orbiter"}

# Reverse mission translations (readable->true)
missions_true = {value: key for key, value in missions_readable.items()}

# Creates a root based on your directory
@app.route('/')
def root_dir():  # pragma: no cover

    # Gets the directory the python file was executed
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Calls generate_routes() function on current directory
    return generate_routes(current_dir)


# Dynamically create routes based on the directory
@app.route('/show/<path:possible_file>')
def generate_routes(possible_file):
    file_paths = []
    actual_files = []

    # Checks each item in a directory to check if it is a file or directory
    for item in os.listdir(possible_file):
        if os.path.isfile(os.path.join(possible_file, item)):
            actual_files.append(item)
        else:
            file_paths.append(item)

    # Returns your directory laid out as directories and files
    return jsonify(Directories = file_paths, Files = actual_files)

# Lists all nodes that can be synced with
@app.route('/update/')
def update():
    users, ip, filepath = configure()
    return jsonify(Nodes = users)

@app.route('/ssh')
def ssh():
    return jsonify(SSH = os.popen('cat /ssh/id_rsa.pub').read())

@app.route('/update/<node>')
def pull(node):

    user, ip, filepath = configure()
    users_info = make_user_ip_filepath_dict(user, ip, filepath)

    rsync(users_info['Home'][1], node, users_info[node][0], users_info[node][1])
    return("SYNCED " + users_info['Home'][0] + " " + "and" + " " + users_info[node][1])


@app.route('/naif/<path:data>')
def naif_missions(data):
    missions = ["clem1-l-spice-6-v1.0", "co-s_j_e_v-spice-6-v1.0",
                "dawn-m_a-spice-6-v1.0", "di-c-spice-6-v1.0",
                "dif-c_e_x-spice-6-v1.0", "ds1-a_c-spice-6-v1.0",
                "grail-l-spice-6-v1.0", "hay-a-spice-6-v1.0",
                "jno-j_e_ss-spice-6-v1.0", "lro-l-spice-6-v1.0",
                "mer1-m-spice-6-v1.0", "mer2-m-spice-6-v1.0",
                "mess-e_v_h-spice-6-v1.0", "mex-e_m-spice-6-v1.0",
                "mgs-m-spice-6-v1.0", "mro-m-spice-6-v1.0",
                "msl-m-spice-6-v1.0", "near-a-spice-6-v1.0",
                "nh-j_p_ss-spice-6-v1.0", "ody-m-spice-6-v1.0",
                "ro_rl-e_m_a_c-spice-6-v1.0", "ros-e_m_a_c-spice-6-v1.0",
                "sdu-c-spice-6-v1.0", "vco-v-spice-6-v1.0",
                "vex-e_v-spice-6-v1.0", "vo1_vo2-m-spice-6-v1.0"]

    # Checks each item in a directory to check if it is a file or directory
    for item in os.listdir(data):
        if os.path.isfile(os.path.join(data, item)):
            pass
        else:
            missions.append(item)

    # Returns your directory laid out as directories and files
    return jsonify(Missions = missions)

@app.route('/missions/<data>')
def readable_missions(data):
    missions = []
    nair_names = []
    real_names = {"mro-m-spice-6-v1.0": "mars_resonnaissance_orbiter",
                  "Kernal2": "SomethingElse"}

    directories = {v: k for k, v in real_names.items()}


    nair_names.append('mro-m-spice-6-v1.0')
    # Checks each item in a directory to check if it is a file or directory
    for item in os.listdir(data):
        if os.path.isfile(os.path.join(data, item)):
            pass
        else:
            missions.append(real_names[item])

    # Returns your directory laid out as directories and files
    return jsonify(Missions = missions)

@app.route('/hash')
def hash_dataframe():
    user, ip, filepath = configure()
    home = make_user_ip_filepath_dict(user, ip, filepath)
    dataframe = create_dirdf(home['Home'][1].strip())
    #data = create_dirdf(dataframe[0].strip())

    return str(farmhash.hash64((str(dataframe.values))))

@app.route('/dataframe')
def make_df():
    user, ip, filepath = configure()
    home = make_user_ip_filepath_dict(user, ip, filepath)
    dataframe = create_dirdf(home['Home'][1].strip())
    df_json = dataframe.to_json(orient='index')
    return df_json

def rsync(SRC, USER, IP, DEST):
    os.system("rsync -avP " + SRC + ' ' + USER + '@' + IP + ':' + DEST)


# Parses config file for user settings
def configure():
    with open('config.txt', 'r') as f:
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

def make_user_ip_filepath_dict(user, ip, filepath):
    zipped = list(zip(ip, filepath))
    return dict(zip(user, zipped))

# @app.route('/df')
def create_dirdf(directory):

    filenames = []
    hashvalues = []

    for root, subdir, files in os.walk(directory):
        for name in files:
            if not name[0] == ".": # ignore hidden files
                filepath = os.path.join(root, name)
                # file = open(filepath).read()
                filenames.append(filepath.split(directory, 1)[1])
                with open(filepath, 'r') as file:
                    file = file.read()
                hashvalues.append(farmhash.hash64(file))
    df = pd.DataFrame(data=hashvalues, index = filenames, columns = ["Hash"])
    df.index.name = directory
    return df

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
