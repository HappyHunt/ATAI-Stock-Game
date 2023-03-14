import time


def get_step(interval: int):
    return interval*60 * 200 * 1000


def get_timestamp():
    return int(time.time()) * 1000



