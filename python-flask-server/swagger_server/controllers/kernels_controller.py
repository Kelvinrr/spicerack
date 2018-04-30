import connexion
import six

from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.kernels import Kernels  # noqa: E501
from swagger_server import util


def get_kernel_endpoints(mission, kernel):  # noqa: E501
    """List of the available endpoints for a given mission/kernel

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str

    :rtype: List[Endpoints]
    """
    return 'do some magic!'


def get_kernel_hash(mission, kernel):  # noqa: E501
    """Hash of a kernel for a given mission

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str

    :rtype: List[Hash]
    """
    return 'do some magic!'


def get_kernels(mission):  # noqa: E501
    """List of available kernels for a given mission

     # noqa: E501

    :param mission: 
    :type mission: str

    :rtype: List[Kernels]
    """
    return 'do some magic!'
