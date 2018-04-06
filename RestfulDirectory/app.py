import os.path
from flask import Flask
from flask import jsonify
import pandas as pd
import numpy as np
import farmhash
import pexpect
import sys

app = Flask(__name__)


missions_readable = {   "clem1-l-spice-6-v1.0"       : "Clementine",
                        "co-s_j_e_v-spice-6-v1.0"    : "Cassini Orbiter",
                        "dawn-m_a-spice-6-v1.0"      : "DAWN",
                        "di-c-spice-6-v1.0"          : "Deep Impact",
                        "dif-c_e_x-spice-6-v1.0"     : "EPOXI",
                        "ds1-a_c-spice-6-v1.0"       : "Deep Space 1",
                        "grail-l-spice-6-v1.0"       : "GRAIL",
                        "hay-a-spice-6-v1.0"         : "Hayabusa",
                        "jno-j_e_ss-spice-6-v1.0"    : "JUNO",
                        "lro-l-spice-6-v1.0"         : "Lunar Reconnaissance Orbiter",
                        "mer1-m-spice-6-v1.0"        : "MER 1 (Opportunity)",
                        "mer2-m-spice-6-v1.0"        : "MER 2 (Spirit)",
                        "mess-e_v_h-spice-6-v1.0"    : "Messenger",
                        "mex-e_m-spice-6-v1.0"       : "Mars Express",
                        "mgs-m-spice-6-v1.0"         : "Mars Global Surveyor",
                        "mro-m-spice-6-v1.0"         : "Mars Reconnaissance Orbiter",
                        "msl-m-spice-6-v1.0"         : "Mars Science Laboratory",
                        "near-a-spice-6-v1.0"        : "NEAR",
                        "nh-j_p_ss-spice-6-v1.0"     : "New Horizons",
                        "ody-m-spice-6-v1.0"         : "Mars Odyssey",
                        "ro_rl-e_m_a_c-spice-6-v1.0" : "Rosetta",
                        "ros-e_m_a_c-spice-6-v1.0"   : "Rosetta", # Nothing matching this on naif website
                        "sdu-c-spice-6-v1.0"         : "Stardust",
                        "vco-v-spice-6-v1.0"         : "Venus Climate Orbiter",
                        "vex-e_v-spice-6-v1.0"       : "Venus Express",
                        "vo1_vo2-m-spice-6-v1.0"     : "Viking Oribiter"}

# Reverse mission dictionary (readable->true)
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

# @app.route('/sync')
# def synchronize_directory():
#
#     ip, user, filepath = configure()
#
#     #data = create_dirdf(sync[0].strip())
#     #facility = create_dirdf(sync[1].strip())
#
#
#     #dir1hash = farmhash.hash64(str(data.values))
#     #facilityhash = farmhash.hash64(str(facility.values))
#
#     # if dir1hash == facilityhash:
#     #     return ("Directories '" + sync[0] + "' and '" + sync[1] + "' SYNCED")
#     #     # return("Directories are identical")
#     #
#     # else:
#     #     # print("Synchronizing Directories: rsync -av " + data.index.name + "/ " + data.index.name + "/")
#     rsync(filepath[0], user[1], ip[1], filepath[1])
#     return("SYNCED " + filepath[0] + " " + "and" + " " + filepath[1])

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
    os.system("rsync -avP" + SRC + ' ' + USER + '@' + IP + ':' + DEST)


def configure():
    with open('config.txt', 'r') as f:
        ip = []
        user = []
        filepath  = []
        for line in f:
            research = line.split(': ')
            ip.append(research[0].strip())
            #print(research[0])

            research = line.split(' ')
            #print(research[1])
            user.append(research[1].strip())

            #print(research[2])
            filepath.append(research[2].strip())

        # print(ip)
        # print(user)
        # print(filepath)


        return user, ip, filepath

def make_user_ip_filepath_dict(user, ip, filepath):
    zipped = list(zip(ip, filepath))
    new_dict = dict()
    new_dict = dict(zip(user, zipped))

    return new_dict

# @app.route('/df')
def create_dirdf(directory):
    # if not os.path.exists(directory):
    #     return("Error: Directory '" + directory + "' does not exist.")

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
