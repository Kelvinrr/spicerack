import connexion
import six

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
    return 'do some magic!'


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
