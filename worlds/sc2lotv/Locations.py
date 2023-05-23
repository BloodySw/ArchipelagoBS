from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld
from .Options import get_option_value

from BaseClasses import Location

SC2LOTV_LOC_ID_OFFSET = 12000


class SC2LotVLocation(Location):
    game: str = "Starcraft2LotV"


class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]
    rule: Callable = lambda state: True


def get_locations(multiworld: Optional[MultiWorld], player: Optional[int]) -> Tuple[LocationData, ...]:
    # Note: rules which are ended with or True are rules identified as needed later when restricted units is an option
    logic_level = get_option_value(multiworld, player, 'required_tactics')
    location_table: List[LocationData] = [
        LocationData("For Aiur!", "For Aiur!: Victory", SC2LOTV_LOC_ID_OFFSET + 100),
        LocationData("For Aiur!", "For Aiur!: First Hive", SC2LOTV_LOC_ID_OFFSET + 101),
        LocationData("For Aiur!", "For Aiur!: Second Hive", SC2LOTV_LOC_ID_OFFSET + 102),
        LocationData("For Aiur!", "For Aiur!: Third Hive", SC2LOTV_LOC_ID_OFFSET + 103),
		LocationData("For Aiur!", "For Aiur!: Fourth Hive", SC2LOTV_LOC_ID_OFFSET + 104),
        LocationData("The Growing Shadow", "The Growing Shadow: Victory", SC2LOTV_LOC_ID_OFFSET + 200,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   (logic_level > 0 or state._sc2lotv_has_anti_air(multiworld, player))),
        LocationData("The Growing Shadow", "The Growing Shadow: First Void Pylon", SC2LOTV_LOC_ID_OFFSET + 201),
		LocationData("The Growing Shadow", "The Growing Shadow: Second Void Pylon", SC2LOTV_LOC_ID_OFFSET + 202,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player)),
		LocationData("The Growing Shadow", "The Growing Shadow: Third Void Pylon", SC2LOTV_LOC_ID_OFFSET + 203,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player)),
        LocationData("The Spear of Adun", "The Spear of Adun: Victory", SC2LOTV_LOC_ID_OFFSET + 300,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   (logic_level > 0 or state._sc2lotv_has_anti_air(multiworld, player))),
        LocationData("The Spear of Adun", "The Spear of Adun: West Warp Gate Powered", SC2LOTV_LOC_ID_OFFSET + 301),
        LocationData("The Spear of Adun", "The Spear of Adun: Eeast Warp Gate Powered", SC2LOTV_LOC_ID_OFFSET + 302,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player)),
        LocationData("The Spear of Adun", "The Spear of Adun: South Warp Gate Powered", SC2LOTV_LOC_ID_OFFSET + 303,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player)),
        LocationData("Sky Shield", "Sky Shield: Victory", SC2LOTV_LOC_ID_OFFSET + 400,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Sky Shield", "Sky Shield: Center EMP Scrambler", SC2LOTV_LOC_ID_OFFSET + 401,
		             lambda state: state._sc2lotv_has_common_unit(multiworld, player)),
        LocationData("Sky Shield", "Sky Shield: North EMP Scrambler", SC2LOTV_LOC_ID_OFFSET + 402,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player)),
        LocationData("Sky Shield", "Sky Shield: South EMP Scrambler", SC2LOTV_LOC_ID_OFFSET + 403,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player)),
        LocationData("Brothers in Arms", "Brothers in Arms: Victory", SC2LOTV_LOC_ID_OFFSET + 500,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   (logic_level > 0 or state._sc2lotv_has_anti_air(multiworld, player))),
        LocationData("Brothers in Arms", "Brothers in Arms: Center Research Facility", SC2LOTV_LOC_ID_OFFSET + 501),
        LocationData("Brothers in Arms", "Brothers in Arms: North Research Facility", SC2LOTV_LOC_ID_OFFSET + 502,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Brothers in Arms", "Brothers in Arms: South Research Facility", SC2LOTV_LOC_ID_OFFSET + 503,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Amon's Reach", "Amon's Reach: Victory", SC2LOTV_LOC_ID_OFFSET + 600,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   (logic_level > 0 or state._sc2lotv_has_anti_air(multiworld, player))),
        LocationData("Amon's Reach", "Amon's Reach: Center Vault", SC2LOTV_LOC_ID_OFFSET + 601),
        LocationData("Amon's Reach", "Amon's Reach: North Vault", SC2LOTV_LOC_ID_OFFSET + 602,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   (logic_level > 0 or state._sc2lotv_has_anti_air(multiworld, player))),
        LocationData("Amon's Reach", "Amon's Reach: South West Vault", SC2LOTV_LOC_ID_OFFSET + 603,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   (logic_level > 0 or state._sc2lotv_has_anti_air(multiworld, player))),
        LocationData("Last Stand", "Last Stand: Victory", SC2LOTV_LOC_ID_OFFSET + 700,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player) and
                                   state._sc2lotv_defense_rating(multiworld, player) >= 3),
        LocationData("Last Stand", "Last Stand: All Zenith Stones", SC2LOTV_LOC_ID_OFFSET + 701,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Last Stand", "Last Stand: Some ridiculous amount of zerg because Karax couldn't start the extraction process sooner", SC2LOTV_LOC_ID_OFFSET + 702,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player) and
                                   state._sc2lotv_defense_rating(multiworld, player) >= 6),
        LocationData("Forbidden Weapon", "Forbidden Weapon: Victory", SC2LOTV_LOC_ID_OFFSET + 800,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   (logic_level > 0 or state._sc2lotv_has_anti_air(multiworld, player))),
        LocationData("Forbidden Weapon", "Forbidden Weapon: First Raw Solarite", SC2LOTV_LOC_ID_OFFSET + 801,
	                 lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   (logic_level > 0 or state._sc2lotv_has_anti_air(multiworld, player))),
        LocationData("Forbidden Weapon", "Forbidden Weapon: Second Raw Solarite", SC2LOTV_LOC_ID_OFFSET + 802),
		             lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   (logic_level > 0 or state._sc2lotv_has_anti_air(multiworld, player))),
        LocationData("Forbidden Weapon", "Forbidden Weapon: Third Raw Solarite", SC2LOTV_LOC_ID_OFFSET + 803,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   (logic_level > 0 or state._sc2lotv_has_anti_air(multiworld, player))),
        LocationData("Temple of Yurification", "Temple of Yurification: Victory", SC2LOTV_LOC_ID_OFFSET + 900,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Temple of Yurification", "Temple of Yurification: Titanic Warp Prism", SC2LOTV_LOC_ID_OFFSET + 901,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("The Infinite Cycle", "The Infinite Cycle: Victory", SC2LOTV_LOC_ID_OFFSET + 1000,
        LocationData("The Infinite Cycle", "The Infinite Cycle: First Xel'naga Relic", SC2LOTV_LOC_ID_OFFSET + 1003,
        LocationData("The Infinite Cycle", "The Infinite Cycle: Second Xel'naga Relic", SC2LOTV_LOC_ID_OFFSET + 1004,
        LocationData("The Infinite Cycle", "The Infinite Cycle: Third Xel'naga Relic", SC2LOTV_LOC_ID_OFFSET + 1005,
        LocationData("Harbinger of Oblivion", "Harbinger of Oblivion: Victory", SC2LOTV_LOC_ID_OFFSET + 1100,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Harbinger of Oblivion", "Harbinger of Oblivion: South Xel'naga Vessel", SC2LOTV_LOC_ID_OFFSET + 1101),
        LocationData("Harbinger of Oblivion", "Harbinger of Oblivion: Center Xel'naga Vessel", SC2LOTV_LOC_ID_OFFSET + 1102,
		             lambda state: state._sc2lotv_has_common_unit(multiworld, player)),
        LocationData("Harbinger of Oblivion", "Harbinger of Oblivion: North Xel'naga Vessel", SC2LOTV_LOC_ID_OFFSET + 1103,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player)),
        LocationData("Unsealing the Past", "Unsealing the Past: Victory", SC2LOTV_LOC_ID_OFFSET + 1200,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Unsealing the Past", "Unsealing the Past: South Power Core Housing", SC2LOTV_LOC_ID_OFFSET + 1201,
		             lambda state: state._sc2lotv_has_common_unit(multiworld, player)),
        LocationData("Unsealing the Past", "Unsealing the Past: East Power Core Housing", SC2LOTV_LOC_ID_OFFSET + 1202,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Purification", "Purification: Victory", SC2LOTV_LOC_ID_OFFSET + 1300,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Purification", "Purification: Purifier Warden", SC2LOTV_LOC_ID_OFFSET + 1301,
		             lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Steps of the Rite", "Steps of the Rite: Victory", SC2LOTV_LOC_ID_OFFSET + 1400,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Steps of the Rite", "Steps of the Rite: South Tal'darim Mothership", SC2LOTV_LOC_ID_OFFSET + 1401,
		             lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Steps of the Rite", "Steps of the Rite: North Tal'darim Mothership", SC2LOTV_LOC_ID_OFFSET + 1402,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Rak'Shir", "Rak'Shir: Victory", SC2LOTV_LOC_ID_OFFSET + 1500,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Rak'Shir", "Rak'Shir: South Slayn Elemental", SC2LOTV_LOC_ID_OFFSET + 1501,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Rak'Shir", "Rak'Shir: North Slayn Elemental", SC2LOTV_LOC_ID_OFFSET + 1502,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
		LocationData("Rak'Shir", "Rak'Shir: East Slayn Elemental", SC2LOTV_LOC_ID_OFFSET + 1503,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Templar's Charge", "Templar's Charge: Victory", SC2LOTV_LOC_ID_OFFSET + 1600,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Templar's Charge", "Templar's Charge: West Hybrid Stasis Chamber", SC2LOTV_LOC_ID_OFFSET + 1601,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Templar's Charge", "Templar's Charge: East Hybrid Stasis Chamber", SC2LOTV_LOC_ID_OFFSET + 1602,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Templar's Return", "Templar's Return: Victory", SC2LOTV_LOC_ID_OFFSET + 1700),
        LocationData("Templar's Return", "Templar's Return: First Khaydarian Crystal", SC2LOTV_LOC_ID_OFFSET + 1701),
        LocationData("Templar's Return", "Templar's Return: Second Khaydarian Crystal", SC2LOTV_LOC_ID_OFFSET + 1702),
        LocationData("The Host", "The Host: Victory", SC2LOTV_LOC_ID_OFFSET + 1800,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("The Host", "The Host: Nerazim Camp (East)", SC2LOTV_LOC_ID_OFFSET + 1801,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("The Host", "The Host: Purifier Camp (North)", SC2LOTV_LOC_ID_OFFSET + 1802,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("The Host", "The Host: Tal'darim Camp (West)", SC2LOTV_LOC_ID_OFFSET + 1803,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
		LocationData("Salvation", "Salvation: Victory", None,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player) and
                                   state._sc2lotv_defense_rating(multiworld, player) >= 6),
        LocationData("Dark Whispers", "Dark Whispers: Victory", SC2LOTV_LOC_ID_OFFSET + 1900,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Dark Whispers", "Dark Whispers: North Terran Pylon", SC2LOTV_LOC_ID_OFFSET + 1901,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Dark Whispers", "Dark Whispers: East Terran Pylon", SC2LOTV_LOC_ID_OFFSET + 1902,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Ghosts in the Fog", "Ghosts in the Fog: Victory", SC2LOTV_LOC_ID_OFFSET + 2000,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Ghosts in the Fog", "Ghosts in the Fog: South Gassy Rocks", SC2LOTV_LOC_ID_OFFSET + 2001,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Ghosts in the Fog", "Ghosts in the Fog: East Gassy Rocks", SC2LOTV_LOC_ID_OFFSET + 2002,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Ghosts in the Fog", "Ghosts in the Fog: West Gassy Rocks", SC2LOTV_LOC_ID_OFFSET + 2003,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Evil Awoken", "Evil Awoken: Victory", SC2LOTV_LOC_ID_OFFSET + 2100),
        LocationData("Evil Awoken", "Evil Awoken: First Particle Cannon", SC2LOTV_LOC_ID_OFFSET + 2101),
        LocationData("Evil Awoken", "Evil Awoken: Second Particle Cannon", SC2LOTV_LOC_ID_OFFSET + 2102),
        LocationData("Evil Awoken", "Evil Awoken: Third Particle Cannon", SC2LOTV_LOC_ID_OFFSET + 2103),
		LocationData("Evil Awoken", "Evil Awoken: Meet 'Tassadar'", SC2LOTV_LOC_ID_OFFSET + 2104),
        LocationData("Into the Void", "Into the Void: Victory", SC2LOTV_LOC_ID_OFFSET + 2200,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Into the Void", "Into the Void: First West Landing Site", SC2LOTV_LOC_ID_OFFSET + 2201,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Into the Void", "Into the Void: Second West Landing Site", SC2LOTV_LOC_ID_OFFSET + 2202,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
        LocationData("Into the Void", "Into the Void: First East Landing Site", SC2LOTV_LOC_ID_OFFSET + 2203,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
		LocationData("Into the Void", "Into the Void: Second East Landing Site", SC2LOTV_LOC_ID_OFFSET + 2204,
                     lambda state: state._sc2lotv_has_common_unit(multiworld, player) and
                                   state._sc2lotv_has_anti_air(multiworld, player)),
    ]

    beat_events = []

    for i, location_data in enumerate(location_table):
        # Removing all item-based logic on No Logic
        if logic_level == 2:
            location_data = location_data._replace(rule=Location.access_rule)
            location_table[i] = location_data
        # Generating Beat event locations
        if location_data.name.endswith(": Victory"):
            beat_events.append(
                location_data._replace(name="Beat " + location_data.name.rsplit(": ", 1)[0], code=None)
            )
    return tuple(location_table + beat_events)
