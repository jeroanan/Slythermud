import logging 

import states.state as state
import world.direction as direction

class State10(state.State):
    """State10: main in-game state"""

    def __init__(self, sInfo, config, world):
        super().__init__(sInfo, config, world)
        self.__logger = logging.getLogger()
        logging.basicConfig(level=logging.DEBUG)
        
    def enter(self):
        self.__enter_room(self.sInfo.player.status.zone, self.sInfo.player.status.room)

    def process_input(self, data):
        player = self.sInfo.player
        player_status = player.status

        if direction.is_direction(data):
            room_id = player_status.room
            zone_id = player_status.zone

            room = self.__get_room(zone_id, room_id)

            if room.can_exit_dir(data):
                new_zone_id, new_room_id = room.get_exit(data)

                self.sInfo.player.status.room = new_room_id
                self.__enter_room(self.sInfo.player.status.zone, self.sInfo.player.status.room)

                if new_zone_id!=".":
                    # zone cnange
                    pass
                else:
                    pass
            else:
                self.sInfo.send_string("Can't go that way!")

    def __enter_room(self, zone_id, room_id):

        room = self.__get_room(zone_id, room_id)

        self.sInfo.send_string(room.name)
        self.sInfo.send_string(room.description)

    def __get_room(self, zone_id, room_id):
        self.__logger.info('Enter __get_room({zi}, {ri})'.format(zi=zone_id, ri=room_id))
        def find_in_list(l, v):
            matches = [r for r in l if str(r.id)==str(v)]
            return matches[0]

        zone = find_in_list(self.world, zone_id)
        room = find_in_list(zone.rooms, room_id)

        return room

    def __get_player_status(self):
        return (self.sInfo, self.sInfo.player.status)
