import sender_requests

def test_check_order_by_track_number():
    new_order = sender_requests.post_create_new_order() #запрос на создание заказа
    track_number = new_order.json()["track"] #сохранение номера трека заказа
    response = sender_requests.get_order_status(track_number) #запрос на получения заказа по треку заказа
    assert response.status_code == 200 #проверка, что код ответа равен 200