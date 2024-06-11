import re

def convert_esi_short_to_route_target_format(esi_short):
    if esi_short is None or esi_short == "":
        return None
    esi = esi_short.replace(":", "")
    return ":".join(re.findall("..", esi))
