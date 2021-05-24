import client
from constants import Constants
import json
from typing import Text

responseType = "code"


def connect(clientID, redeirectURL, state) -> Text:
    """
        The first step in the OAuth process is to request authorization from a user. This is done by sending a user to the authorization URL. You may send the user to this URL with a simple hyperlink or a redirect from another request.
        :rtype: object
        :param clientID: An identifier for your integration, found in the integration settings
        :param redeirectURL: A URL where the user should return after granting access.
        :param state: if the user was in the middle of an interaction or operation, this parameter can be used to restore state after the user returns. It is also can be used to prevent CSRF attacks.
        """
    if state is not None:
        return Constants.NOTION_BASE_URL + Constants.NOTION_VERSION + "/oauth/authorize?client_id=" + clientID + "&redirect_uri=" + redeirectURL + "&response_type=" + responseType + "&state=" + state
    else:
        return Constants.NOTION_BASE_URL + Constants.NOTION_VERSION + "/oauth/authorize?client_id=" + clientID + "&redirect_uri=" + redeirectURL + "&response_type=" + responseType


def accesstoken(code, redirect_uri) -> Text:
    """
        :param code: A temporary authorization code - required
        :param redirect_uri: The "redirect_uri" that was provided in the Authorization step
        """
    x = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri
    }
    request = json.dumps(x)

    # send to client
    return client.send(request, "")
