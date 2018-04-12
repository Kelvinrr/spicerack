import connexion
import six

from swagger_server.models.dataframe import Dataframe  # noqa: E501
from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.update import Update  # noqa: E501
from swagger_server import util, configure, create_dirdf, make_user_ip_filepath_dict
from flask import jsonify
import farmhash
import os


def get_home_dataframe():  # noqa: E501
    """Dataframe of the home directory in JSON

     # noqa: E501


    :rtype: List[Dataframe]
    """
    user, ip, filepath = configure()
    home = make_user_ip_filepath_dict(user, ip, filepath)
    dataframe = create_dirdf('/spicedata')
    df_json = dataframe.to_json(orient='index')
    return df_json


def get_home_endpoints():  # noqa: E501
    """List of available endpoints from home directory

     # noqa: E501


    :rtype: List[Endpoints]
    """
    endpoints = ['/dataframe', '/naif', '/missions', '/hash', '/update', '/refresh']
    return jsonify(Endpoints=endpoints)


def get_home_hash():  # noqa: E501
    """Hash of the home dataframe

     # noqa: E501


    :rtype: List[Hash]
    """
    users, ip, filepath = configure()
    users_info = make_user_ip_filepath_dict(users, ip, filepath)
    filepath = os.listdir(users_info['Home'][1].strip())
    dataframe = create_dirdf(users_info['Home'][1].strip())
    return farmhash.hash64(str(dataframe.values))


def refresh_db():  # noqa: E501
    """Refresh database of file info

     # noqa: E501


    :rtype: List[Update]
    """
    return 'do some magic!'
