import sender_stand_request
import data

#Создание пользователя и получение токена
def create_new_user():
   user_body = data.user_body.copy()
   response = sender_stand_request.post_new_user(user_body)
   assert response.status_code == 201
   assert response.json()["authToken"] != ""
   return response.json()["authToken"]

#Получение заголовка Authorization для набора
def get_header_kit(auth_token):
    current_header = data.headers_kit.copy()
    current_header["Authorization"] = "Bearer " + auth_token
    return current_header

#Получение тела запроса на создание Набора
def get_kit_body(name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.name_kit.copy()
    # изменение значения в поле name
    current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_body

# Создание Набор пользователя
def create_new_kit(auth_token,kit_body):
    kit_headers = get_header_kit(auth_token)
    return sender_stand_request.post_new_client_kit(kit_headers, kit_body)

#Позитивная проверка
def positive_assert(kit_name):
    authToken = create_new_user()
    kit_body = get_kit_body(kit_name)
    kit_response = create_new_kit(authToken, kit_body)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken, и оно не пустое
    assert kit_response.json()["name"] == kit_name

#Негативная проверка
def negative_assert_code_400(kit_name):
    authToken = create_new_user()
    kit_body = get_kit_body(kit_name)
    kit_response = create_new_kit(authToken, kit_body)

    # Проверка, что код ответа равен 400
    assert kit_response.status_code == 400
    # Проверка, что в теле ответа атрибут "code" равен 400
    assert kit_response.json()["code"] == 400
    # Проверка текста в теле ответа в атрибуте "message"
    assert kit_response.json()["message"] == "Не все необходимые параметры были переданы"

#Тесты ===============================================================================

#Тест №1
def test_create_kit_1_letter_in_name_get_success_response_201():
    positive_assert("a")

#Тест №2
def test_create_kit_511_letters_in_name_get_success_response_201():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Тест №3
def test_create_kit_0_letter_in_name_get_bad_request_400():
    negative_assert_code_400("")

#Тест №4
def test_create_kit_512_letter_in_name_get_bad_request_400():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Тест №5
def test_create_kit_english_letters_in_name_get_success_response_201():
    positive_assert("QWErty")

#Тест №6
def test_create_kit_russians_letters_in_name_get_success_response_201():
    positive_assert("Мария")

#Тест №7
def test_create_kit_special_symbols_in_name_get_success_response_201():
    positive_assert('"№%@",')

#Тест №8
def test_create_kit_spaces_in_name_get_success_response_201():
        positive_assert(" Человек и КО ")

#Тест №9
def test_create_kit_numbers_in_name_get_success_response_201():
    positive_assert("123")

#Тест №10
def test_create_kit_without_parameter_in_name_get_bad_request_400():
    name_kit = data.name_kit.copy()
    name_kit.pop("name")
    negative_assert_code_400(name_kit)

#Тест №11
def test_create_kit_parameter_type_number_in_name_get_bad_request_400():
    negative_assert_code_400(123)