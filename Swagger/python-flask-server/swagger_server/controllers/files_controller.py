import connexion
import six

from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server import util


def get_file_by_year(mission, kernel, file):  # noqa: E501
    """Newest file for a given year

     # noqa: E501

    :param mission: Name of the mission
    :type mission: str
    :param kernel: Kernel type being viewed
    :type kernel: str
    :param file: Name of the file
    :type file: str

    :rtype: List[Hash]
    """
    return 'do some magic!'


def get_file_hash(mission, kernel, file):  # noqa: E501
    """Hash of file for a given mission/kernel

     # noqa: E501

    :param mission: Name of the mission
    :type mission: str
    :param kernel: Kernel type being viewed
    :type kernel: str
    :param file: Name of the file being hashed
    :type file: str

    :rtype: List[Hash]
    """
    return 'do some magic!'


def get_file_path(mission, kernel, file):  # noqa: E501
    """Filepath of a given file

     # noqa: E501

    :param mission: Name of the mission
    :type mission: str
    :param kernel: Kernel type being viewed
    :type kernel: str
    :param file: Name of the file being hashed
    :type file: str

    :rtype: List[Hash]
    """
    return 'do some magic!'


def get_file_raw(mission, kernel, file):  # noqa: E501
    """Raw contents of file for a given mission/kernel

     # noqa: E501

    :param mission: Name of the mission
    :type mission: str
    :param kernel: Kernel type being viewed
    :type kernel: str
    :param file: Name of the file being viewed
    :type file: str

    :rtype: List[File]
    """
    return 'do some magic!'


def get_file_year(mission, kernel, file):  # noqa: E501
    """Year for the given file

     # noqa: E501

    :param mission: Name of the mission
    :type mission: str
    :param kernel: Kernel type being viewed
    :type kernel: str
    :param file: Name of the file
    :type file: str

    :rtype: List[Hash]
    """
    return 'do some magic!'


def get_kernel_files(mission, kernel, file):  # noqa: E501
    """List of available files for a given mission/kernel

     # noqa: E501

    :param mission: Name of the mission
    :type mission: str
    :param kernel: Kernel type being viewed
    :type kernel: str
    :param file: Name of the file being hashed
    :type file: str

    :rtype: List[Hash]
    """
    return 'do some magic!'
