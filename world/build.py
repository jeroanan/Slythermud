import json
import os

import entities.zone as zone

def build():

    zones = []

    json_dir = os.path.join("world", "data")
    fs = [j for j in os.listdir(json_dir) if j.endswith(".json")]
    
    for f in fs:
        file_path = os.path.join(json_dir, f)
        with open(file_path) as j:
            c = json.loads(j.read())
            
            zones.append(zone.Zone.from_dict(c))

    return zones

