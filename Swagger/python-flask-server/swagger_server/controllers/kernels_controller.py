import connexion
import six

from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.kernels import Kernels  # noqa: E501
from swagger_server import util, missions_true, create_dirdf
import os
import farmhash


def get_kernel_endpoints(mission, kernel):  # noqa: E501
    """List of the available endpoints for a given mission/kernel

     # noqa: E501

    :param mission:
    :type mission: str
    :param kernel:
    :type kernel: str

    :rtype: List[Endpoints]
    """
    endpoints = ['/newest', '/hash', '/year', '/files']
    return endpoints


def get_kernel_hash(mission, kernel):  # noqa: E501
    """Hash of a kernel for a given mission

     # noqa: E501

    :param mission:
    :type mission: str
    :param kernel:
    :type kernel: str

    :rtype: List[Hash]
    """
    data_dir = []

    get_kernels = '/app/{}'.format(missions_true[mission])

    for kern in os.listdir(get_kernels):
        if os.path.isfile(os.path.join(get_kernels, kern)):
            continue
        else:
            data_dir.append(kern)

    dataframe = create_dirdf('/app/{}/{}/data/{}/'.format(missions_true[mission], data_dir[0], kernel).strip())
    return "The hash of {} is: {}".format('/app/{}/{}/data/{}/'.format(missions_true[mission], data_dir[0], kernel), str(farmhash.hash64((str(dataframe.values)))))


def get_kernels(mission):  # noqa: E501
    """List of available kernels for a given mission

     # noqa: E501

    :param mission:
    :type mission: str

    :rtype: List[Kernels]
    """
    data_dir = []
    kerns = []
    get_kernels = '/app/{}'.format(missions_true[mission])

    for kern in os.listdir(get_kernels):
        if os.path.isfile(os.path.join(get_kernels, kern)):
            continue
        else:
            data_dir.append(kern)

    for kern in os.listdir('/app/{}/{}/data'.format(missions_true[mission], data_dir[0])):
        if os.path.isfile(os.path.join('/app/{}/{}/data'.format(missions_true[mission], data_dir[0]), kern)):
            continue
        else:
            kerns.append(kern)

    return kerns
