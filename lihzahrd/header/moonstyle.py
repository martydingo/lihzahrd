import enum


class MoonStyle(enum.IntEnum):
    """All possible moon styles."""
    WHITE = 0
    ORANGE = 1
    RINGED_GREEN = 2

    def __repr__(self):
        return f"MoonStyle('{self.name}')"
