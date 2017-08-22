import states.state as state

class State4(state.State):
    """State 4: Ask the user to confirm their password"""

    def enter(self):
        msg = "Confirm password:"
        self.sInfo.send_string(msg)

    def process_input(self, data):
        if self.sInfo.player.verify_password(data):
            self.sInfo.change_state(self.config, 5)
        else:
            self.sInfo.send_string("Passwords do not match")
            self.sInfo.change_state(self.config, 3)
