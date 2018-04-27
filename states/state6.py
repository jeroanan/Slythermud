import logging 

import states.state as state

class State6(state.State):
    """State6: Ask an existing user for their password"""

    def __init__(self, sInfo, config, world):
        super().__init__(sInfo, config, world)
        self.__logger = logging.getLogger()
        logging.basicConfig(level=logging.INFO)
        
    def enter(self):
        msg = "Enter password"
        self.sInfo.send_string(msg)

    def process_input(self, data):
        if self.sInfo.player.verify_password(data):
            # Password is valid. Enter game.
            self.__logger.info('Player {pn} logged in.'.format(pn=self.sInfo.player.name))
            self.change_state(10)
        else:
            self.enter() # not good long-term.

