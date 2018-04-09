import connexion
import six

from swagger_server.models.missions import Missions  # noqa: E501
from swagger_server import util


def find_missio_endpoints(mission):  # noqa: E501
    """List of the next available endpoints for a given mission

    Get a listing of available kernel types by missions # noqa: E501

    :param mission: Name of the missions
    :type mission: str

    :rtype: List[Missions]
    """
    return 'do some magic!'


def get_naif_names():  # noqa: E501
    """List of available missions (NAIF technical names)

     # noqa: E501


    :rtype: List[Missions]
    """
    return 'do some magic!'
