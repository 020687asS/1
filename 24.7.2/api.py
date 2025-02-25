import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"
    def get_api_key(self, email: str, password: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса в формате JSON с уникальным ключем пользователя, найденного по указанным email и паролем"""
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key',headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def get_list_of_pets(self, auth_key: json, filter: str="") -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON со списком найденных питомцев, совпадающих с фильтромюНа данный момент фильтр может иметь пустое значение - получить список всех питомцев, либо 'my_pets' - получить список собственных питомцев"""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets',headers=headers, params=filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def add_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON, позволяет добавить нового питомца в список Мои питомцы"""
        data = MultipartEncoder(fields= {
            'name': name,
            'animal_type': animal_type,
            'age': age,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/jpeg')
        })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def add_pet_photo(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Метод позволяет добавить фото к уже существующему питомцу"""
        data = MultipartEncoder(fields={
            'pet_id': pet_id,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/jpeg')
        })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets/set_photo/'+pet_id , headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet_from_database(self, auth_key: json, pet_id: str) -> json:
        """Метод удаляет существующего питомца из списка Мои питомцы"""
        data = MultipartEncoder(fields={
            'pet_id': pet_id
        })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.delete(self.base_url + 'api/pets/'+ pet_id, headers=headers, data=data)
        status = res.status_code

        return status


    def update_information_about_pet(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: str) -> json:
        """Метод позволяет изменить данные питомца из списка Мои питомцы"""
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key['key']}
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

   