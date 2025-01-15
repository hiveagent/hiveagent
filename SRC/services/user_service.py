from src.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, user_data):
        # Here you would add validation logic
        return self.repository.save(user_data)
    
    def get_user(self, user_id):
        return self.repository.find_by_id(user_id)
