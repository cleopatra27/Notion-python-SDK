from oauth import connect


def oauth():
    x = connect(NOTION_CLIENT_ID, REDIRECT_URL,STATE)
    print(x)


oauth()
