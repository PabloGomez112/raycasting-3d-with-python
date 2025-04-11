import math

RAD_CONS = 180

def deg_to_rad(n):
    return n * (math.pi / RAD_CONS)

def normalize_angle(angle):
    """
    Takes an angle in radians and returns this angle normalized (0, 2PI)
    :param angle: Angle in radians
    :return: Normalized angle
    """
    angle = angle % (2 * math.pi)
    return angle if angle != 0 else 2 * math.pi