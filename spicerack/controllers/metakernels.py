import connexion
import six

from spicerack.models.metakernels import Metakernels  # noqa: E501
from spicerack import util


def get_metakernel(mission, year, version):  # noqa: E501
    """Get a specific kernel, or a set of kernels 

    Adds an item to the system # noqa: E501

    :param mission:
    :type mission: str
    :param year:
    :type year: str
    :param version:
    :type version: str

    :rtype: Metakernels
    """
    return 'do some magic!'
