from app.models.slot import Slot
import threading

class SlotService:
    _instance = None
    _lock = threading.Lock()  # Lock for singleton instance creation

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(SlotService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, center_service):
        if not hasattr(self, 'center_service'):
            self.center_service = center_service
            self.lock = threading.Lock()  # Lock for slot operations

    def add_slot(self, center_name, start_time, workout_type, seats, waitlist_size):
        with self.lock:
            center = self.center_service.get_center(center_name)
            if not center:
                raise Exception("Center not found")
            slot = Slot(start_time, workout_type, seats, waitlist_size)
            center.add_slot(slot)
