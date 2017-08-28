class State(object):

    def __init__(self, sInfo, config, world):
        self.sInfo = sInfo
        self.config = config
        self.world = world

    def change_state(self, state):
        self.sInfo.change_state(self.config, self.world, state)

