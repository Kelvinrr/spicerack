import connexion
import six

from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server import util


def get_file_endpoints(mission, kernel, file):  # noqa: E501
    """List of available endpoints for a given versioned file

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str
    :param file: 
    :type file: str

    :rtype: List[Endpoints]
    """
    return 'do some magic!'


def get_file_hash(mission, kernel, file):  # noqa: E501
    """Hashed contents of a given versioned file

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str
    :param file: 
    :type file: str

    :rtype: List[Hash]
    """
    return 'do some magic!'


def get_file_path(mission, kernel, file):  # noqa: E501
    """Filepath of a given versioned file

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str
    :param file: 
    :type file: str

    :rtype: List[Filelist]
    """
    return 'do some magic!'


def get_file_raw(mission, kernel, file):  # noqa: E501
    """Raw contents of a given versioned file

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str
    :param file: 
    :type file: str

    :rtype: List[Hash]
    """
    return 'do some magic!'


def get_files(mission, kernel):  # noqa: E501
    """List of available files for a given mission/kernel

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str

    :rtype: List[Filelist]
    """
    return 'do some magic!'


def get_kernels_newest(mission, kernel):  # noqa: E501
    """Newest files for a given mission/kernel

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str

    :rtype: List[Filelist]
    """
    return 'do some magic!'
