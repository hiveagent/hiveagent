from src.services.user_service import UserService

class UserController:
    def __init__(self):
        self.service = UserService()

    def create_user(self, user_data):
        return self.service.create_user(user_data)
    
    def get_user(self, user_id):
        return self.service.get_user(user_id)
