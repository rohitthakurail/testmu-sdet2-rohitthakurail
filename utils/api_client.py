import requests
from config.settings import BASE_API_URL
import json

class APIClient:
    def get(self, endpoint):
        return requests.get(f"{BASE_API_URL}{endpoint}")

    def post(self, endpoint, payload):
        return requests.post(f"{BASE_API_URL}{endpoint}", json=payload)

    def put(self, endpoint, payload, headers):
        return requests.put(f"{BASE_API_URL}{endpoint}", json=payload, headers=headers)

    def delete(self, endpoint, headers):
        return requests.delete(f"{BASE_API_URL}{endpoint}", headers=headers)

    def load_api_data(self) -> dict:
        with open("data/api/api_data.json", "r") as file:
            data = json.load(file)
        return data

    def load_schemas(self) -> dict:
        with open("utils/schemas.json", "r") as file:
            schemas = json.load(file)
        return schemas

    def create_booking_id(self) -> int:
        """
        api to create a booking        :return:  id int
        """
        payload = self.load_api_data()["create_booking_data"]
        return self.post('/booking', payload).json()['bookingid']

    def create_admin_headers(self) -> dict:
        """
        Method to create headers with auth token
        :return: headers dict
        """
        admin_payload = self.load_api_data()["admin_credentials"]
        token = self.post('/auth', admin_payload).json()['token']
        headers = {"Content-Type": "application/json",
                   'Accept': 'application/json',
                   'Cookie': f'token={token}'}
        return headers
