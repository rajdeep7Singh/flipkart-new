class Center:
    def __init__(self, name, city, location, lat, long):
        self.name = name
        self.city = city
        self.location = location
        self.lat = lat
        self.long = long
        self.slots = []

    def add_slot(self, slot):
        self.slots.append(slot)
        
    def get_slots(self):
        return self.slots
