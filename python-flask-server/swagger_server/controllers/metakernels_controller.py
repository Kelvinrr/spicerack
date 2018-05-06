import connexion
import six

from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.models.raw import Raw  # noqa: E501
from swagger_server import util, sqlselect_command


def get_metakernel_info(mission, file):  # noqa: E501
    """Hash, Path and Links for a given metakernel file

     # noqa: E501

    :param mission: 
    :type mission: str
    :param file: 
    :type file: str

    :rtype: List[Filelist]
    """
    rows = sqlselect_command("SELECT * FROM SPICE WHERE Mission='{mn}' AND Kernel='mk' AND File='{fn}'".format(mn=mission, fn=file))
    if rows == []:
        return "Unable to find a file that matches mission ["+mission+"], kernel [mk], and filename ["+file+"]."
    file_info = sqlselect_dict(rows[0]) # there should only be one possible return for a select like this. if we want to catch edge cases, we can add sqlselect_dictarray(rows)

    file_info["links"] = []
    if file.endswith(('.lbl', '.txt')):
        file_info["links"].append("/raw")
        
    return file_info


def get_metakernels(mission):  # noqa: E501
    """List of available metakernels for a given mission

     # noqa: E501

    :param mission: 
    :type mission: str

    :rtype: List[Filelist]
    """
    rows = sqlselect_command("SELECT * FROM SPICE WHERE Mission='{mn}' AND Kernel='mk'".format(mn=mission))
    files = [row[2] for row in rows]
    return files


def get_mk_newest(mission):  # noqa: E501
    """Newest metakernel for a given mission

     # noqa: E501

    :param mission: 
    :type mission: str

    :rtype: List[Filelist]
    """
    return 'do some magic!'


def get_mk_raw(mission, file):  # noqa: E501
    """Raw contents of a given metakernel file

     # noqa: E501

    :param mission: 
    :type mission: str
    :param file: 
    :type file: str

    :rtype: List[Raw]
    """
    if not file.endswith(('.lbl', '.txt')): # TODO create a longer list of acceptable file exensions in __init__ and include it in each controller?
        return "We do not current support raw display for files not ending with a '.lbl' or a '.txt' extension."

    rows = sqlselect_command("SELECT * FROM SPICE WHERE Mission='{mn}' AND Kernel='mk' AND File='{fn}'".format(mn=mission, fn=file))
    if rows == []:
        return "Unable to find a file that matches mission ["+mission+"], kernel [mk], and filename ["+file+"]."

    path = rows[0][3] # we shouldnt ever have more than one file that would match the query, so we should? be fine directly indexing zero
    file = io.open(path+'/'+file, 'r').readlines()
    return file


def get_mk_year(mission, year):  # noqa: E501
    """List of available metakernels for a given mission and year

     # noqa: E501

    :param mission: 
    :type mission: str
    :param year: 
    :type year: int

    :rtype: List[Filelist]
    """
    return 'do some magic!'


def get_mk_year_newest(mission, year):  # noqa: E501
    """Newest metakernels for a given mission and year

     # noqa: E501

    :param mission: 
    :type mission: str
    :param year: 
    :type year: int

    :rtype: List[Filelist]
    """
    return 'do some magic!'


def get_mk_years(mission):  # noqa: E501
    """List of years represented in the versions of metakernels for a given mission

     # noqa: E501

    :param mission: 
    :type mission: str

    :rtype: List[Filelist]
    """
    return 'do some magic!'
