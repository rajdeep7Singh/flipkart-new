from app.models.center import Center
from app.models.slot import Slot
from app.models.user import User
from app.models.workout import WorkoutType


class FlipFitFactory:
    @staticmethod
    def create_center(name, city, location, lat, long):
        return Center(name, city, location, lat, long)

    @staticmethod
    def create_slot(start_time, workout_type, seats, waitlist_size):
        return Slot(start_time, workout_type, seats, waitlist_size)

    @staticmethod
    def create_user(user_id, name):
        return User(user_id, name)

    @staticmethod
    def create_workout(name):
        return WorkoutType(name)
