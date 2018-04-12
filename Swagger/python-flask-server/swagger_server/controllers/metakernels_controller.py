import connexion
import six

from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.raw import Raw  # noqa: E501
from swagger_server import util, missions_true, create_dirdf
import os
import farmhash


def get_metakernels(mission):  # noqa: E501
    """List of available metakernels for a given mission

     # noqa: E501

    :param mission:
    :type mission: str

    :rtype: List[Filelist]
    """
    data_dir = []
    kerns = []
    get_kernels = '/spicedata/{}'.format(missions_true[mission])

    for kern in os.listdir(get_kernels):
        if os.path.isfile(os.path.join(get_kernels, kern)):
            continue
        else:
            data_dir.append(kern)


    return os.listdir('/spicedata/{}/{}/extras/mk'.format(missions_true[mission], data_dir[0]))


def get_mk_hash(mission, file):  # noqa: E501
    """Hashed contents of a given metakernel file

     # noqa: E501

    :param mission:
    :type mission: str
    :param file:
    :type file: str

    :rtype: List[Hash]
    """
    data_dir = []
    kerns = []
    get_kernels = '/spicedata/{}'.format(missions_true[mission])

    for kern in os.listdir(get_kernels):
        if os.path.isfile(os.path.join(get_kernels, kern)):
            continue
        else:
            data_dir.append(kern)

    dataframe = create_dirdf('/spicedata/{}/{}/extras/mk/{}'.format(missions_true[mission], data_dir[0], file).strip())
    return "The hash of {} is: {}".format('/spicedata/{}/{}/extras/mk/{}'.format(missions_true[mission], data_dir[0], file), str(farmhash.hash64((str(dataframe.values)))))


def get_mk_newest(mission):  # noqa: E501
    """Newest metakernels for a given mission

     # noqa: E501

    :param mission:
    :type mission: str

    :rtype: List[Filelist]
    """
    return 'do some magic!'


def get_mk_path(mission, file):  # noqa: E501
    """Filepath of a given metakernel file

     # noqa: E501

    :param mission:
    :type mission: str
    :param file:
    :type file: str

    :rtype: List[Filelist]
    """
    return 'do some magic!'


def get_mk_raw(mission, file):  # noqa: E501
    """Raw contents of a given metakernel file

     # noqa: E501

    :param mission:
    :type mission: str
    :param file:
    :type file: str

    :rtype: List[Raw]
    """
    return 'do some magic!'


def get_mk_year(mission, year):  # noqa: E501
    """List of available metakernels for a given mission and year

     # noqa: E501

    :param mission:
    :type mission: str
    :param year:
    :type year: int

    :rtype: List[Filelist]
    """
    return 'do some magic!'


def get_mk_year_newest(mission, year):  # noqa: E501
    """Newest metakernels for a given mission and year

     # noqa: E501

    :param mission:
    :type mission: str
    :param year:
    :type year: int

    :rtype: List[Filelist]
    """
    return 'do some magic!'
