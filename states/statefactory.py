class StateFactory(object):

    @classmethod
    def Create(cls, sInfo, config, world, state_number):
        n = "states.state" + str(state_number)
        mod = __import__(n, fromlist=[''])
        return getattr(mod, 'State' + str(state_number))(sInfo, config, world)
