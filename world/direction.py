def is_direction(data):
    return get_direction(data)!=""

def get_direction(data):
    directions = ["north", "east", "south", "west", "up", "down"]
    d = data.lower()

    for x in directions:
        if x.startswith(d): return x

    return ""
