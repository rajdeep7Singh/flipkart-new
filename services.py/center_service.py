from app.models.center import Center
import threading


class CenterService:
    _instance = None
    _lock = threading.Lock()  # Lock for singleton instance creation

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(CenterService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'centers'):
            self.centers = {}
            self.lock = threading.Lock()  # Lock for center operations

    def add_center(self, name, city, location, lat, long):
        with self.lock:
            if name in self.centers:
                raise Exception("Center already exists")
            self.centers[name] = Center(name, city, location, lat, long)

    def get_center(self, name):
        with self.lock:
            return self.centers.get(name)
