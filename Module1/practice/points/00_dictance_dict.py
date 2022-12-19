import math

def distance(p1: dict, p2: dict) -> float:
    return math.sqrt((p2['x'] - p1['x']) ** 2) + math.sqrt((p2['y'] - p1['y']) ** 2)
