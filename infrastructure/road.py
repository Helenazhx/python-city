def draw_road(length, orientation = "horizontal"):
    """
    prints a road of a given length

    Args: 
        length: integer defining the length of a road
        orientation : string defining oreintation of a raod
                        values in [vertical, horizontal]
    """
    #constance
    ALLOWED_OREINTATION = ['vertical', 'horizontal']
    #Sanitizing parameter
    if length < 0:
        raise ValueError("length is negative")
    if length == 0:
        return
    if orientation not in ALLOWED_OREINTATION:
        raise ValueError("not a valid orientation")
    # printing the road
    if orientation == "horizontal":
        for _ in range(length):
            print("-", end = "")
        print()
    else:
        for _ in range(length):
            print("|")
        print()
    return
