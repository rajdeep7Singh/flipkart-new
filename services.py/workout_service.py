from app.models.workout import WorkoutType
import threading

class WorkoutService:
    _instance = None
    _lock = threading.Lock()  # Lock for singleton instance creation

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(WorkoutService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'workouts'):
            self.workouts = {}
            self.lock = threading.Lock()  # Lock for workout operations

    def add_workout(self, name):
        with self.lock:
            if name in self.workouts:
                raise Exception("Workout type already exists")
            self.workouts[name] = WorkoutType(name)

    def get_workout(self, name):
        with self.lock:
            return self.workouts.get(name)
