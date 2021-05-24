class OAuthTokenResponse:
    def __init__(self, access_token, workspace_name, workspace_icon, bot_id):
        self.access_token = access_token
        self.workspace_name = workspace_name
        self.workspace_icon = workspace_icon
        self.bot_id = bot_id