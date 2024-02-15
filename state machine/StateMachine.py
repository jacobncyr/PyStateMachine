class StateMachine:
    def __init__(self):
        self.current_state = None

    def switch_state(self, new_state):
        if self.current_state:
            self.current_state.exit()
        self.current_state = new_state
        if self.current_state:
            self.current_state.enter()

    def update(self, delta_time):
        if self.current_state:
            self.current_state.tick(delta_time)
