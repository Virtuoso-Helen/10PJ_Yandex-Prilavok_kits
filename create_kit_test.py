import sender_stand_request
import data

#замена значения name
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

#позитивная проверка
def positive_assert(name):
    user_token = sender_stand_request.get_new_user_token(data.user_body)
    kit_body = get_kit_body(name)
    kit_responce = sender_stand_request.post_new_client_kit(kit_body, user_token)
    assert kit_responce.status_code == 201
    assert kit_responce.json()["name"] == name

#негативная проверка
def negative_assert(name):
    user_token = sender_stand_request.get_new_user_token(data.user_body)
    kit_body = get_kit_body(name)
    kit_responce = sender_stand_request.post_new_client_kit(kit_body, user_token)
    assert kit_responce.status_code == 400

#1тест позитивный, допустимое количество символов (1):
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#2тест позитивный, допустимое количество символов (511):
def test_create_kit_511_letter_in_name_get_success_responce():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#3тест негативный, кол-во символов меньше допустимого (0):
def test_create_kit_0_symbol_in_name_get_mistake():
    negative_assert("")

#4тест негативный, кол-во символов больше допустимого (512)
def test_create_kit_512_symbol_in_name_get_mistake():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#5тест позитивный, допустимые символы (латиница)
def test_create_kit_eng_letter_in_name_get_success_response():
    positive_assert("QWErty")

#6тест позитивный, допустимые символы (кирилица)
def test_create_kit_rus_letter_in_name_get_success_response():
    positive_assert("Мария")

#7тест позитивный, допустимые символы (спецсимволы)
def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert(" \"№%@ \",")

#8тест позитивный, допустимые символы (пробел)
def test_create_kit_space_in_name_get_success_response():
    positive_assert("Человек и КО")

#9тест позитивный, разрешены цифры
def test_create_kit_number_get_success_response():
    positive_assert("12345")

#10тест негативный, проверка отсутсвия параметра
def test_create_kit_no_parameter_in_name_get_mistake():
    kit_body = {}
    user_token = sender_stand_request.get_new_user_token(data.user_body)
    kit_responce = sender_stand_request.post_new_client_kit(kit_body, user_token)
    assert kit_responce.status_code == 400

#11тест негативный, иной тип параметра (число)
def test_create_kit_different_parameter_type_in_name_get_mistake():
    negative_assert(123)