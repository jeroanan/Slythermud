import states.state as state

class State10(state.State):
    """State10: main in-game state"""

    def enter(self):
        self.__enter_room(self.sInfo.player.status.zone, self.sInfo.player.status.room)

    def process_input(self, data):
        pass

    def __enter_room(self, zone, room):

        def find_in_list(l, v):
            return [r for r in l if r.id==v][0]

        zone = find_in_list(self.world, zone)
        room = find_in_list(zone.rooms, room)

        self.sInfo.send_string(room.name)
        self.sInfo.send_string(room.description)
    


        
