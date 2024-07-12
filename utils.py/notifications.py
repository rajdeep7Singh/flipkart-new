class Observer:
    def update(self, user):
        raise NotImplementedError


class WaitlistNotifier(Observer):
    def update(self, user):
        print(f"User {user.name} promoted from waitlist")
