import states.state as state

class State2(state.State):

    def enter(self):
        msg = "Are you sure you want to be known as {} [Y/N]?".format(self.sInfo.player.name)
        self.sInfo.send_string(msg)

    def process_input(self, data):
        if data[0].upper() == "Y":
            # Get password
            pass
        elif data[0].upper() == "N":
            self.sInfo.change_state(self.config, 1)
        else:
            self.enter()
