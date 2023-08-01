import configuration
import requests
import data

#Создание нового пользователя (получение authToken в ответе)
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)

#создание нового набора
def post_new_client_kit(kit_headers,kit_body):
    return requests.post((configuration.URL_SERVICE + configuration.CLIENT_KIT_PATH),
                         json=kit_body,
                         headers=kit_headers)