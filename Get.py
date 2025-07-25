import requests

class Get:

    def __init__(self, id):
        self.baseUrl = "https://api.restful-api.dev/objects"
        self.id = id

    def get_api(self, id):
        headers = {'Content-Type': 'application/json'} 
        params = {'id': self.id}  
        response = requests.get(self.baseUrl, headers=headers, params=params)
        return response