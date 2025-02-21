import enum


class WallType(enum.IntEnum):
    """All possible wall types.

    Data from https://github.com/tModLoader/tModLoader/wiki/Vanilla-Wall-IDs."""

    STONE = 1
    DIRT_UNSAFE = 2
    EBONSTONE_UNSAFE = 3
    WOOD = 4
    GRAY_BRICK = 5
    RED_BRICK = 6
    BLUE_DUNGEON_UNSAFE = 7
    GREEN_DUNGEON_UNSAFE = 8
    PINK_DUNGEON_UNSAFE = 9
    GOLD_BRICK = 10
    SILVER_BRICK = 11
    COPPER_BRICK = 12
    HELLSTONE_BRICK_UNSAFE = 13
    OBSIDIAN_BRICK_UNSAFE = 14
    MUD_UNSAFE = 15
    DIRT = 16
    BLUE_DUNGEON = 17
    GREEN_DUNGEON = 18
    PINK_DUNGEON = 19
    OBSIDIAN_BRICK = 20
    GLASS = 21
    PEARLSTONE_BRICK = 22
    IRIDESCENT_BRICK = 23
    MUDSTONE_BRICK = 24
    COBALT_BRICK = 25
    MYTHRIL_BRICK = 26
    PLANKED = 27
    PEARLSTONE_BRICK_UNSAFE = 28
    CANDY_CANE = 29
    GREEN_CANDY_CANE = 30
    SNOW_BRICK = 31
    ADAMANTITE_BEAM = 32
    DEMONITE_BRICK = 33
    SANDSTONE_BRICK = 34
    EBONSTONE_BRICK = 35
    RED_STUCCO = 36
    YELLOW_STUCCO = 37
    GREEN_STUCCO = 38
    GRAY = 39
    SNOW_WALL_UNSAFE = 40
    EBONWOOD = 41
    RICH_MAOGANY = 42
    PEARLWOOD = 43
    RAINBOW_BRICK = 44
    TIN_BRICK = 45
    TUNGSTEN_BRICK = 46
    PLATINUM_BRICK = 47
    AMETHYST_UNSAFE = 48
    TOPAZ_UNSAFE = 49
    SAPPHIRE_UNSAFE = 50
    EMERALD_UNSAFE = 51
    RUBY_UNSAFE = 52
    DIAMOND_UNSAFE = 53
    CAVE_UNSAFE = 54
    CAVE2UNSAFE = 55
    CAVE3UNSAFE = 56
    CAVE4UNSAFE = 57
    CAVE5UNSAFE = 58
    CAVE6UNSAFE = 59
    LIVING_LEAF = 60
    CAVE7UNSAFE = 61
    SPIDER_UNSAFE = 62
    GRASS_UNSAFE = 63
    JUNGLE_UNSAFE = 64
    FLOWER_UNSAFE = 65
    GRASS = 66
    JUNGLE = 67
    FLOWER = 68
    CORRUPT_GRASS_UNSAFE = 69
    HALLOWED_GRASS_UNSAFE = 70
    ICE_UNSAFE = 71
    CACTUS = 72
    CLOUD = 73
    MUSHROOM = 74
    BONE = 75
    SLIME = 76
    FLESH = 77
    LIVING_WOOD = 78
    OBSIDIAN_BACK_UNSAFE = 79
    MUSHROOM_UNSAFE = 80
    CRIMSON_GRASS_UNSAFE = 81
    DISC_WALL = 82
    CRIMSTONE_UNSAFE = 83
    ICE_BRICK = 84
    SHADEWOOD = 85
    HIVE_UNSAFE = 86
    LIHZAHRD_BRICK_UNSAFE = 87
    PURPLE_STAINED_GLASS = 88
    YELLOW_STAINED_GLASS = 89
    BLUE_STAINED_GLASS = 90
    GREEN_STAINED_GLASS = 91
    RED_STAINED_GLASS = 92
    RAINBOW_STAINED_GLASS = 93
    BLUE_DUNGEON_SLAB_UNSAFE = 94
    BLUE_DUNGEON_TILE_UNSAFE = 95
    PINK_DUNGEON_SLAB_UNSAFE = 96
    PINK_DUNGEON_TILE_UNSAFE = 97
    GREEN_DUNGEON_SLAB_UNSAFE = 98
    GREEN_DUNGEON_TILE_UNSAFE = 99
    BLUE_DUNGEON_SLAB = 100
    BLUE_DUNGEON_TILE = 101
    PINK_DUNGEON_SLAB = 102
    PINK_DUNGEON_TILE = 103
    GREEN_DUNGEON_SLAB = 104
    GREEN_DUNGEON_TILE = 105
    WOODEN_FENCE = 106
    METAL_FENCE = 107
    HIVE = 108
    PALLADIUM_COLUMN = 109
    BUBBLEGUM_BLOCK = 110
    TITANSTONE_BLOCK = 111
    LIHZAHRD_BRICK = 112
    PUMPKIN = 113
    HAY = 114
    SPOOKY_WOOD = 115
    CHRISTMAS_TREE_WALLPAPER = 116
    ORNAMENT_WALLPAPER = 117
    CANDY_CANE_WALLPAPER = 118
    FESTIVE_WALLPAPER = 119
    STARS_WALLPAPER = 120
    SQUIGGLES_WALLPAPER = 121
    SNOWFLAKE_WALLPAPER = 122
    KRAMPUS_HORN_WALLPAPER = 123
    BLUEGREEN_WALLPAPER = 124
    GRINCH_FINGER_WALLPAPER = 125
    FANCY_GRAY_WALLPAPER = 126
    ICE_FLOE_WALLPAPER = 127
    MUSIC_WALLPAPER = 128
    PURPLE_RAIN_WALLPAPER = 129
    RAINBOW_WALLPAPER = 130
    SPARKLE_STONE_WALLPAPER = 131
    STARLIT_HEAVEN_WALLPAPER = 132
    BUBBLE_WALLPAPER = 133
    COPPER_PIPE_WALLPAPER = 134
    DUCKY_WALLPAPER = 135
    WATERFALL = 136
    LAVAFALL = 137
    EBONWOOD_FENCE = 138
    RICH_MAHOGANY_FENCE = 139
    PEARLWOOD_FENCE = 140
    SHADEWOOD_FENCE = 141
    WHITE_DYNASTY = 142
    BLUE_DYNASTY = 143
    ARCANE_RUNES = 144
    IRON_FENCE = 145
    COPPER_PLATING = 146
    STONE_SLAB = 147
    SAIL = 148
    BOREAL_WOOD = 149
    BOREAL_WOOD_FENCE = 150
    PALM_WOOD = 151
    PALM_WOOD_FENCE = 152
    AMBER_GEMSPARK = 153
    AMETHYST_GEMSPARK = 154
    DIAMOND_GEMSPARK = 155
    EMERALD_GEMSPARK = 156
    AMBER_GEMSPARK_OFF = 157
    AMETHYST_GEMSPARK_OFF = 158
    DIAMOND_GEMSPARK_OFF = 159
    EMERALD_GEMSPARK_OFF = 160
    RUBY_GEMSPARK_OFF = 161
    SAPPHIRE_GEMSPARK_OFF = 162
    TOPAZ_GEMSPARK_OFF = 163
    RUBY_GEMSPARK = 164
    SAPPHIRE_GEMSPARK = 165
    TOPAZ_GEMSPARK = 166
    TIN_PLATING = 167
    CONFETTI = 168
    CONFETTI_BLACK = 169
    CAVE_WALL = 170
    CAVE_WALL2 = 171
    HONEYFALL = 172
    CHLOROPHYTE_BRICK = 173
    CRIMTANE_BRICK = 174
    SHROOMITE_PLATING = 175
    MARTIAN_CONDUIT = 176
    HELLSTONE_BRICK = 177
    MARBLE_UNSAFE = 178
    MARBLE_BLOCK = 179
    GRANITE_UNSAFE = 180
    GRANITE_BLOCK = 181
    METEORITE_BRICK = 182
    MARBLE = 183
    GRANITE = 184
    CAVE8UNSAFE = 185
    CRYSTAL = 186
    SANDSTONE = 187
    CORRUPTION_UNSAFE1 = 188
    CORRUPTION_UNSAFE2 = 189
    CORRUPTION_UNSAFE3 = 190
    CORRUPTION_UNSAFE4 = 191
    CRIMSON_UNSAFE1 = 192
    CRIMSON_UNSAFE2 = 193
    CRIMSON_UNSAFE3 = 194
    CRIMSON_UNSAFE4 = 195
    DIRT_UNSAFE1 = 196
    DIRT_UNSAFE2 = 197
    DIRT_UNSAFE3 = 198
    DIRT_UNSAFE4 = 199
    HALLOW_UNSAFE1 = 200
    HALLOW_UNSAFE2 = 201
    HALLOW_UNSAFE3 = 202
    HALLOW_UNSAFE4 = 203
    JUNGLE_UNSAFE1 = 204
    JUNGLE_UNSAFE2 = 205
    JUNGLE_UNSAFE3 = 206
    JUNGLE_UNSAFE4 = 207
    LAVA_UNSAFE1 = 208
    LAVA_UNSAFE2 = 209
    LAVA_UNSAFE3 = 210
    LAVA_UNSAFE4 = 211
    ROCKS_UNSAFE1 = 212
    ROCKS_UNSAFE2 = 213
    ROCKS_UNSAFE3 = 214
    ROCKS_UNSAFE4 = 215
    HARDENED_SAND = 216
    CORRUPT_HARDENED_SAND = 217
    CRIMSON_HARDENED_SAND = 218
    HALLOW_HARDENED_SAND = 219
    CORRUPT_SANDSTONE = 220
    CRIMSON_SANDSTONE = 221
    HALLOW_SANDSTONE = 222
    DESERT_FOSSIL = 223
    LUNAR_BRICK_WALL = 224
    COG_WALL = 225
    SAND_FALL = 226
    SNOW_FALL = 227
    SILLY_BALLOON_PINK_WALL = 228
    SILLY_BALLOON_PURPLE_WALL = 229
    SILLY_BALLOON_GREEN_WALL = 230

    # 1.4, adapted from: https://github.com/TerraMap/windows/blob/master/Data/tiles.xml
    # Ecto blocks are craftable versions of the natural walls which can be crafted in graveyards
    # https://terraria.gamepedia.com/1.4.0.1

    IRON_BRICK = 231
    LEAD_BRICK = 232
    LESION_BLOCK = 233
    CRIMSTONE_BRICK = 234
    SMOOTH_SANDSTONE = 235
    SPIDER = 236
    SOLAR_BRICK = 237
    VORTEX_BRICK = 238
    NEBULA_BRICK = 239
    STARDUST_BRICK = 240
    ORANGE_STAINED_GLASS = 241
    GOLD_STARRY_GLASS_WALL = 242
    BLUE_STARRY_GLASS_WALL = 243
    LIVING_WOOD_UNSAFE = 244
    WROUGHT_IRON_FENCE = 245
    ECTO_EBONSTONE = 246
    ECTO_MUDWALL = 247
    ECTO_PEARLSTONE = 248
    ECTO_SNOWWALL = 249
    ECTO_AMETHYST = 250
    ECTO_TOPAZ = 251
    ECTO_SAPPHIRE = 252
    ECTO_EMERALD = 253
    ECTO_RUBY = 254
    ECTO_DIAMOND = 255
    ECTO_CAVE1 = 256
    ECTO_CAVE2 = 257
    ECTO_CAVE3 = 258
    ECTO_CAVE4 = 259
    ECTO_CAVE5 = 260
    ECTO_CAVE6 = 261
    ECTO_CAVE7 = 262
    ECTO_SPIDER = 263
    ECTO_CORRUPT_GRASS = 264
    ECTO_HALLOWED_GRASS = 265
    ECTO_ICE = 266
    ECTO_OBSIDIAN_BACK = 267
    ECTO_CRIMSON_GRASS = 268
    ECTO_CRIMSTONE = 269
    ECTO_CAVEWALL1 = 270
    ECTO_CAVEWALL2 = 271
    ECTO_MARBLE_UNUSED = 272
    ECTO_GRANITE_UNUSED = 273
    ECTO_CAVE8 = 274
    ECTO_SANDSTONE = 275
    ECTO_CORRUPTION1 = 276
    ECTO_CORRUPTION2 = 277
    ECTO_CORRUPTION3 = 278
    ECTO_CORRUPTION4 = 279
    ECTO_CRIMSON1 = 280
    ECTO_CRIMSON2 = 281
    ECTO_CRIMSON3 = 282
    ECTO_CRIMSON4 = 283
    ECTO_DIRT1 = 284
    ECTO_DIRT2 = 285
    ECTO_DIRT3 = 286
    ECTO_DIRT4 = 287
    ECTO_HALLOW1 = 288
    ECTO_HALLOW2 = 289
    ECTO_HALLOW3 = 290
    ECTO_HALLOW4 = 291
    ECTO_JUNGLE1 = 292
    ECTO_JUNGLE2 = 293
    ECTO_JUNGLE3 = 294
    ECTO_JUNGLE4 = 295
    ECTO_LAVA1 = 296
    ECTO_LAVA2 = 297
    ECTO_LAVA3 = 298
    ECTO_LAVA4 = 299
    ECTO_ROCKS1 = 300
    ECTO_ROCKS2 = 301
    ECTO_ROCKS3 = 302
    ECTO_ROCKS4 = 303
    ECTO_HARDENED_SAND = 304
    ECTO_CORRUPT_HARDENED_SAND = 305
    ECTO_CRIMSON_HARDENED_SAND = 306
    ECTO_HALLOW_HARDENED_SAND = 307
    ECTO_CORRUPT_SANDSTONE = 308
    ECTO_CRIMSON_SANDSTONE = 309
    ECTO_HALLOW_SANDSTONE = 310
    ECTO_DESERT_FOSSIL = 311
    BAMBOO_BLOCK_WALL = 312
    LARGE_BAMBOO_BLOCK_WALL = 313
    ECTO_AMBER_STONE_WALL = 314
    BAMBOO_FENCE = 315
    ASHWOOD = 316
    ASHWOODFENCE = 317
    ECHOWALL = 318
    REEFWALL = 319
    POOPWALL = 320
    SHIMMERBLOCKWALL = 321
    SHIMMERBRICKWALL = 322
    LUNARRUSTBRICKWALL = 323
    DARKCELESTIALBRICKWALL = 324
    ASTRABRICKWALL = 325
    COSMICEMBERBRICKWALL = 326
    CRYOCOREBRICKWALL = 327
    MERCURYBRICKWALL = 328
    STARROYALEBRICKWALL = 329
    HEAVENFORGEBRICKWALL = 330
    ANCIENTBLUEBRICKWALL = 331
    ANCIENTGREENBRICKWALL = 332
    ANCIENTPINKBRICKWALL = 333
    ANCIENTGOLDBRICKWALL = 334
    ANCIENTSILVERBRICKWALL = 335
    ANCIENTCOPPERBRICKWALL = 336
    ANCIENTOBSIDIANBRICKWALL = 337
    ANCIENTHELLSTONEBRICKWALL = 338
    ANCIENTCOBALTBRICKWALL = 339
    ANCIENTMYTHRILBRICKWALL = 340
    LAVAMOSSBLOCKWALL = 341
    ARGONMOSSBLOCKWALL = 342
    KRYPTONMOSSBLOCKWALL = 343
    XENONMOSSBLOCKWALL = 344
    VIOLETMOSSBLOCKWALL = 345
    RAINBOWMOSSBLOCKWALL = 346

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"