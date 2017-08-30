import states.state as state

class State6(state.State):
    """State6: Ask an existing user for their password"""

    def enter(self):
        msg = "Enter password"
        self.sInfo.send_string(msg)

    def process_input(self, data):
        if self.sInfo.player.verify_password(data):
            # Password is valid. Enter game.
            self.change_state(10)
        else:
            self.enter() # not good long-term.

