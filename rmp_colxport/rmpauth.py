from requests.auth import AuthBase

class RMPAuth(AuthBase):
    def __init__(self, encodedData):
        self.basicAuth = encodedData

    def __call__(self, r):
        r.headers['Authorization'] = self.basicAuth
        return r
