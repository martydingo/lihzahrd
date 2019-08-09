class Backgrounds:
    """The backgrounds of various world biomes."""
    def __init__(self,
                 bg_underground_snow: int,
                 bg_underground_jungle: int,
                 bg_hell: int,
                 bg_forest: int,
                 bg_corruption: int,
                 bg_jungle: int,
                 bg_snow: int,
                 bg_hallow: int,
                 bg_crimson: int,
                 bg_desert: int,
                 bg_ocean: int):
        self.bg_underground_snow: int = bg_underground_snow
        self.bg_underground_jungle: int = bg_underground_jungle
        self.bg_hell: int = bg_hell
        self.bg_forest: int = bg_forest
        self.bg_corruption: int = bg_corruption
        self.bg_jungle: int = bg_jungle
        self.bg_snow: int = bg_snow
        self.bg_hallow: int = bg_hallow
        self.bg_crimson: int = bg_crimson
        self.bg_desert: int = bg_desert
        self.bg_ocean: int = bg_ocean

    def __repr__(self):
        return f"WorldBackgrounds({self.bg_underground_snow}, {self.bg_underground_jungle}, {self.bg_hell}, {self.bg_forest}, {self.bg_corruption}, {self.bg_jungle}, {self.bg_snow}, {self.bg_hallow}, {self.bg_crimson}, {self.bg_desert}, {self.bg_ocean})"
