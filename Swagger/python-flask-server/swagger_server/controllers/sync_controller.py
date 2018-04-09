import connexion
import six
import os
from swagger_server.models.update import Update  # noqa: E501
from swagger_server import util
from swagger_server import configure
from flask import jsonify




def get_public_ssh(user):  # noqa: E501
    """Public SSH Key of User

     # noqa: E501

    :param user: Return SSH Public Key
    :type user: str

    :rtype: List[Update]
    """
    return jsonify(SSH = os.popen('cat /root/.ssh/id_rsa.pub').read())


def list_nodes():  # noqa: E501
    """List of available nodes

     # noqa: E501


    :rtype: List[Update]
    """

    users, ip, filepath = configure()
    return jsonify(Nodes = users)


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
    return("SYNCED " + users_info['Home'][0] + " " + "and" + " " + users_info[user][1])

def rsync(SRC, USER, IP, DEST):
    os.system("rsync -avP " + SRC + ' ' + USER + '@' + IP + ':' + DEST)

def make_user_ip_filepath_dict(user, ip, filepath):
    zipped = list(zip(ip, filepath))
    return dict(zip(user, zipped))
