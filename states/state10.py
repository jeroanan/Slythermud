import states.state as state

class State10(state.State):
    """State10: main in-game state"""

    def enter(self):
        self.__enter_room(self.sInfo.player.status.zone, self.sInfo.player.status.room)

    def process_input(self, data):
        pass

    def __enter_room(self, zone, room):

        def f(l, v):
            return [r for r in l if r.id==v][0]

        zone = f(self.world, zone)
        room = f(zone.rooms, room)

        self.sInfo.send_string(room.name)
        self.sInfo.send_string(room.description)
    


        
