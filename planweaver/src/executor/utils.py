DEBUG = False


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
