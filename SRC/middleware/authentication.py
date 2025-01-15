class AuthenticationMiddleware:
    def __init__(self):
        self.token = "secret_token"

    def authenticate(self, request_token):
        if request_token == self.token:
            return True
        return False
