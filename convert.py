from typing import Optional

#Takes a string as input
#Tries to convert it to float, returns float if successful
#If unsuccessful, returns None
def str_to_float(inp: str) -> Optional[float]:
    try:
        f = float(inp)
        return f
    except ValueError:
        return None
