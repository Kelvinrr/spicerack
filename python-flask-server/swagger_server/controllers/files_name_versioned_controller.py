import connexion
import six
import sqlite3
import io

from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server import util, sqlselect_dict


def get_file_info(mission, kernel, file):  # noqa: E501
    """List of available endpoints for a given versioned file

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str
    :param file: 
    :type file: str

    :rtype: List[Endpoints]
    """
    conn = sqlite3.connect('/spicedata/.spicedb.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM SPICE WHERE Mission='{mn}' AND Kernel='{kn}' AND File='{fn}'".format(mn=mission, kn=kernel, fn=file))
    rows = c.fetchall()
    conn.close()   
    if rows == []:
        return "Unable to find a file that matches mission ["+mission+"], kernel ["+kernel+"], and filename ["+file+"]."
    file_info = sqlselect_dict(rows[0]) # there should only be one possible return for a select like this. if we want to catch edge cases, we can add sqlselect_dictarray(rows)
    if file.endswith('.lbl'):
        file_info["links"] = ["/raw"]
    else:
        file_info["links"] = []

    return file_info


# this method's return is formatted as an array of strings, to make for better readability on the browser.
# if this is called from within another program, treat it as you called readlines() on the file
# TODO: fix how this displays special characters, i.e. "PRODUCT_ID                   = \"clem_act_ck3.bc\"\n" might be hard for users to parse
def get_file_raw(mission, kernel, file):  # noqa: E501
    """Raw contents of a given versioned file

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str
    :param file: 
    :type file: str

    :rtype: List[Hash]
    """
    if not file.endswith('.lbl'):
        return "We do not current support raw display for files not ending with a '.lbl' extension."

    conn = sqlite3.connect('/spicedata/.spicedb.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM SPICE WHERE Mission='{mn}' AND Kernel='{kn}' AND File='{fn}'".format(mn=mission, kn=kernel, fn=file))
    rows = c.fetchall()
    conn.close() 

    path = rows[0][3]
    file = io.open(path+'/'+file, 'r').readlines()
    return file

def get_files(mission, kernel):  # noqa: E501
    """List of available files for a given mission/kernel

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str

    :rtype: List[Filelist]
    """
    conn = sqlite3.connect('/spicedata/.spicedb.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM SPICE WHERE Mission='{mn}' AND Kernel='{kn}'".format(mn=mission, kn=kernel))
    rows = c.fetchall()
    conn.close() 

    files = [row[2] for row in rows]
    return files


def get_kernels_newest(mission, kernel):  # noqa: E501
    """Newest files for a given mission/kernel

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str

    :rtype: List[Filelist]
    """
    conn = sqlite3.connect('/spicedata/.spicedb.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM SPICE WHERE Mission='{mn}' AND Kernel='{kn}'".format(mn=mission, kn=kernel))
    rows = c.fetchall()
    conn.close() 

    # file = filename for row in sqlselect if filename == newest
    files = [row[2] for row in rows if row[2] == row[5]] # wow
    return files
