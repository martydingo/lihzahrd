from ..fileutils import Coordinates
from ..npcs import EntityType


class Room:
    def __init__(self, npc: EntityType, position: Coordinates):
        self.npc: EntityType = npc
        self.position: Coordinates = position

    def __repr__(self):
        return f"<Room for {self.npc} at {self.position}>"
