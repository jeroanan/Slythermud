import states.state1 as state1
import states.state2 as state2
import states.state3 as state3
import states.state4 as state4

class StateFactory(object):

    @classmethod
    def Create(cls, sInfo, config, state_number):
        mapping = {
                1: state1.State1,
                2: state2.State2,
                3: state3.State3,
                4: state4.State4
        }

        if state_number in mapping:
            return mapping[state_number](sInfo, config)
        else:
            raise Exception("Unknown state number {}".format(state_number))
