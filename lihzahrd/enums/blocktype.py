import enum


class BlockType(enum.IntEnum):
    """All possible block types.

    Data from https://github.com/tModLoader/tModLoader/wiki/Vanilla-Tile-IDs."""

    DIRT = 0
    STONE = 1
    GRASS = 2
    PLANTS = 3
    TORCHES = 4
    TREES = 5
    IRON = 6
    COPPER = 7
    GOLD = 8
    SILVER = 9
    CLOSED_DOOR = 10
    OPEN_DOOR = 11
    HEART = 12
    BOTTLES = 13
    TABLES = 14
    CHAIRS = 15
    ANVILS = 16
    FURNACES = 17
    WORK_BENCHES = 18
    PLATFORMS = 19
    SAPLINGS = 20
    CONTAINERS = 21
    DEMONITE = 22
    CORRUPT_GRASS = 23
    CORRUPT_PLANTS = 24
    EBONSTONE = 25
    DEMON_ALTAR = 26
    SUNFLOWER = 27
    POTS = 28
    PIGGY_BANK = 29
    WOOD_BLOCK = 30
    SHADOW_ORBS = 31
    CORRUPT_THORNS = 32
    CANDLES = 33
    CHANDELIERS = 34
    JACKOLANTERNS = 35
    PRESENTS = 36
    METEORITE = 37
    GRAY_BRICK = 38
    RED_BRICK = 39
    CLAY_BLOCK = 40
    BLUE_DUNGEON_BRICK = 41
    HANGING_LANTERNS = 42
    GREEN_DUNGEON_BRICK = 43
    PINK_DUNGEON_BRICK = 44
    GOLD_BRICK = 45
    SILVER_BRICK = 46
    COPPER_BRICK = 47
    SPIKES = 48
    WATER_CANDLE = 49
    BOOKS = 50
    COBWEB = 51
    VINES = 52
    SAND = 53
    GLASS = 54
    SIGNS = 55
    OBSIDIAN = 56
    ASH = 57
    HELLSTONE = 58
    MUD = 59
    JUNGLE_GRASS = 60
    JUNGLE_PLANTS = 61
    JUNGLE_VINES = 62
    SAPPHIRE = 63
    RUBY = 64
    EMERALD = 65
    TOPAZ = 66
    AMETHYST = 67
    DIAMOND = 68
    JUNGLE_THORNS = 69
    MUSHROOM_GRASS = 70
    MUSHROOM_PLANTS = 71
    MUSHROOM_TREES = 72
    PLANTS2 = 73
    JUNGLE_PLANTS2 = 74
    OBSIDIAN_BRICK = 75
    HELLSTONE_BRICK = 76
    HELLFORGE = 77
    CLAY_POT = 78
    BEDS = 79
    CACTUS = 80
    CORAL = 81
    IMMATURE_HERBS = 82
    MATURE_HERBS = 83
    BLOOMING_HERBS = 84
    TOMBSTONES = 85
    LOOM = 86
    PIANOS = 87
    DRESSERS = 88
    BENCHES = 89
    BATHTUBS = 90
    BANNERS = 91
    LAMPPOSTS = 92
    LAMPS = 93
    KEGS = 94
    CHINESE_LANTERNS = 95
    COOKING_POTS = 96
    SAFES = 97
    SKULL_LANTERNS = 98
    TRASH_CAN = 99
    CANDELABRAS = 100
    BOOKCASES = 101
    THRONES = 102
    BOWLS = 103
    GRANDFATHER_CLOCKS = 104
    STATUES = 105
    SAWMILL = 106
    COBALT = 107
    MYTHRIL = 108
    HALLOWED_GRASS = 109
    HALLOWED_PLANTS = 110
    ADAMANTITE = 111
    EBONSAND = 112
    HALLOWED_PLANTS2 = 113
    TINKERERS_WORKBENCH = 114
    HALLOWED_VINES = 115
    PEARLSAND = 116
    PEARLSTONE = 117
    PEARLSTONE_BRICK = 118
    IRIDESCENT_BRICK = 119
    MUDSTONE = 120
    COBALT_BRICK = 121
    MYTHRIL_BRICK = 122
    SILT = 123
    WOODEN_BEAM = 124
    CRYSTAL_BALL = 125
    DISCO_BALL = 126
    MAGICAL_ICE_BLOCK = 127
    MANNEQUIN = 128
    CRYSTALS = 129
    ACTIVE_STONE_BLOCK = 130
    INACTIVE_STONE_BLOCK = 131
    LEVER = 132
    ADAMANTITE_FORGE = 133
    MYTHRIL_ANVIL = 134
    PRESSURE_PLATES = 135
    SWITCHES = 136
    TRAPS = 137
    BOULDER = 138
    MUSIC_BOXES = 139
    DEMONITE_BRICK = 140
    EXPLOSIVES = 141
    INLET_PUMP = 142
    OUTLET_PUMP = 143
    TIMERS = 144
    CANDY_CANE_BLOCK = 145
    GREEN_CANDY_CANE_BLOCK = 146
    SNOW_BLOCK = 147
    SNOW_BRICK = 148
    HOLIDAY_LIGHTS = 149
    ADAMANTITE_BEAM = 150
    SANDSTONE_BRICK = 151
    EBONSTONE_BRICK = 152
    RED_STUCCO = 153
    YELLOW_STUCCO = 154
    GREEN_STUCCO = 155
    GRAY_STUCCO = 156
    EBONWOOD = 157
    RICH_MAHOGANY = 158
    PEARLWOOD = 159
    RAINBOW_BRICK = 160
    ICE_BLOCK = 161
    BREAKABLE_ICE = 162
    CORRUPT_ICE = 163
    HALLOWED_ICE = 164
    STALACTITE = 165
    TIN = 166
    LEAD = 167
    TUNGSTEN = 168
    PLATINUM = 169
    PINE_TREE = 170
    CHRISTMAS_TREE = 171
    SINKS = 172
    PLATINUM_CANDELABRA = 173
    PLATINUM_CANDLE = 174
    TIN_BRICK = 175
    TUNGSTEN_BRICK = 176
    PLATINUM_BRICK = 177
    EXPOSED_GEMS = 178
    GREEN_MOSS = 179
    BROWN_MOSS = 180
    RED_MOSS = 181
    BLUE_MOSS = 182
    PURPLE_MOSS = 183
    LONG_MOSS = 184
    SMALL_PILES = 185
    LARGE_PILES = 186
    LARGE_PILES2 = 187
    CACTUS_BLOCK = 188
    CLOUD = 189
    MUSHROOM_BLOCK = 190
    LIVING_WOOD = 191
    LEAF_BLOCK = 192
    SLIME_BLOCK = 193
    BONE_BLOCK = 194
    FLESH_BLOCK = 195
    RAIN_CLOUD = 196
    FROZEN_SLIME_BLOCK = 197
    ASPHALT = 198
    FLESH_GRASS = 199
    FLESH_ICE = 200
    FLESH_WEEDS = 201
    SUNPLATE = 202
    CRIMSTONE = 203
    CRIMTANE = 204
    CRIMSON_VINES = 205
    ICE_BRICK = 206
    WATER_FOUNTAIN = 207
    SHADEWOOD = 208
    CANNON = 209
    LAND_MINE = 210
    CHLOROPHYTE = 211
    SNOWBALL_LAUNCHER = 212
    ROPE = 213
    CHAIN = 214
    CAMPFIRE = 215
    FIREWORK = 216
    BLENDOMATIC = 217
    MEAT_GRINDER = 218
    EXTRACTINATOR = 219
    SOLIDIFIER = 220
    PALLADIUM = 221
    ORICHALCUM = 222
    TITANIUM = 223
    SLUSH = 224
    HIVE = 225
    LIHZAHRD_BRICK = 226
    DYE_PLANTS = 227
    DYE_VAT = 228
    HONEY_BLOCK = 229
    CRISPY_HONEY_BLOCK = 230
    LARVA = 231
    WOODEN_SPIKES = 232
    PLANT_DETRITUS = 233
    CRIMSAND = 234
    TELEPORTER = 235
    LIFE_FRUIT = 236
    LIHZAHRD_ALTAR = 237
    PLANTERA_BULB = 238
    METAL_BARS = 239
    PAINTING3X3 = 240
    PAINTING4X3 = 241
    PAINTING6X4 = 242
    IMBUING_STATION = 243
    BUBBLE_MACHINE = 244
    PAINTING2X3 = 245
    PAINTING3X2 = 246
    AUTOHAMMER = 247
    PALLADIUM_COLUMN = 248
    BUBBLEGUM_BLOCK = 249
    TITANSTONE = 250
    PUMPKIN_BLOCK = 251
    HAY_BLOCK = 252
    SPOOKY_WOOD = 253
    PUMPKINS = 254
    AMETHYST_GEMSPARK_OFF = 255
    TOPAZ_GEMSPARK_OFF = 256
    SAPPHIRE_GEMSPARK_OFF = 257
    EMERALD_GEMSPARK_OFF = 258
    RUBY_GEMSPARK_OFF = 259
    DIAMOND_GEMSPARK_OFF = 260
    AMBER_GEMSPARK_OFF = 261
    AMETHYST_GEMSPARK = 262
    TOPAZ_GEMSPARK = 263
    SAPPHIRE_GEMSPARK = 264
    EMERALD_GEMSPARK = 265
    RUBY_GEMSPARK = 266
    DIAMOND_GEMSPARK = 267
    AMBER_GEMSPARK = 268
    WOMANNEQUIN = 269
    FIREFLYINA_BOTTLE = 270
    LIGHTNING_BUGINA_BOTTLE = 271
    COG = 272
    STONE_SLAB = 273
    SAND_STONE_SLAB = 274
    BUNNY_CAGE = 275
    SQUIRREL_CAGE = 276
    MALLARD_DUCK_CAGE = 277
    DUCK_CAGE = 278
    BIRD_CAGE = 279
    BLUE_JAY = 280
    CARDINAL_CAGE = 281
    FISH_BOWL = 282
    HEAVY_WORK_BENCH = 283
    COPPER_PLATING = 284
    SNAIL_CAGE = 285
    GLOWING_SNAIL_CAGE = 286
    AMMO_BOX = 287
    MONARCH_BUTTERFLY_JAR = 288
    PURPLE_EMPEROR_BUTTERFLY_JAR = 289
    RED_ADMIRAL_BUTTERFLY_JAR = 290
    ULYSSES_BUTTERFLY_JAR = 291
    SULPHUR_BUTTERFLY_JAR = 292
    TREE_NYMPH_BUTTERFLY_JAR = 293
    ZEBRA_SWALLOWTAIL_BUTTERFLY_JAR = 294
    JULIA_BUTTERFLY_JAR = 295
    SCORPION_CAGE = 296
    BLACK_SCORPION_CAGE = 297
    FROG_CAGE = 298
    MOUSE_CAGE = 299
    BONE_WELDER = 300
    FLESH_CLONING_VAT = 301
    GLASS_KILN = 302
    LIHZAHRD_FURNACE = 303
    LIVING_LOOM = 304
    SKY_MILL = 305
    ICE_MACHINE = 306
    STEAMPUNK_BOILER = 307
    HONEY_DISPENSER = 308
    PENGUIN_CAGE = 309
    WORM_CAGE = 310
    DYNASTY_WOOD = 311
    RED_DYNASTY_SHINGLES = 312
    BLUE_DYNASTY_SHINGLES = 313
    MINECART_TRACK = 314
    CORALSTONE = 315
    BLUE_JELLYFISH_BOWL = 316
    GREEN_JELLYFISH_BOWL = 317
    PINK_JELLYFISH_BOWL = 318
    SHIP_IN_ABOTTLE = 319
    SEAWEED_PLANTER = 320
    BOREAL_WOOD = 321
    PALM_WOOD = 322
    PALM_TREE = 323
    BEACH_PILES = 324
    TIN_PLATING = 325
    WATERFALL = 326
    LAVAFALL = 327
    CONFETTI = 328
    CONFETTI_BLACK = 329
    COPPER_COIN_PILE = 330
    SILVER_COIN_PILE = 331
    GOLD_COIN_PILE = 332
    PLATINUM_COIN_PILE = 333
    WEAPONS_RACK = 334
    FIREWORKS_BOX = 335
    LIVING_FIRE = 336
    ALPHABET_STATUES = 337
    FIREWORK_FOUNTAIN = 338
    GRASSHOPPER_CAGE = 339
    LIVING_CURSED_FIRE = 340
    LIVING_DEMON_FIRE = 341
    LIVING_FROST_FIRE = 342
    LIVING_ICHOR = 343
    LIVING_ULTRABRIGHT_FIRE = 344
    HONEYFALL = 345
    CHLOROPHYTE_BRICK = 346
    CRIMTANE_BRICK = 347
    SHROOMITE_PLATING = 348
    MUSHROOM_STATUE = 349
    MARTIAN_CONDUIT_PLATING = 350
    CHIMNEY_SMOKE = 351
    CRIMTANE_THORNS = 352
    VINE_ROPE = 353
    BEWITCHING_TABLE = 354
    ALCHEMY_TABLE = 355
    SUNDIAL = 356
    MARBLE_BLOCK = 357
    GOLD_BIRD_CAGE = 358
    GOLD_BUNNY_CAGE = 359
    GOLD_BUTTERFLY_CAGE = 360
    GOLD_FROG_CAGE = 361
    GOLD_GRASSHOPPER_CAGE = 362
    GOLD_MOUSE_CAGE = 363
    GOLD_WORM_CAGE = 364
    SILK_ROPE = 365
    WEB_ROPE = 366
    MARBLE = 367
    GRANITE = 368
    GRANITE_BLOCK = 369
    METEORITE_BRICK = 370
    PINK_SLIME_BLOCK = 371
    PEACE_CANDLE = 372
    WATER_DRIP = 373
    LAVA_DRIP = 374
    HONEY_DRIP = 375
    FISHING_CRATE = 376
    SHARPENING_STATION = 377
    TARGET_DUMMY = 378
    BUBBLE = 379
    PLANTER_BOX = 380
    LAVA_MOSS = 381
    VINE_FLOWERS = 382
    LIVING_MAHOGANY = 383
    LIVING_MAHOGANY_LEAVES = 384
    CRYSTAL_BLOCK = 385
    TRAPDOOR_OPEN = 386
    TRAPDOOR_CLOSED = 387
    TALL_GATE_CLOSED = 388
    TALL_GATE_OPEN = 389
    LAVA_LAMP = 390
    CAGE_ENCHANTED_NIGHTCRAWLER = 391
    CAGE_BUGGY = 392
    CAGE_GRUBBY = 393
    CAGE_SLUGGY = 394
    ITEM_FRAME = 395
    SANDSTONE = 396
    HARDENED_SAND = 397
    CORRUPT_HARDENED_SAND = 398
    CRIMSON_HARDENED_SAND = 399
    CORRUPT_SANDSTONE = 400
    CRIMSON_SANDSTONE = 401
    HALLOW_HARDENED_SAND = 402
    HALLOW_SANDSTONE = 403
    DESERT_FOSSIL = 404
    FIREPLACE = 405
    CHIMNEY = 406
    FOSSIL_ORE = 407
    LUNAR_ORE = 408
    LUNAR_BRICK = 409
    LUNAR_MONOLITH = 410
    DETONATOR = 411
    LUNAR_CRAFTING_STATION = 412
    SQUIRREL_ORANGE_CAGE = 413
    SQUIRREL_GOLD_CAGE = 414
    LUNAR_BLOCK_SOLAR = 415
    LUNAR_BLOCK_VORTEX = 416
    LUNAR_BLOCK_NEBULA = 417
    LUNAR_BLOCK_STARDUST = 418
    LOGIC_GATE_LAMP = 419
    LOGIC_GATE = 420
    CONVEYOR_BELT_LEFT = 421
    CONVEYOR_BELT_RIGHT = 422
    LOGIC_SENSOR = 423
    WIRE_PIPE = 424
    ANNOUNCEMENT_BOX = 425
    TEAM_BLOCK_RED = 426
    TEAM_BLOCK_RED_PLATFORM = 427
    WEIGHTED_PRESSURE_PLATE = 428
    WIRE_BULB = 429
    TEAM_BLOCK_GREEN = 430
    TEAM_BLOCK_BLUE = 431
    TEAM_BLOCK_YELLOW = 432
    TEAM_BLOCK_PINK = 433
    TEAM_BLOCK_WHITE = 434
    TEAM_BLOCK_GREEN_PLATFORM = 435
    TEAM_BLOCK_BLUE_PLATFORM = 436
    TEAM_BLOCK_YELLOW_PLATFORM = 437
    TEAM_BLOCK_PINK_PLATFORM = 438
    TEAM_BLOCK_WHITE_PLATFORM = 439
    GEM_LOCKS = 440
    FAKE_CONTAINERS = 441
    PROJECTILE_PRESSURE_PAD = 442
    GEYSER_TRAP = 443
    BEE_HIVE = 444
    PIXEL_BOX = 445
    SILLY_BALLOON_PINK = 446
    SILLY_BALLOON_PURPLE = 447
    SILLY_BALLOON_GREEN = 448
    SILLY_STREAMER_BLUE = 449
    SILLY_STREAMER_GREEN = 450
    SILLY_STREAMER_PINK = 451
    SILLY_BALLOON_MACHINE = 452
    SILLY_BALLOON_TILE = 453
    PIGRONATA = 454
    PARTY_MONOLITH = 455
    PARTY_BUNDLE_OF_BALLOON_TILE = 456
    PARTY_PRESENT = 457
    SAND_FALL_BLOCK = 458
    SNOW_FALL_BLOCK = 459
    SNOW_CLOUD = 460
    SAND_DRIP = 461
    DJINN_LAMP = 462
    DEFENDERS_FORGE = 463
    WAR_TABLE = 464
    WAR_TABLE_BANNER = 465
    ELDER_CRYSTAL_STAND = 466
    CONTAINERS2 = 467
    FAKE_CONTAINERS2 = 468
    TABLES2 = 469
    # New 1.4 stuff, adapted from: https://github.com/TerraMap/windows/blob/master/Data/tiles.xml
    DISPLAY_DOLL = 470
    WEAPON_RACK_2 = 471
    IRON_BRICK = 472
    LEAD_BRICK = 473
    LESION_BLOCK = 474
    HAT_RACK = 475
    GOLF_CUP = 476
    MOWED_GOLF_GRASS = 477
    CRIMSTONE_BRICK = 478
    SMOOTH_SANDSTONE = 479
    BLOOD_MOON_MONOLITH = 480
    CRACKED_BLUE_DUNGEON_BRICK = 481
    CRACKED_GREEN_DUNGEON_BRICK = 482
    CRACKED_PINK_DUNGEON_BRICK = 483
    ROLLING_CACTUS = 484
    ANTLION_LARVA = 485
    DRUM_SET = 486
    PICNIC_TABLE = 487
    FALLEN_LOG = 488
    PIN_WHEEL = 489
    WEATHER_VANE = 490
    VOID_VAULT = 491
    GOLF_GRASS_HALLOWED = 492
    GOLF_CUP_FLAG = 493
    GOLF_TEE = 494
    SHELL_PILE = 495
    ANTI_PORTAL_BLOCK = 496
    TOILETS = 497
    SPIDER_NEST_BLOCK = 498
    DECAY_CHAMBER = 499
    SOLAR_BRICK = 500
    VORTEX_BRICK = 501
    NEBULA_BRICK = 502
    STARDUST_BRICK = 503
    MYSTIC_SNAKE_ROPE = 504
    GOLD_FISH_BOWL = 505
    BAST_STATUE = 506
    GOLD_STARRY_BLOCK = 507
    BLUE_STARRY_BLOCK = 508
    VOID_MONOLITH = 509
    ARROW_SIGN = 510
    PAINTED_ARROW_SIGN = 511
    GREEN_MOSS_BRICK = 512
    BROWN_MOSS_BRICK = 513
    RED_MOSS_BRICK = 514
    BLUE_MOSS_BRICK = 515
    PURPLE_MOSS_BRICK = 516
    LAVA_MOS_SBRICK = 517
    LILY_PAD = 518
    CATTAIL = 519
    PLATE = 520
    BLACK_DRAGONFLY_JAR = 521
    BLUE_DRAGONFLY_JAR = 522
    GREEN_DRAGONFLY_JAR = 523
    ORANGE_DRAGONFLY_JAR = 524
    RED_DRAGONFLY_JAR = 525
    YELLOW_DRAGONFLY_JAR = 526
    GOLD_DRAGONFLY_JAR = 527
    MUSHROOMVINES = 528
    SEA_OATS = 529
    OASIS_PLANTS = 530
    BOULDER_STATUE = 531
    MAGGOT_CAGE = 532
    RAT_CAGE = 533
    KRYPTON_MOSS = 534
    KRYPTON_MOSS_BRICK = 535
    XENON_MOSS = 536
    XENON_MOSS_BRICK = 537
    LADYBUG_CAGE = 538
    ARGON_MOSS = 539
    ARGON_MOSS_BRICK = 540
    ECHO_BLOCK = 541
    OWL_CAGE = 542
    PUPFISH_BOWL = 543
    GOLD_LADYBUG_CAGE = 544
    LAWN_FLAMINGO = 545
    GRATE = 546
    POTTED_PLANTS_1 = 547
    POTTED_PLANTS_2 = 548
    SEAWEED = 549
    TURTLE_CAGE = 550
    JUNGLE_TURTLE_CAGE = 551
    SANDCASTLES = 552
    GREBE_CAGE = 553
    SEAGULL_CAGE = 554
    WATER_STRIDER_CAGE = 555
    GOLD_WATER_STRIDER_CAGE = 556
    GRATE_CLOSED = 557
    SEAHORSE_CAGE = 558
    GOLD_SEAHORSE_CAGE = 559
    GOLF_TROPHIES = 560
    MARBLE_COLUMN = 561
    BAMBOO = 562
    LARGE_BAMBOO = 563
    PLASMA_LAMP = 564
    FOG_MACHINE = 565
    AMBER_STONE_BLOCK = 566
    GARDEN_GNOME = 567
    PINK_FAIRY_JAR = 568
    GREEN_FAIRY_JAR = 569
    BLUE_FAIRY_JAR = 570
    BAMBOO_TREE = 571
    SOUL_BOTTLES = 572
    TATTERED_WOOD_SIGN = 573
    BOREAL_BEAM = 574
    RICH_MAHOGANY_BEAM = 575
    GRANITE_COLUMN = 576
    SANDSTONE_COLUMN = 577
    MUSHROOM_BEAM = 578
    ROCK_GOLEM_HEAD = 579
    HELL_BUTTERFLY_JAR = 580
    LAVAFLY_IN_A_BOTTLE = 581
    MAGMA_SNAIL_CAGE = 582
    TREE_TOPAZ = 583
    TREE_AMETHYST = 584
    TREE_SAPPHIRE = 585
    TREE_EMERALD = 586
    TREE_RUBY = 587
    TREE_DIAMOND = 588
    TREE_AMBER = 589
    GEM_SAPLINGS = 590
    POTS_SUSPENDED = 591
    HANGING_BRAZIER = 592
    MINI_VOLCANO = 593
    LARGE_VOLCANO = 594
    VANITY_TREE_SAKURA_SAPLINGS = 595
    VANITY_TREE_SAKURA = 596
    TELEPORTATION_PYLON = 597
    LAVAFISH_BOWL = 598
    AMETHYST_BUNNY_CAGE = 599
    TOPAZ_BUNNY_CAGE = 600
    SAPPHIRE_BUNNY_CAGE = 601
    EMERALD_BUNNY_CAGE = 602
    RUBY_BUNNY_CAGE = 603
    DIAMOND_BUNNY_CAGE = 604
    AMBER_BUNNY_CAGE = 605
    AMETHYST_SQUIRREL_CAGE = 606
    TOPAZ_SQUIRREL_CAGE = 607
    SAPPHIRE_SQUIRREL_CAGE = 608
    EMERALD_SQUIRREL_CAGE = 609
    RUBY_SQUIRREL_CAGE = 610
    DIAMOND_SQUIRREL_CAGE = 611
    AMBER_SQUIRREL_CAGE = 612
    POTTEDLAVAPLANTS = 613
    POTTED_EMBER_TENDRILS = 614
    VANITY_TREE_WILLOW_SAPLINGS = 615
    VANITY_TREE_YELLOW_WILLOW = 616
    MASTER_TROPHY_BASE = 617
    STONE_ACCENT_SLAB = 618
    TRUFFLE_WORM_CAGE = 619
    PRISMATIC_LACEWING_JAR = 620
    SLICE_OF_CAKE = 621
    TEAPOT = 622
    POTTED_CRYSTAL_PLANTS = 623
    ABIGAIL_FLOWER = 624
    VIOLETMOSS = 625
    VIOLETMOSSBRICK = 626
    RAINBOWMOSS = 627
    RAINBOWMOSSBRICK = 628
    STINKBUGCAGE = 629
    STINKBUGHOUSINGBLOCKER = 630
    STINKBUGHOUSINGBLOCKERECHO = 631
    SCARLETMACAWCAGE = 632
    ASHGRASS = 633
    TREEASH = 634
    ASHWOOD = 635
    CORRUPTVINES = 636
    ASHPLANTS = 637
    ASHVINES = 638
    MANACRYSTAL = 639
    BLUEMACAWCAGE = 640
    REEFBLOCK = 641
    CHLOROPHYTEEXTRACTINATOR = 642
    TOUCANCAGE = 643
    YELLOWCOCKATIELCAGE = 644
    GRAYCOCKATIELCAGE = 645
    SHADOWCANDLE = 646
    LARGEPILESECHO = 647
    LARGEPILES2ECHO = 648
    SMALLPILES2X1ECHO = 649
    SMALLPILES1X1ECHO = 650
    PLANTDETRITUS3X2ECHO = 651
    PLANTDETRITUS2X2ECHO = 652
    POTSECHO = 653
    TNTBARREL = 654
    PLANTERATHORNS = 655
    GLOWTULIP = 656
    ECHOMONOLITH = 657
    SHIMMERMONOLITH = 658
    SHIMMERBLOCK = 659
    SHIMMERFLYINABOTTLE = 660
    CORRUPTJUNGLEGRASS = 661
    CRIMSONJUNGLEGRASS = 662
    MOONDIAL = 663
    BOUNCYBOULDER = 664
    LIFECRYSTALBOULDER = 665
    POOPBLOCK = 666
    SHIMMERBRICK = 667
    DIRTIESTBLOCK = 668
    LUNARRUSTBRICK = 669
    DARKCELESTIALBRICK = 670
    ASTRABRICK = 671
    COSMICEMBERBRICK = 672
    CRYOCOREBRICK = 673
    MERCURYBRICK = 674
    STARROYALEBRICK = 675
    HEAVENFORGEBRICK = 676
    ANCIENTBLUEBRICK = 677
    ANCIENTGREENBRICK = 678
    ANCIENTPINKBRICK = 679
    ANCIENTGOLDBRICK = 680
    ANCIENTSILVERBRICK = 681
    ANCIENTCOPPERBRICK = 682
    ANCIENTOBSIDIANBRICK = 683
    ANCIENTHELLSTONEBRICK = 684
    ANCIENTCOBALTBRICK = 685
    ANCIENTMYTHRILBRICK = 686
    LAVAMOSSBLOCK = 687
    ARGONMOSSBLOCK = 688
    KRYPTONMOSSBLOCK = 689
    XENONMOSSBLOCK = 690
    VIOLETMOSSBLOCK = 691
    RAINBOWMOSSBLOCK = 692

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"