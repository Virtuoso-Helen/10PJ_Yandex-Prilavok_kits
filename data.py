#заголовок на создание набора
headers = {
    "Content-Type": "application/json"
}
#тело для создания нового пользователя
user_body = {
    "firstName": "Елена",
    "phone": "+79995553322",
    "address": "г. Москва, Останкино, д. 777"
}
#создание нового пользователя с токеном
headers_of_kits = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {authToken}"
}
#тело для создания нового набора
kit_body = {"name": "Вкусный набор"}