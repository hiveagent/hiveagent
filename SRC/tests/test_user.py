import unittest
from src.controllers.user_controller import UserController

class TestUserController(unittest.TestCase):
    def setUp(self):
        self.controller = UserController()

    def test_create_user(self):
        user_data = {"name": "John", "email": "john@example.com"}
        created_user = self.controller.create_user(user_data)
        self.assertEqual(created_user["name"], "John")
        self.assertEqual(created_user["email"], "john@example.com")

    def test_get_user(self):
        user_data = {"name": "John", "email": "john@example.com"}
        created_user = self.controller.create_user(user_data)
        user = self.controller.get_user(created_user["user_id"])
        self.assertEqual(user["name"], "John")

