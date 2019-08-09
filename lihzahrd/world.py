import uuid
import math
from . import header as h


class World:
    """The Python representation of a Terraria world."""
    def __init__(self,
                 version: h.Version,
                 savefile_type: int,
                 revision: int,
                 is_favorite: bool,
                 name: str,
                 generator: h.GeneratorInfo,
                 uuid_: uuid.UUID,
                 id_: int,
                 bounds: h.Rect,
                 size: h.Coordinates,
                 is_expert: bool,
                 created_on,
                 styles: h.Styles,
                 backgrounds: h.Backgrounds,
                 spawn_point: h.Coordinates,
                 underground_level: float,
                 cavern_level: float,
                 time: h.Time,
                 events: h.Events,
                 dungeon_point: h.Coordinates,
                 world_evil: h.WorldEvilType,
                 saved_npcs: h.SavedNPCs,
                 altars_smashed: h.AltarsSmashed,
                 is_hardmode: bool,
                 shadow_orbs: h.ShadowOrbs,
                 bosses_defeated: h.BossesDefeated,
                 anglers_quest: h.AnglerQuest,
                 clouds: h.Clouds,
                 cultist_delay: int):

        self.version: h.Version = version
        """The game version when this savefile was last saved."""

        self.savefile_type = savefile_type
        """The format of the save file. Should be 2 for all versions following 1.2."""

        self.revision: int = revision
        """The number of times this world was saved."""

        self.is_favorite: bool = is_favorite
        """If the world is marked as favorite or not."""

        self.name: str = name
        """The name the world was given at creation. Doesn't always match the filename."""

        self.generator: h.GeneratorInfo = generator
        """Information about the generation of this world."""

        self.uuid: uuid.UUID = uuid_
        """The Universally Unique ID of this world."""

        self.id: int = id_
        """The world id. Used to name the minimap file."""

        self.bounds: h.rect.Rect = bounds
        """The world size in pixels."""

        self.size: h.Coordinates = size
        """The world size in tiles."""

        self.is_expert: bool = is_expert
        """If the world is in expert mode or not."""

        self.created_on = created_on
        """The date and time this world was created in."""

        self.styles: h.Styles = styles
        """The styles of various world elements."""

        self.backgrounds: h.Backgrounds = backgrounds
        """The backgrounds of the various biomes."""

        self.spawn_point: h.Coordinates = spawn_point
        """The coordinates of the spawn point."""

        self.underground_level: float = underground_level
        """The depth at which the underground biome starts."""

        self.cavern_level: float = cavern_level
        """The depth at which the cavern biome starts."""

        self.time: h.Time = time
        """Game time related information."""

        self.events: h.Events = events
        """Currently ongoing world events."""

        self.dungeon_point: h.Coordinates = dungeon_point
        """The Old Man spawn point."""

        self.world_evil: h.WorldEvilType = world_evil
        """Whether the world has Corruption or Crimson."""

        self.saved_npcs: h.SavedNPCs = saved_npcs
        """The NPCs that were rescued by the player."""

        self.altars_smashed: h.AltarsSmashed = altars_smashed
        """Information related to the destruction of Demon Altars with a Pwnhammer."""

        self.is_hardmode: bool = is_hardmode
        """Whether or not the world is in hardmode."""

        self.shadow_orbs: h.ShadowOrbs = shadow_orbs
        """Information related to the Shadow Orbs or Crimson Hearts in the world."""

        self.bosses_defeated: h.BossesDefeated = bosses_defeated
        """Which bosses have been defeated in the world."""

        self.anglers_quest: h.AnglerQuest = anglers_quest
        """Information about today's Angler's Quest."""

        self.clouds: h.Clouds = clouds
        self.cultist_delay: int = cultist_delay

    def __repr__(self):
        return f'<World "{self.name}">'

    @property
    def crimson_hearts(self) -> h.shadoworbs.ShadowOrbs:
        return self.shadow_orbs

    @crimson_hearts.setter
    def crimson_hearts(self, value):
        self.shadow_orbs = value

    @classmethod
    def create_from_file(cls, file):
        """Create a World object from a .wld file."""
        # This code is a mess.

        f = h.filereader.FileReader(file)

        version = h.version.Version(f.int4())
        relogic = f.string(7)
        savefile_type = f.uint1()
        if version != h.version.Version("1.3.5.3") or relogic != "relogic" or savefile_type != 2:
            raise NotImplementedError("This parser can only read Terraria 1.3.5.3 save files.")

        revision = f.uint4()
        is_favorite = f.uint8() != 0

        # Pointers and tileframeimportant
        _ = [f.int4() for _ in range(f.int2())]
        tileframeimportant_size = math.ceil(f.int2() / 8)
        _ = []
        for _ in range(tileframeimportant_size):
            current_bit = f.bit()
            _ = [*_, *current_bit]

        name = f.string()

        generator = h.GeneratorInfo(f.string(), f.int4())

        uuid_ = f.uuid()
        id_ = f.int8()
        bounds = f.rect()
        world_size = h.Coordinates(y=f.int4(), x=f.int4())
        is_expert = f.bool()
        created_on = f.datetime()

        world_styles = h.Styles(moon=h.moonstyle.MoonStyle(f.uint1()),
                                trees=h.fourpartsplit.FourPartSplit(separators=[f.int4(), f.int4(), f.int4()],
                                                                    properties=[f.int4(),
                                                                                f.int4(),
                                                                                f.int4(),
                                                                                f.int4()]),
                                moss=h.fourpartsplit.FourPartSplit(separators=[f.int4(), f.int4(), f.int4()],
                                                                   properties=[f.int4(),
                                                                               f.int4(),
                                                                               f.int4(),
                                                                               f.int4()]))

        bg_underground_snow = f.int4()
        bg_underground_jungle = f.int4()
        bg_hell = f.int4()

        spawn_point = h.Coordinates(f.int4(), f.int4())
        underground_level = f.double()
        cavern_level = f.double()

        current_time = f.double()
        is_daytime = f.bool()
        moon_phase = h.MoonPhase(f.uint4())

        blood_moon = f.bool()
        eclipse = f.bool()

        dungeon_point = h.Coordinates(f.int4(), f.int4())
        world_evil = h.WorldEvilType(f.bool())

        defeated_eye_of_cthulhu = f.bool()  # Possibly. I'm not sure.
        defeated_eater_of_worlds = f.bool()  # Possibly. I'm not sure.
        defeated_skeletron = f.bool()  # Possibly. I'm not sure.
        defeated_queen_bee = f.bool()
        defeated_the_twins = f.bool()
        defeated_the_destroyer = f.bool()
        defeated_skeletron_prime = f.bool()
        defeated_any_mechnical_boss = f.bool()
        defeated_plantera = f.bool()
        defeated_golem = f.bool()
        defeated_king_slime = f.bool()

        saved_goblin_tinkerer = f.bool()
        saved_wizard = f.bool()
        saved_mechanic = f.bool()

        defeated_goblin_army = f.bool()
        defeated_clown = f.bool()
        defeated_frost_moon = f.bool()
        defeated_pirates = f.bool()

        shadow_orbs = h.ShadowOrbs(smashed_at_least_once=f.bool(),
                                   spawn_meteorite=f.bool(),
                                   evil_boss_counter=f.int4())

        smashed_altars_count = f.int4()

        is_hardmode = f.bool()

        invasion_delay = f.int4()
        invasion_size = f.int4()
        invasion_type = h.InvasionType(f.int4())
        invasion_position = f.double()

        time_left_slime_rain = f.double()

        sundial_cooldown = f.uint1()

        rain = h.Rain(is_active=f.bool(), time_left=f.int4(), max_rain=f.single())

        hardmode_ore_1 = h.HardmodeTier1Ore(f.int4())
        hardmode_ore_2 = h.HardmodeTier2Ore(f.int4())
        hardmode_ore_3 = h.HardmodeTier3Ore(f.int4())
        altars_smashed = h.AltarsSmashed(count=smashed_altars_count,
                                         ore_tier1=hardmode_ore_1,
                                         ore_tier2=hardmode_ore_2,
                                         ore_tier3=hardmode_ore_3)

        bg_forest = f.int1()
        bg_corruption = f.int1()
        bg_jungle = f.int1()
        bg_snow = f.int1()
        bg_hallow = f.int1()
        bg_crimson = f.int1()
        bg_desert = f.int1()
        bg_ocean = f.int1()

        backgrounds = h.Backgrounds(bg_underground_snow=bg_underground_snow,
                                    bg_underground_jungle=bg_underground_jungle,
                                    bg_hell=bg_hell,
                                    bg_forest=bg_forest,
                                    bg_corruption=bg_corruption,
                                    bg_jungle=bg_jungle,
                                    bg_snow=bg_snow,
                                    bg_hallow=bg_hallow,
                                    bg_crimson=bg_crimson,
                                    bg_desert=bg_desert,
                                    bg_ocean=bg_ocean)

        clouds = h.Clouds(bg_cloud=f.int4(), cloud_number=f.int2(), wind_speed=f.single())

        angler_today_quest_completed_by_count = f.uint1()
        angler_today_quest_completed_by = []
        for _ in range(angler_today_quest_completed_by_count):
            angler_today_quest_completed_by.append(f.string())

        saved_angler = f.bool()

        angler_today_quest_target = h.AnglerQuestFish(f.int4())
        anglers_quest = h.AnglerQuest(current_goal=angler_today_quest_target,
                                      completed_by=angler_today_quest_completed_by)

        saved_stylist = f.bool()
        saved_tax_collector = f.bool()

        invasion_size_start = f.int4()  # ???
        invasion = h.Invasion(delay=invasion_delay,
                              size=invasion_size,
                              type_=invasion_type,
                              position=invasion_position,
                              size_start=invasion_size_start)

        cultist_delay = f.int4()  # ???
        mob_types_count = f.int2()
        mob_kills = {}
        for mob_id in range(mob_types_count):
            mob_kills[mob_id] = f.int4()

        fast_forward_time = f.bool()
        time = h.Time(current=current_time,
                      is_daytime=is_daytime,
                      moon_phase=moon_phase,
                      sundial_cooldown=sundial_cooldown,
                      fast_forward_time=fast_forward_time)

        defeated_duke_fishron = f.bool()
        defeated_moon_lord = f.bool()
        defeated_pumpking = f.bool()
        defeated_mourning_wood = f.bool()
        defeated_ice_queen = f.bool()
        defeated_santa_nk1 = f.bool()
        defeated_everscream = f.bool()
        defeated_pillars = h.PillarsInfo(solar=f.bool(), vortex=f.bool(), nebula=f.bool(), stardust=f.bool())

        lunar_events = h.LunarEvents(pillars_present=h.PillarsInfo(solar=f.bool(),
                                                                   vortex=f.bool(),
                                                                   nebula=f.bool(),
                                                                   stardust=f.bool()),
                                     are_active=f.bool())

        party_center_active = f.bool()
        party_natural_active = f.bool()
        party_cooldown = f.int4()
        partying_npcs_count = f.int4()
        partying_npcs = []
        for _ in range(partying_npcs_count):
            partying_npcs.append(f.int4())
        party = h.Party(thrown_by_party_center=party_center_active,
                        thrown_by_npcs=party_natural_active,
                        cooldown=party_cooldown,
                        partying_npcs=partying_npcs)

        sandstorm = h.Sandstorm(is_active=f.bool(),
                                time_left=f.int4(),
                                severity=f.single(),
                                intended_severity=f.single())

        events = h.Events(blood_moon=blood_moon,
                          solar_eclipse=eclipse,
                          invasion=invasion,
                          slime_rain=time_left_slime_rain,
                          rain=rain,
                          party=party,
                          sandstorm=sandstorm,
                          lunar_events=lunar_events)

        saved_bartender = f.bool()
        saved_npcs = h.SavedNPCs(goblin_tinkerer=saved_goblin_tinkerer,
                                 wizard=saved_wizard,
                                 mechanic=saved_mechanic,
                                 angler=saved_angler,
                                 stylist=saved_stylist,
                                 tax_collector=saved_tax_collector,
                                 bartender=saved_bartender)

        old_ones_army = h.OldOnesArmyTiers(f.bool(), f.bool(), f.bool())

        bosses_defeated = h.BossesDefeated(eye_of_cthulhu=defeated_eye_of_cthulhu,
                                           eater_of_worlds=defeated_eater_of_worlds,
                                           skeletron=defeated_skeletron,
                                           queen_bee=defeated_queen_bee,
                                           the_twins=defeated_the_twins,
                                           the_destroyer=defeated_the_destroyer,
                                           skeletron_prime=defeated_skeletron_prime,
                                           any_mechnical_boss=defeated_any_mechnical_boss,
                                           plantera=defeated_plantera,
                                           golem=defeated_golem,
                                           king_slime=defeated_king_slime,
                                           goblin_army=defeated_goblin_army,
                                           clown=defeated_clown,
                                           frost_moon=defeated_frost_moon,
                                           pirates=defeated_pirates,
                                           duke_fishron=defeated_duke_fishron,
                                           moon_lord=defeated_moon_lord,
                                           pumpking=defeated_pumpking,
                                           mourning_wood=defeated_mourning_wood,
                                           ice_queen=defeated_ice_queen,
                                           santa_nk1=defeated_santa_nk1,
                                           everscream=defeated_everscream,
                                           lunar_pillars=defeated_pillars,
                                           old_ones_army=old_ones_army)
        # Tile data starts here
        world = World(version=version, savefile_type=savefile_type, revision=revision, is_favorite=is_favorite,
                      name=name, generator=generator, uuid_=uuid_, id_=id_, bounds=bounds, size=world_size,
                      is_expert=is_expert, created_on=created_on, styles=world_styles, backgrounds=backgrounds,
                      spawn_point=spawn_point, underground_level=underground_level, cavern_level=cavern_level,
                      time=time, events=events, dungeon_point=dungeon_point, world_evil=world_evil,
                      saved_npcs=saved_npcs, altars_smashed=altars_smashed, is_hardmode=is_hardmode,
                      shadow_orbs=shadow_orbs, bosses_defeated=bosses_defeated, anglers_quest=anglers_quest,
                      clouds=clouds, cultist_delay=cultist_delay)
        breakpoint()
        return world
