from app.models.user import User
import threading

class UserService:
    _instance = None
    _lock = threading.Lock()  # Lock for singleton instance creation

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(UserService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'users'):
            self.users = {}
            self.lock = threading.Lock()  # Lock for user operations

    def register_user(self, user_id, name):
        with self.lock:
            if user_id in self.users:
                raise Exception("User already exists")
            self.users[user_id] = User(user_id, name)

    def get_user(self, user_id):
        with self.lock:
            return self.users.get(user_id)
