import requests
class MinkeyService:
    def __init__(self, serviceConfig: dict):
        self.endpoint = serviceConfig['endpoint']

    def getString(self, key):
        resp = requests.get(f"{self.endpoint}/string/{key}")
        return resp.text

    def autoGet(self, data):
        if data.startswith('minkey@'):
            key = data[7:]
            return self.getString(key)