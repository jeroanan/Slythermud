import states.state as state

class State2(state.State):
    """State 2: Confirm with the new player that they have chosen the name they want.
                If it is, advance to state 3. Otherwise it's back to state 1.
    """

    def enter(self):
        msg = "Are you sure you want to be known as {} [Y/N]?".format(self.sInfo.player.name)
        self.sInfo.send_string(msg)

    def process_input(self, data):
        if data[0].upper() == "Y":
            self.sInfo.change_state(self.config, 3)
        elif data[0].upper() == "N":
            self.sInfo.change_state(self.config, 1)
        else:
            self.enter()
