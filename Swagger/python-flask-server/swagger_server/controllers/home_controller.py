import connexion
import six

from swagger_server.models.dataframe import Dataframe  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.missions import Missions  # noqa: E501
from swagger_server import util, configure, make_user_ip_filepath_dict, create_dirdf
from flask import jsonify
import farmhash
import os


def get_dataframe():  # noqa: E501
    """Dataframe of the home directory in JSON

     # noqa: E501


    :rtype: List[Dataframe]
    """

    user, ip, filepath = configure()
    home = make_user_ip_filepath_dict(user, ip, filepath)
    dataframe = create_dirdf(home['Home'][1].strip())
    df_json = dataframe.to_json(orient='index')
    return df_json


def get_hash():  # noqa: E501
    """Hash of the home dataframe

     # noqa: E501


    :rtype: List[Hash]
    """
    users, ip, filepath = configure()
    users_info = make_user_ip_filepath_dict(users, ip, filepath)
    dataframe = create_dirdf(users_info['Home'][1])
    return "The hash of {} is: {}".format(users_info['Home'][1], str(farmhash.hash64((str(dataframe.values)))))



def get_home_endpoints():  # noqa: E501
    """List of next available endpoints from home directory

     # noqa: E501


    :rtype: List[Dataframe]
    """

    endpoints = ['home/dataframe', '/home/naif', '/home/missions', '/home/hash', '/home/missions/naif']
    return jsonify(Endpoints=endpoints)


def get_naif():  # noqa: E501
    """List of available missions in naif format

     # noqa: E501


    :rtype: List[Hash]
    """
    return 'do some magic!'


def list_missions():  # noqa: E501
    """List of available missions (Human-Readable)

     # noqa: E501


    :rtype: List[Missions]
    """
    return 'do some magic!'
