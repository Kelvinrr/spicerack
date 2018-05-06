import connexion
import six
import farmhash

from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.kernels import Kernels  # noqa: E501
from swagger_server import util, sqlselect_command, sqlselect_dataframe


def get_kernel_info(mission, kernel):  # noqa: E501
    """List of the available endpoints for a given mission/kernel

     # noqa: E501

    :param mission: 
    :type mission: str
    :param kernel: 
    :type kernel: str

    :rtype: List[Endpoints]
    """
    rows = sqlselect_command("SELECT * FROM SPICE WHERE Mission='{mn}' AND Kernel='{kn}'".format(mn=mission, kn=kernel))
    if rows == []:
        return "Unable to find a match for mission ["+mission+"] and kernel ["+kernel+"]."
    df = sqlselect_dataframe(rows)
    kernel_info = { 'mission' : mission,
                    'kernel'  : kernel,
                    'hash'    : farmhash.hash64(str(df.values)),
                    'links'   : ["/files"]}

    return kernel_info


def get_kernels(mission):  # noqa: E501
    """List of available kernels for a given mission

     # noqa: E501

    :param mission: 
    :type mission: str

    :rtype: List[Kernels]
    """
    # this could honestly be hardcoded ??? - kernels dont change, and we dont expect anyone to 
    rows = sqlselect_command("SELECT Kernel FROM SPICE WHERE Mission = '{mn}'".format(mn=mission))
    if rows == []:
        return "Unable to find a match for mission ["+mission+"]."
    kernels = []
    for row in rows:
        for kern in row:
            kernels.append(kern) 

    return list(set(kernels)) # what
