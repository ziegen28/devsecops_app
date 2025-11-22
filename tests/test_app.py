import unittest
from app import user_login
from security import is_strong_password

class TestSecurity(unittest.TestCase):

    def test_strong_password(self):
        self.assertTrue(is_strong_password("Admin@123"))

    def test_weak_password(self):
        self.assertFalse(is_strong_password("admin123"))

    def test_valid_login(self):
        result = user_login("admin", "Admin@123")
        self.assertEqual(result["status"], "success")

    def test_invalid_login(self):
        result = user_login("admin", "wrongpass")
        self.assertEqual(result["status"], "error")

if __name__ == "__main__":
    unittest.main()
