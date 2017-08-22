import states.state as state

class State5(state.State):
    """State 5: Ask the user for their gender
                When this state has reached is conclusion
                at this point we save the new player and enter
                the game"""

    def enter(self):
        msg = "Select Gender [M/F]:"
        self.sInfo.send_string(msg)

    def process_input(self, data):
        gender = data[0].upper()

        if gender in ['M', 'F']:
            self.sInfo.player.gender = gender
            self.sInfo.player.save(self.config)
            self.sInfo.send_string("Player Saved")
        else:
            self.enter()
    


