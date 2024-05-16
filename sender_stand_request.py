import configuration
import data
import requests

#создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_USER,
                         json=body,
                         headers=data.headers)

#создание нового набора
def post_new_client_kit(kit_body, auth_token):
    new_headers = data.headers_of_kits.copy()
    new_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_KIT,
                         json=kit_body,
                         headers=new_headers)

#получение токена для нового пользователя
def get_new_user_token(body):
    return post_new_user(body).json()["authToken"]