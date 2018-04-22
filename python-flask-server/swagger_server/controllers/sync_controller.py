import connexion
import six

from swagger_server.models.update import Update  # noqa: E501
from swagger_server import util


def get_ssh_key(user):  # noqa: E501
    """Returns public SSH key

     # noqa: E501

    :param user: Get Public SSH Key
    :type user: str

    :rtype: List[Update]
    """
    return 'do some magic!'


def list_nodes():  # noqa: E501
    """List of available nodes

     # noqa: E501


    :rtype: object
    """
    return 'do some magic!'


def next_places(user):  # noqa: E501
    """List of the next available endpoints for a given node

     # noqa: E501

    :param user: See where a user can navigate to next
    :type user: str

    :rtype: List[Update]
    """
    return 'do some magic!'


def sync_nodes(user):  # noqa: E501
    """Synchronize data with another node

     # noqa: E501

    :param user: Sync with that user
    :type user: str

    :rtype: List[Update]
    """
    return 'do some magic!'
