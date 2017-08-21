import states.state as state

class State4(state.State):

    def enter(self):
        msg = "Confirm password:"
        self.sInfo.send_string(msg)

    def process_input(self, data):
        if self.sInfo.player.verify_password(data):
            pass
            #TODO: Next
        else:
            self.sInfo.send_string("Passwords do not match")
            self.sInfo.change_state(self.config, 3)
