import states.state1 as state1
import states.state2 as state2

class StateFactory(object):

    @classmethod
    def Create(cls, sInfo, config, state_number):
        mapping = {
                1: state1.State1,
                2: state2.State2
        }

        if state_number in mapping:
            return mapping[state_number](sInfo, config)
        else:
            raise Exception("Unknown state number {}".format(state_number))
