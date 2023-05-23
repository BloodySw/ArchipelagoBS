from typing import List, Set, Dict, Tuple, Optional, Callable
from BaseClasses import MultiWorld, Region, Entrance, Location
from .Locations import LocationData
from .Options import get_option_value
from .MissionTables import MissionInfo, mission_orders, vanilla_mission_req_table, alt_final_mission_locations, MissionPools
from .PoolFilter import filter_missions


def create_regions(multiworld: MultiWorld, player: int, locations: Tuple[LocationData, ...], location_cache: List[Location])\
        -> Tuple[Dict[str, MissionInfo], int, str]:
    locations_per_region = get_locations_per_region(locations)

    mission_order_type = get_option_value(multiworld, player, "mission_order")
    mission_order = mission_orders[mission_order_type]

    mission_pools = filter_missions(multiworld, player)

    regions = [create_region(multiworld, player, locations_per_region, location_cache, "Menu")]

    names: Dict[str, int] = {}

    if mission_order_type == 0:

        # Generating all regions and locations
        for region_name in vanilla_mission_req_table.keys():
            regions.append(create_region(multiworld, player, locations_per_region, location_cache, region_name))
        multiworld.regions += regions

        connect(multiworld, player, names, 'Menu', 'For Aiur!'),
        connect(multiworld, player, names, 'For Aiur!', 'The Growing Shadow',
                lambda state: state.has("Beat For Aiur!", player)),
        connect(multiworld, player, names, 'The Growing Shadow', 'The Spear of Adun',
                lambda state: state.has("Beat The Growing Shadow", player)),
        connect(multiworld, player, names, 'The Spear of Adun', 'Sky Shield',
                lambda state: state.has("Beat The Spear of Adun", player)),
		connect(multiworld, player, names, 'The Spear of Adun', "Amon's Reach",
                lambda state: state.has("Beat The Spear of Adun", player)),
		
		connect(multiworld, player, names, 'The Spear of Adun', "Dark Whispers",
                lambda state: state.has("Beat The Spear of Adun", player)),				
        connect(multiworld, player, names, 'Dark Whispers', 'Ghosts in the Fog',
                lambda state: state.has("Beat Dark Whispers", player)),
		connect(multiworld, player, names, 'Ghosts in the Fog', 'Evil Awoken',
                lambda state: state.has("Beat Ghosts in the Fog", player)),
		connect(multiworld, player, names, 'Sky Shield', 'Brothers in Arms',
                lambda state: state.has("Beat Sky Shield", player)),
		connect(multiworld, player, names, "Amon's Reach", "Last Stand",
                lambda state: state.has("Beat Amon's Reach", player)),
		connect(multiworld, player, names, 'The Spear of Adun', 'Forbidden Weapon',
                lambda state: state.has('Beat The Spear of Adun', player) and (
                        state.has('Beat Brothers in Arms', player) or state.has('Beat Last Stand', player))),
		connect(multiworld, player, names, 'Forbidden Weapon', 'Temple of Yurification',
                lambda state: state.has('Beat Temple of Yurification', player) and (
                        state.has('Beat Brothers in Arms', player) and state.has('Beat Last Stand', player))),
		connect(multiworld, player, names, "Temple of Yurification", "The Infinite Cycle",
                lambda state: state.has("Beat Temple of Yurification", player)),
		connect(multiworld, player, names, "The Infinite Cycle", "Harbinger of Oblivion",
                lambda state: state.has("Beat The Infinite Cycle", player)),
		connect(multiworld, player, names, "Harbinger of Oblivion", "Unsealing the Past",
                lambda state: state.has("Beat Harbinger of Oblivion", player)),
		connect(multiworld, player, names, "Harbinger of Oblivion", "Into the Void",
                lambda state: state.has("Beat Harbinger of Oblivion", player)),		
		connect(multiworld, player, names, "Unsealing the Past", "Purification",
                lambda state: state.has("Beat Unsealing the Past", player)),
		connect(multiworld, player, names, "Harbinger of Oblivion", "Steps of the Rite",
                lambda state: state.has("Beat Harbinger of Oblivion", player)),
		connect(multiworld, player, names, "Steps of the Rite", "Rak'Shir",
                lambda state: state.has("Beat Steps of the Rite", player)),
		connect(multiworld, player, names, 'Harbinger of Oblivion', "Templar's Charge",
                lambda state: state.has('Beat Harbinger of Oblivion', player) and (
                        state.has("Beat Purification", player) or state.has("Beat Rak'Shir", player))),
		connect(multiworld, player, names, "Templar's Charge", "Templar's Return",
                lambda state: state.has("Beat Templar's Charge", player) and (
                        state.has("Beat Purification", player) and state.has("Beat Rak'Shir", player))),
		connect(multiworld, player, names, "Templar's Return", "The Host",
                lambda state: state.has("Beat Templar's Return", player)),
		connect(multiworld, player, names, "The Host", "Salvation",
                lambda state: state.has("Beat The Host", player))

        return vanilla_mission_req_table, 23, 'Salvation: Victory'

    else:
        missions = []

        remove_prologue = mission_order_type == 1 and not get_option_value(multiworld, player, "shuffle_prologue")

        final_mission = mission_pools[MissionPools.FINAL][0]

        # Determining if missions must be removed
        mission_pool_size = sum(len(mission_pool) for mission_pool in mission_pools.values())
        removals = len(mission_order) - mission_pool_size
        # Removing entire Prophecy chain on vanilla shuffled when not shuffling protoss
        if remove_prologue:
            removals -= 3

        # Initial fill out of mission list and marking all-in mission
        for mission in mission_order:
            # Removing extra missions if mission pool is too small
            if 0 < mission.removal_priority <= removals or mission.category == 'Whispers' and remove_prophecy:
                missions.append(None)
            elif mission.type == MissionPools.FINAL:
                missions.append(final_mission)
            else:
                missions.append(mission.type)

        no_build_slots = []
        easy_slots = []
        medium_slots = []
        hard_slots = []

        # Search through missions to find slots needed to fill
        for i in range(len(missions)):
            if missions[i] is None:
                continue
            if missions[i] == MissionPools.STARTER:
                no_build_slots.append(i)
            elif missions[i] == MissionPools.EASY:
                easy_slots.append(i)
            elif missions[i] == MissionPools.MEDIUM:
                medium_slots.append(i)
            elif missions[i] == MissionPools.HARD:
                hard_slots.append(i)

        # Add no_build missions to the pool and fill in no_build slots
        missions_to_add = mission_pools[MissionPools.STARTER]
        if len(no_build_slots) > len(missions_to_add):
            raise Exception("There are no valid No-Build missions.  Please exclude fewer missions.")
        for slot in no_build_slots:
            filler = multiworld.random.randint(0, len(missions_to_add) - 1)

            missions[slot] = missions_to_add.pop(filler)

        # Add easy missions into pool and fill in easy slots
        missions_to_add = missions_to_add + mission_pools[MissionPools.EASY]
        if len(easy_slots) > len(missions_to_add):
            raise Exception("There are not enough Easy missions to fill the campaign.  Please exclude fewer missions.")
        for slot in easy_slots:
            filler = multiworld.random.randint(0, len(missions_to_add) - 1)

            missions[slot] = missions_to_add.pop(filler)

        # Add medium missions into pool and fill in medium slots
        missions_to_add = missions_to_add + mission_pools[MissionPools.MEDIUM]
        if len(medium_slots) > len(missions_to_add):
            raise Exception("There are not enough Easy and Medium missions to fill the campaign.  Please exclude fewer missions.")
        for slot in medium_slots:
            filler = multiworld.random.randint(0, len(missions_to_add) - 1)

            missions[slot] = missions_to_add.pop(filler)

        # Add hard missions into pool and fill in hard slots
        missions_to_add = missions_to_add + mission_pools[MissionPools.HARD]
        if len(hard_slots) > len(missions_to_add):
            raise Exception("There are not enough missions to fill the campaign.  Please exclude fewer missions.")
        for slot in hard_slots:
            filler = multiworld.random.randint(0, len(missions_to_add) - 1)

            missions[slot] = missions_to_add.pop(filler)

        # Generating regions and locations from selected missions
        for region_name in missions:
            regions.append(create_region(multiworld, player, locations_per_region, location_cache, region_name))
        multiworld.regions += regions

        # Mapping original mission slots to shifted mission slots when missions are removed
        slot_map = []
        slot_offset = 0
        for position, mission in enumerate(missions):
            slot_map.append(position - slot_offset + 1)
            if mission is None:
                slot_offset += 1

        # Loop through missions to create requirements table and connect regions
        # TODO: Handle 'and' connections
        mission_req_table = {}

        for i, mission in enumerate(missions):
            if mission is None:
                continue
            connections = []
            for connection in mission_order[i].connect_to:
                required_mission = missions[connection]
                if connection == -1:
                    connect(multiworld, player, names, "Menu", mission)
                elif required_mission is None:
                    continue
                else:
                    connect(multiworld, player, names, required_mission, mission,
                            (lambda name, missions_req: (lambda state: state.has(f"Beat {name}", player) and
                                                                       state._sc2lotv_cleared_missions(multiworld, player,
                                                                                                      missions_req)))
                            (missions[connection], mission_order[i].number))
                    connections.append(slot_map[connection])

            mission_req_table.update({mission: MissionInfo(
                vanilla_mission_req_table[mission].id, connections, mission_order[i].category,
                number=mission_order[i].number,
                completion_critical=mission_order[i].completion_critical,
                or_requirements=mission_order[i].or_requirements)})

        final_mission_id = vanilla_mission_req_table[final_mission].id

        # Changing the completion condition for alternate final missions into an event
        if final_mission != 'Salvation':
            final_location = alt_final_mission_locations[final_mission]
            # Final location should be near the end of the cache
            for i in range(len(location_cache) - 1, -1, -1):
                if location_cache[i].name == final_location:
                    location_cache[i].locked = True
                    location_cache[i].event = True
                    location_cache[i].address = None
                    break
        else:
            final_location = 'All-In: Victory'

        return mission_req_table, final_mission_id, final_location

def create_location(player: int, location_data: LocationData, region: Region,
                    location_cache: List[Location]) -> Location:
    location = Location(player, location_data.name, location_data.code, region)
    location.access_rule = location_data.rule

    if id is None:
        location.event = True
        location.locked = True

    location_cache.append(location)

    return location


def create_region(multiworld: MultiWorld, player: int, locations_per_region: Dict[str, List[LocationData]],
                  location_cache: List[Location], name: str) -> Region:
    region = Region(name, player, multiworld)

    if name in locations_per_region:
        for location_data in locations_per_region[name]:
            location = create_location(player, location_data, region, location_cache)
            region.locations.append(location)

    return region


def connect(world: MultiWorld, player: int, used_names: Dict[str, int], source: str, target: str,
            rule: Optional[Callable] = None):
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (' ' * used_names[target])

    connection = Entrance(player, name, sourceRegion)

    if rule:
        connection.access_rule = rule

    sourceRegion.exits.append(connection)
    connection.connect(targetRegion)


def get_locations_per_region(locations: Tuple[LocationData, ...]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[LocationData]] = {}

    for location in locations:
        per_region.setdefault(location.region, []).append(location)

    return per_region
