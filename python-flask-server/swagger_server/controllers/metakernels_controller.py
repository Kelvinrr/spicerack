import connexion
import six

from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.models.raw import Raw  # noqa: E501
from swagger_server import util


def get_metakernel_dict(mission, file):  # noqa: E501
    """Hash, Path and Links for a given metakernel file

     # noqa: E501

    :param mission: 
    :type mission: str
    :param file: 
    :type file: str

    :rtype: List[Filelist]
    """
    return 'do some magic!'


def get_metakernels(mission):  # noqa: E501
    """List of available metakernels for a given mission

     # noqa: E501

    :param mission: 
    :type mission: str

    :rtype: List[Filelist]
    """
    return 'do some magic!'


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
    return 'do some magic!'


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
