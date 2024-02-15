class State:
    def __init__(self):
        pass

    def enter(self):
        raise NotImplementedError("Subclasses must implement enter() method")

    def tick(self, delta_time):
        raise NotImplementedError("Subclasses must implement tick() method")

    def exit(self):
        raise NotImplementedError("Subclasses must implement exit() method")
