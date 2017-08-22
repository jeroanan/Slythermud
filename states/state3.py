import states.state as state

class State3(state.State):
    """State 3: ask the new player for a password"""

    def enter(self):
        msg = "Enter a password:"
        self.sInfo.send_string(msg)

    def process_input(self, data):
        self.sInfo.player.password = data
        self.sInfo.change_state(self.config, 4)

