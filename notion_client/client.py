import requests

from constants import Constants


def send(request, notion_token, action, page_id):
    # check action and add path
    if action is 'page-create':
        return post_send(request, notion_token, Constants.NOTION_BASE_URL + 'pages')

    elif action is 'page-retrieve':
        return get_send(request, notion_token, Constants.NOTION_BASE_URL + 'pages/'+page_id)

    elif action is 'page-update':
        return patch_send(request, notion_token, Constants.NOTION_BASE_URL + 'pages/'+page_id)

    elif action is 'token':
        return post_send(request, notion_token, Constants.NOTION_BASE_URL + 'oauth/token')


def post_send(request, notion_token, url):
    return requests.post(url, json=request,
                             headers={"Authorization": 'Basic ' + notion_token,
                                      "Notion-Version": Constants.NOTION_VERSION})

def get_send(request, notion_token, url):
    return requests.get(url, json=request,
                                 headers={"Authorization": 'Basic ' + notion_token,
                                          "Notion-Version": Constants.NOTION_VERSION})

def patch_send(request, notion_token, url):
    return requests.patch(url, json=request,
                                headers={"Authorization": 'Basic ' + notion_token,
                                         "Notion-Version": Constants.NOTION_VERSION})
