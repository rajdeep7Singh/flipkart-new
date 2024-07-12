import threading
from app.utils.notifications import WaitlistNotifier

class Slot:
    def __init__(self, start_time, workout_type, seats, waitlist_size):
        self.start_time = start_time
        self.workout_type = workout_type
        self.seats = seats
        self.waitlist_size = waitlist_size
        self.booked_seats = 0
        self.waitlist = []
        self.notifier = WaitlistNotifier()
        self.lock = threading.Lock()  # Lock for concurrency control

    def book_slot(self, user):
        with self.lock:
            if self.booked_seats < self.seats:
                self.booked_seats += 1
                return True
            elif len(self.waitlist) < self.waitlist_size:
                self.waitlist.append(user)
                return True
            return False

    def cancel_booking(self, user):
        with self.lock:
            if user in self.waitlist:
                self.waitlist.remove(user)
            else:
                self.booked_seats -= 1
                if self.waitlist:
                    promoted_user = self.waitlist.pop(0)
                    self.booked_seats += 1
                    self.notifier.update(promoted_user)
                    return promoted_user
            return None
