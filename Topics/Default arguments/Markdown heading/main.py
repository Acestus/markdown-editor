def heading(heading, level=1):
    if level > 6:
        level = 6
    elif level < 1:
        level = 1
    return "#" * level + " " + heading
