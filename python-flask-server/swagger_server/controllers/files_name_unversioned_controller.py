import connexion
import six
import re
import sqlite3


from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server import util


def get_fn_newest(mission, kernel, name):  # noqa: E501
    """Newest version of a given file

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str
    :param name: 
    :type name: str

    :rtype: List[Filelist]
    """
    split = name.split('.')
    if len(split) < 2:
        return "Incompatible file name ["+name+"]. Make sure that the name does not include version number and does include a file extension."
    regex = split[0] + '%' + split[1] 

    conn = sqlite3.connect('/spicedata/.spicedb.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM SPICE WHERE Mission='{mn}' AND Kernel='{kn}' AND File LIKE '{fn}'".format(mn=mission, kn=kernel, fn=regex))
    rows = c.fetchall()
    conn.close()

    if rows == []:
        return "Unable to find a file that matches mission ["+mission+"], kernel ["+kernel+"], and filename regex ["+regex+"]."
    return rows[0][5]


def get_fn_year(mission, kernel, name, year):  # noqa: E501
    """Newest version of a given file

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str
    :param name: 
    :type name: str
    :param year: 
    :type year: int

    :rtype: List[Filelist]
    """
    return 'do some magic!'


def get_fn_year_newest(mission, kernel, name, year):  # noqa: E501
    """Newest file for a given year

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str
    :param name: 
    :type name: str
    :param year: 
    :type year: int

    :rtype: List[Filelist]
    """
    return 'do some magic!'
