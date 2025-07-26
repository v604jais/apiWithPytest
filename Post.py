import requests
import json

class Post:

    def __init__(self):
        self.baseUrl = "https://api.restful-api.dev/objects"
        

    def post_api(self):
        headers = {'Content-Type': 'application/json'} 
     
        requestbody =   {
                          "name": "Apple MacBook Pro 16",
                           "data": {
                                     "year": 2019,
                                     "price": 1849.99,
                                     "CPU model": "Intel Core i9",
                                     "Hard disk size": "1 TB"
                                    }
                        }
        response = requests.post(self.baseUrl, data=json.dumps(requestbody),headers=headers)
        return response 