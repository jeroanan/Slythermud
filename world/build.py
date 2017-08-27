import json
import os

import entities.room as room
import entities.zone as zone

class Build(object):
    
    @classmethod
    def build(cls):

        zones = []

        json_dir = os.path.join("world", "data")
        fs = [j for j in os.listdir(json_dir) if j.endswith(".json")]
        
        for f in fs:
            file_path = os.path.join(json_dir, f)
            with open(file_path) as j:
                c = json.loads(j.read())
                
                z = zone.Zone()
                z.id = c["id"]
                z.name = c["name"]
                z.description = c["description"]

                for r in c["rooms"]:
                    rm = room.Room()
                    rm.id = r["id"]
                    rm.name = r["name"]
                    rm.description = r["description"]

                    z.rooms.append(rm)

                zones.append(z)

        return zones
