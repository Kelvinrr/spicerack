import connexion
import six

from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.models.missions import Missions  # noqa: E501
from swagger_server import util, missions_true


def get_home_naif():  # noqa: E501
    """List of available missions in naif format

     # noqa: E501


    :rtype: List[Missions]
    """
    rows = sqlselect_command("SELECT Mission FROM SPICE")
    missions = []
    for row in rows:
        for mis in row:
            missions.append(missions_true[mis]) 

    return list(set(missions))


def get_misc(mission):  # noqa: E50
    """List of the available misc. files for a given mission

     # noqa: E501

    :param mission: 
    :type mission: str

    :rtype: List[Filelist]
    """
    return


def get_mission_endpoints(mission):  # noqa: E501
    """List of the available endpoints for a given mission

     # noqa: E501

    :param mission: 
    :type mission: str

    :rtype: List[Endpoints]
    """
    return 'do some magic!'


def get_missions():  # noqa: E501
    """List of available missions (Human-Readable)

     # noqa: E501


    :rtype: List[Missions]
    """
    rows = sqlselect_command("SELECT Mission FROM SPICE")
    missions = []
    for row in rows:
        for mis in row:
            missions.append(mis) 

    return list(set(missions))
