import os
import json
from spacetrack import SpaceTrackClient
import spacetrack.operators as op

credentials_file = "credentials.JSON"
config_file = "config.JSON"

def get_info(file):
    with open(file, "r") as details:
        return json.load(details)


credentials = get_info(credentials_file)
api_user = credentials["identity"]
api_passkey = credentials["password"]

config = get_info(config_file)
User = config["User"]
Project = config["Project"]
country = config["country"]
object_type = config["object_type"]
orderby = config["orderby"]

st = SpaceTrackClient(api_user, api_passkey)

satdata = st.satcat(
        # country=country,
        # object_type=object_type,
        decay=None,
        orderby=orderby,
        apogee=op.greater_than(1000),
        perigee=op.less_than(500),
        rcs_size=op.not_equal('small'),
        limit=1,
        format='json'
)

if not os.path.exists(os.path.join(User, Project)):
    os.mkdir(f'{User}/{Project}')

with open(f'{User}/{Project}/data.JSON', 'w') as datadump:
    json.dump(json.loads(satdata), datadump, indent=4)