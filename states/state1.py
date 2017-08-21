import states.state as state
import entities.player as player

class State1(state.State):
    """State 1: The user has just connected and we need to get their
       character's name.

       If it's a name that does not exist yet, we commence with character
       creation. Otherwise we ask for password before entering the MUD
    """

    def enter(self):
        banner_filename = "{}/banner".format(self.config.text_dir)
        banner = ''

        with open(banner_filename) as bf:
            banner = bf.read()

        for i, bLines in enumerate(banner.split('\n')):
            if i < len(bLines) - 1:
                self.sInfo.send_string(bLines)
            else:
                self.sInfo.send_string(bLines, False)			

    def process_input(self, data):
        the_player = player.Player.load_by_name(self.config, data)
        state = None

        if the_player is None:
            the_player = player.Player()
            the_player.name = data
            state = 2
        else:
            print("The player already exists")

        self.sInfo.player = the_player
        self.sInfo.change_state(self.config, state)

        
