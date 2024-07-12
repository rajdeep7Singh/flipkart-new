from services.center_service import CenterService
from services.slot_service import SlotService
from services.user_service import UserService
from services.workout_service import WorkoutService
from utils.factory import FlipFitFactory
from utils.exceptions import *


def main():
    center_service = CenterService()
    slot_service = SlotService(center_service)
    user_service = UserService()
    workout_service = WorkoutService()

    # Add centers
    center_service.add_center("Bellandur", "Bangalore", "Location 1", 12.9352, 77.6245)

    # Add workouts
    workout_service.add_workout("Weights")
    workout_service.add_workout("Cardio")

    # Add slots
    slot_service.add_slot("Bellandur", "6:00 AM", "Weights", 10, 5)
    slot_service.add_slot("Bellandur", "7:00 AM", "Cardio", 10, 5)

    # Register user
    user_service.register_user("user1", "John Doe")

    # Book slot
    user = user_service.get_user("user1")
    center = center_service.get_center("Bellandur")
    slots = center.get_slots()

    for slot in slots:
        if slot.start_time == "6:00 AM" and slot.workout_type == "Weights":
            if slot.book_slot(user):
                user.add_booking(slot)
            else:
                print("Booking failed or added to waitlist")

    # View user bookings
    bookings = user.get_bookings()
    for booking in bookings:
        print(f"Booking: {booking.start_time} - {booking.workout_type}")

    # Cancel slot
    for booking in bookings:
        if booking.start_time == "6:00 AM" and booking.workout_type == "Weights":
            promoted_user = booking.cancel_booking(user)
            user.remove_booking(booking)
            if promoted_user:
                print(f"User {promoted_user.name} promoted from waitlist")


if __name__ == "__main__":
    main()
