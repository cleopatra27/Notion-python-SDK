# import requests
#
# from constants import Constants
#
#
# def send(request, MY_NOTION_TOKEN, action, page_id):
#     # check action and add path
#     if action is 'page-create':
#         url = Constants.NOTION_BASE_URL + 'pages'
#         response = requests.post(Constants.NOTION_BASE_URL, json=request,
#                                  headers={"Authorization": 'Basic ' + MY_NOTION_TOKEN,
#                                           "Notion-Version": Constants.NOTION_VERSION})
#     elif action is 'page-retrieve':
#         url = Constants.NOTION_BASE_URL + 'pages/'+page_id
#         response = requests.get(Constants.NOTION_BASE_URL, json=request,
#                                  headers={"Authorization": 'Basic ' + MY_NOTION_TOKEN,
#                                           "Notion-Version": Constants.NOTION_VERSION})
#     elif action is 'page-update':
#         url = Constants.NOTION_BASE_URL + 'pages/' + page_id
#         response = requests.patch(Constants.NOTION_BASE_URL, json=request,
#                                 headers={"Authorization": 'Basic ' + MY_NOTION_TOKEN,
#                                          "Notion-Version": Constants.NOTION_VERSION})
#     elif action is 'token':
#         url = Constants.NOTION_BASE_URL + 'oauth/' + page_id
#         response = requests.patch(Constants.NOTION_BASE_URL, json=request,
#                                 headers={"Authorization": 'Basic ' + MY_NOTION_TOKEN,
#                                          "Notion-Version": Constants.NOTION_VERSION})
#     return response
