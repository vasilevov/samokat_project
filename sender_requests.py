import requests
import data
import config


#Запрос на создание нового заказа со стандартным телом
def post_create_new_order():
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=data.default_order_body,
                         headers=data.headers)

#Запрос на получение статуса заказа по трекинговому номеру track
def get_order_status(track):
    return requests.get(config.URL_SERVICE + config.GET_ORDER_PATH,
                        params={"t": track})
