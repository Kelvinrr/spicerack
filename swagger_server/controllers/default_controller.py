import connexion
import six

from swagger_server.models.metakernal import Metakernal  # noqa: E501
from swagger_server import util


def get_metakernel(mission, year, version=None):  # noqa: E501
    """Returns Kernels from query params

    Adds an item to the system # noqa: E501

    :param mission: 
    :type mission: str
    :param year: 
    :type year: str
    :param version: 
    :type version: str

    :rtype: Metakernal
    """
    return 'do some magic!'
