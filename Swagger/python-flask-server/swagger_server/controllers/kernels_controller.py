import connexion
import six

from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.kernels import Kernels  # noqa: E501
from swagger_server import util


def find_kernels_by_mission(mission):  # noqa: E501
    """List of available kernels for a given mission

     # noqa: E501

    :param mission: Name of the missions
    :type mission: str

    :rtype: List[Kernels]
    """
    return 'do some magic!'


def get_kernel_endpoints(mission, kernel):  # noqa: E501
    """List of the next available endpoints for a given mission/kernel

     # noqa: E501

    :param mission: Name of the missions
    :type mission: str
    :param kernel: Kernel type being hashed
    :type kernel: str

    :rtype: List[Kernels]
    """
    return 'do some magic!'


def get_kernel_hash(mission, kernel):  # noqa: E501
    """Hash of a kernel for a given mission

     # noqa: E501

    :param mission: Name of the missions
    :type mission: str
    :param kernel: Kernel type being hashed
    :type kernel: str

    :rtype: List[Hash]
    """
    return 'do some magic!'
