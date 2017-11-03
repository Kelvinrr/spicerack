import os.path
from flask import Flask
from flask import jsonify

app = Flask(__name__)

# Creates a root based on your directory
@app.route('/')
def root_dir():  # pragma: no cover

    # Gets the directory the python file was executed
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Calls generate_routes() function on current directory
    return generate_routes(current_dir)

# Dynamically create routes based on the directory
@app.route('/<path:possible_file>')
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
