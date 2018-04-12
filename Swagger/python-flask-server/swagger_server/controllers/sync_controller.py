import connexion
import six

from swagger_server.models.update import Update  # noqa: E501
from swagger_server import util, configure
from flask import jsonify
import os



def get_ssh_key(user):  # noqa: E501
    """Returns public SSH key

     # noqa: E501

    :param user: Get Public SSH Key
    :type user: str

    :rtype: List[Update]
    """
    return jsonify(SSH = os.popen('cat /root/.ssh/id_rsa.pub').read())



def list_nodes():  # noqa: E501
    """List of available nodes

     # noqa: E501


    :rtype: object
    """
    users, ip, filepath = configure()
    return jsonify(Nodes = users)


def next_places(user):  # noqa: E501
    """List of the next available endpoints for a given node

     # noqa: E501

    :param user: See where a user can navigate to next
    :type user: str

    :rtype: List[Update]
    """
    endpoints = ['/ssh', '/sync']
    return endpoints


def sync_nodes(user):  # noqa: E501
    """Synchronize data with another node

     # noqa: E501

    :param user: Sync with that user
    :type user: str

    :rtype: List[Update]
    """
    users, ip, filepath = configure()
    users_info = make_user_ip_filepath_dict(users, ip, filepath)

    rsync(users_info['Home'][1], user, users_info[user][0], users_info[user][1])
    return("SYNCED " + users_info['Home'][1] + " " + "and" + " " + users_info[user][1])

def rsync(SRC, USER, IP, DEST):
    os.system("rsync -avP {}@{}:{} {}".format(USER, IP, DEST, SRC))

def make_user_ip_filepath_dict(user, ip, filepath):
    zipped = list(zip(ip, filepath))
    return dict(zip(user, zipped))
