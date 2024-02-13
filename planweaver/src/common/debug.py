import os

DEBUG = os.environ.get("PLANWEAVER_DEBUG_MODE", "false").lower() in (
    "true",
    "1",
    "t",
)


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
