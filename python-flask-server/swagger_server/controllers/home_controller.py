import connexion
import six
import farmhash

from swagger_server.models.dataframe import Dataframe  # noqa: E501
from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.update import Update  # noqa: E501
from swagger_server import util, populate_spicedb, sqlselect_command, sqlselect_dataframe

def get_home_endpoints():  # noqa: E501
    """List of available endpoints from home directory

     # noqa: E501


    :rtype: List[Endpoints]
    """
    return ["/hash", "/update", "/naif", "/missions", "/refresh", "/update"]


def get_home_hash():  # noqa: E501
    """Hash of the home dataframe

     # noqa: E5    :rtype: List[Hash]
    """
    rows = sqlselect_command("SELECT * FROM SPICE")
    df = sqlselect_dataframe(rows)
    return farmhash.hash64(str(df.values))


def refresh_db():  # noqa: E501
    """Refresh database of file info

     # noqa: E501


    :rtype: List[Update]
    """
    populate_spicedb()
