import os
import requests

SHEETY_GET_ENDPOINT = os.environ["SHEETY_GET_ENDPOINT"]
SHEETY_POST_USER_ENDPOINT = os.environ["SHEETY_POST_USER_ENDPOINT"]


class DataManager:
    def __init__(self):
        self.sheety_get_endpoint = SHEETY_GET_ENDPOINT
        self.sheety_post_endpoint = SHEETY_POST_USER_ENDPOINT
        self.sheety_data = []

    def get_sheety_data(self):
        response = requests.get(url=self.sheety_get_endpoint)
        self.sheety_data = response.json()['sheet1']

    def put_sheety_data(self, row_id, iata_code):
        put_params = {
            'sheet1': {
                'iataCode': iata_code
            }
        }
        response = requests.put(url=f"{self.sheety_get_endpoint}/{row_id}", json=put_params)
        return response

    def post_user_data(self, first_name, last_name, email):
        post_params = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }

        response = requests.post(url=self.sheety_post_endpoint, json=post_params)
        return response
