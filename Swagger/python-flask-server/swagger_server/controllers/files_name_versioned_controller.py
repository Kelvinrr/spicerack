import connexion
import six

from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server import util, missions_true, create_dirdf
import os


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
    endpoints = ['/raw', '/hash', '/filepath', '/newest']
    return endpoints


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
    data_dir = []
    get_kernels = '/app/{}'.format(missions_true[mission])

    for kern in os.listdir(get_kernels):
        if os.path.isfile(os.path.join(get_kernels, kern)):
            continue
        else:
            data_dir.append(kern)
    with open('/app/{}/{}/data/{}/{}'.format(missions_true[mission], data_dir[0], kernel, file)) as f:
        return f.read()

def get_files(mission, kernel):  # noqa: E501
    """List of available files for a given mission/kernel

     # noqa: E501

    :param mission:
    :type mission: str
    :param kernel:
    :type kernel: str

    :rtype: List[Filelist]
    """
    data_dir = []
    files = []
    get_kernels = '/app/{}'.format(missions_true[mission])

    for kern in os.listdir(get_kernels):
        if os.path.isfile(os.path.join(get_kernels, kern)):
            continue
        else:
            data_dir.append(kern)

    for kern in os.listdir('/app/{}/{}/data/{}'.format(missions_true[mission], data_dir[0], kernel)):
        if kern[0] == '.':
            continue
        else:
            files.append(kern)

    return files


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
