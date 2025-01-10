import requests

database = {
    "users": {
        1: {
            "id": 1,
            "email": "sadeepa@gmail.com",
            "password": "Sadeepa@2004"
        },
        2: {
            "id": 2,
            "email": "dileepa@gmail.com",
            "password": "Dileepa@2004"
        }
    }
}


def get_user_from_db(user_id):
    return database.get(user_id)


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        return response.json()

    return requests.HTTPError
