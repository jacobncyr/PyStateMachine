import StateTemplate
import StateMachine
import time

class BaseState:
    def __init__(self):
        self.seconds_left = 30

    def enter(self):
        print("Entered Base State this is where you set up variables")

    def tick(self, delta_time):

        self.seconds_left -= delta_time
        if self.seconds_left > 0:
            print(f"{int(self.seconds_left)} seconds left.")
        else:
            print("Base State finished. Thats where you put quick calculable tasks")

    def exit(self):
        print("Exiting Base State")






# Create an instance of the BaseState
base_state = BaseState()

# Create an instance of the StateMachine
state_machine = StateMachine.StateMachine()

# Pass the BaseState to the StateMachine
state_machine.switch_state(base_state)

# Update the state machine for a certain amount of time (e.g., 30 seconds)
total_time = 5
current_time = 0
while current_time < total_time:
    state_machine.update(1)  # Update with a delta time of 1 second
    current_time += 1
    time.sleep(1)
# After the loop, you might want to switch to another state or handle other logic
