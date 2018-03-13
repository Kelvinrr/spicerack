import os.path
from flask import Flask
from flask import jsonify
import pandas as pd
import numpy as np
import farmhash

app = Flask(__name__)

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

@app.route('/sync')
def synchronize_directory():

    sync = configure()

    data = create_dirdf(sync[0].strip())
    facility = create_dirdf(sync[1].strip())


    dir1hash = farmhash.hash64(str(data.values))
    facilityhash = farmhash.hash64(str(facility.values))

    if dir1hash == facilityhash:
        return ("Directories '" + sync[0] + "' and '" + sync[1] + "' SYNCED")
        # return("Directories are identical")

    else:
        # print("Synchronizing Directories: rsync -av " + data.index.name + "/ " + data.index.name + "/")
        os.system("rsync -av " + sync[0] + ' ' + sync[1])
        return("SYNCED " + sync[0] + " " + "and" + " " + sync[1])

def configure():
    with open('/app/config.txt', 'r') as f:
        files = []
        for line in f:
            research = line.split(':')
            files.append(research[1].strip())
        return files

def create_dirdf(directory):
    if not os.path.exists(directory):
        print("Error: Directory '" + directory + "' does not exist.")
        return

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
