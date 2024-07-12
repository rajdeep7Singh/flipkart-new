class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.bookings = []

    def add_booking(self, slot):
        self.bookings.append(slot)

    def remove_booking(self, slot):
        self.bookings.remove(slot)

    def get_bookings(self):
        return self.bookings
