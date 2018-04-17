import states.state as state
import world.direction as direction

class State10(state.State):
    """State10: main in-game state"""

    def enter(self):
        self.__enter_room(self.sInfo.player.status.zone, self.sInfo.player.status.room)

    def process_input(self, data):
        player = self.sInfo.player
        player_status = player.status

        if direction.is_direction(data):
            room = player_status.room
            zone = player_status.zone

            if room.can_exit_dir(data):
                new_zone, new_room = room.get_exit(data)
                
                if new_zone!=".":
                    # zone cnange
                    pass
                else:

                    pass

    def __enter_room(self, zone, room):

        def find_in_list(l, v):
            return [r for r in l if r.id==v][0]

        zone = find_in_list(self.world, zone)
        room = find_in_list(zone.rooms, room)

        player, status = self.__get_player_status()

        status.room = room
        status.zone = zone
        
        self.sInfo.send_string(room.name)
        self.sInfo.send_string(room.description)

    def __get_player_status(self):
        return (self.sInfo, self.sInfo.player.status)
