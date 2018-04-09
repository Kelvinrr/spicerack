import connexion
import six

from swagger_server.models.metakernels import Metakernels  # noqa: E501
from swagger_server import util


def find_meta_kernels_by_mission(mission):  # noqa: E501
    """List of available metakernels for a given mission

     # noqa: E501

    :param mission: Name of the missions
    :type mission: str

    :rtype: List[Metakernels]
    """
    return 'do some magic!'


def find_meta_kernels_by_mission_new(mission):  # noqa: E501
    """List of available metakernels for a given mission, sorted by newest

     # noqa: E501

    :param mission: Name of the missions
    :type mission: str

    :rtype: List[Metakernels]
    """
    return 'do some magic!'


def find_meta_kernels_by_mission_year(mission, year):  # noqa: E501
    """List of available metakernels for a given mission and year

     # noqa: E501

    :param mission: Name of the missions
    :type mission: str
    :param year: Year to be searched
    :type year: int

    :rtype: List[Metakernels]
    """
    return 'do some magic!'


def find_meta_kernels_by_mission_year_new(mission, year):  # noqa: E501
    """List of available metakernels for a given mission and year, sorted by newest

     # noqa: E501

    :param mission: Name of the missions
    :type mission: str
    :param year: Year to be searched
    :type year: int

    :rtype: List[Metakernels]
    """
    return 'do some magic!'
