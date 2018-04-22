import connexion
import six

from swagger_server.models.dataframe import Dataframe  # noqa: E501
from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.update import Update  # noqa: E501
from swagger_server import util


def get_home_dataframe():  # noqa: E501
    """Dataframe of the home directory in JSON

     # noqa: E501


    :rtype: List[Dataframe]
    """
    return 'do some magic!'


def get_home_endpoints():  # noqa: E501
    """List of available endpoints from home directory

     # noqa: E501


    :rtype: List[Endpoints]
    """
    return 'do some magic!'


def get_home_hash():  # noqa: E501
    """Hash of the home dataframe

     # noqa: E501


    :rtype: List[Hash]
    """
    return 'do some magic!'


def refresh_db():  # noqa: E501
    """Refresh database of file info

     # noqa: E501


    :rtype: List[Update]
    """
    return 'do some magic!'
