from BaseClasses import Item, ItemClassification, MultiWorld
import typing

from .Options import get_option_value
from .MissionTables import vanilla_mission_req_table


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    type: typing.Optional[str]
    number: typing.Optional[int]
    classification: ItemClassification = ItemClassification.useful
    quantity: int = 1
    parent_item: str = None


class StarcraftLotVItem(Item):
    game: str = "Starcraft 2 Legacy of the Void"


def get_full_item_list():
    return item_table


SC2LOTV_ITEM_ID_OFFSET = 12000

item_table = {
    "Aiur Zealot": ItemData(0 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 0),
    "Centurion": ItemData(1 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 1),
    "Sentinel": ItemData(2 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 2, classification=ItemClassification.progression),
    "Stalker": ItemData(3 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 3, classification=ItemClassification.progression),
    "Dragoon": ItemData(4 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 4),
    "Adept": ItemData(5 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 5),
    "Dark Templar": ItemData(6 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 6),
    "Avenger": ItemData(7 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 7),
    "Blood Hunter": ItemData(8 + SC2LOTV_ITEM_ID_OFFSET, "Unit"),
    "Sentry": ItemData(9 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 9),
    "Energizer": ItemData(10 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 10),
    "Havoc": ItemData(11 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 11),
    "Immortal": ItemData(12 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 12, classification=ItemClassification.progression),
    "Annihilator": ItemData(13 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 13),
    "Vanguard": ItemData(14 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 14),
    "Phoenix": ItemData(15 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 15),
    "Corsair": ItemData(16 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 16),
    "Mirage": ItemData(17 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 17),
	"High Templar": ItemData(18 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 18),
	"Dark Archon": ItemData(19 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 19),
	"Ascendant": ItemData(20 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 20),
	"Void Ray": ItemData(21 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 21, classification=ItemClassification.progression),
	"Destroyer": ItemData(22 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 22),
	"Arbiter": ItemData(23 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 23),
	"Colossus": ItemData(24 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 24, classification=ItemClassification.progression),
	"Reaver": ItemData(25 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 25),
	"Wrathwalker": ItemData(26 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 26),
	"Carrier": ItemData(27 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 27, classification=ItemClassification.progression),
	"Tempest": ItemData(28 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 28),
	"Mothership": ItemData(29 + SC2LOTV_ITEM_ID_OFFSET, "Unit", 29),
	

    "Progressive Ground Weapon": ItemData(100 + SC2LOTV_ITEM_ID_OFFSET, "Upgrade", 0, quantity=3),
    "Progressive Ground Armor": ItemData(102 + SC2LOTV_ITEM_ID_OFFSET, "Upgrade", 2, quantity=3),
	"Progressive Shield": ItemData(103 + SC2LOTV_ITEM_ID_OFFSET, "Upgrade", 4, quantity=3),
    "Progressive Air Weapon": ItemData(104 + SC2LOTV_ITEM_ID_OFFSET, "Upgrade", 6, quantity=3),
    "Progressive Air Armor": ItemData(105 + SC2LOTV_ITEM_ID_OFFSET, "Upgrade", 8, quantity=3),
    
	
	"Deploy Pylon": ItemData(200 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 0),
	"Chrono Surge": ItemData(201 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 1),
	"Warp-in Reinforcements": ItemData(202 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 2),
	"Orbital Strike": ItemData(203 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 3),
	"Temporal Field": ItemData(204 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 4),
	"Solar Lance": ItemData(205 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 5),
	"Mass Recall": ItemData(206 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 6),
	"Shield Overcharge": ItemData(207 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 7),
	"Deploy Talandar": ItemData(208 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 8),
	"Purifier Beam": ItemData(209 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 9),
	"Time Stop": ItemData(210 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 10),
	"Solar Bombardment": ItemData(211 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Ability", 11),
	
	"Nexus Overcharge": ItemData(300 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Passive", 0),
	"Orbital Assimilators": ItemData(301 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Passive", 1),
	"Warp Harmonization": ItemData(302 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Passive", 2),
	"Matrix Overload": ItemData(303 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Passive", 3),
	"Guardian Shell": ItemData(304 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Passive", 4),
	"Reconstruction Beam": ItemData(305 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Passive", 5),
	
	"Photon Cannon": ItemData(400 + SC2LOTV_ITEM_ID_OFFSET, "Building", 0),
	"Shield Battery": ItemData(401 + SC2LOTV_ITEM_ID_OFFSET, "Building", 1),
	"Khaydarin Monolith": ItemData(402 + SC2LOTV_ITEM_ID_OFFSET, "Building", 2),

    "+15 Starting Minerals": ItemData(800 + SC2LOTV_ITEM_ID_OFFSET, "Minerals", 15, quantity=0, classification=ItemClassification.filler),
    "+15 Starting Vespene": ItemData(801 + SC2LOTV_ITEM_ID_OFFSET, "Vespene", 15, quantity=0, classification=ItemClassification.filler),
    "+2 Starting Supply": ItemData(802 + SC2LOTV_ITEM_ID_OFFSET, "Supply", 2, quantity=0, classification=ItemClassification.filler),
	"+5 Spear of Adun Energy": ItemData(802 + SC2LOTV_ITEM_ID_OFFSET, "Spear of Adun Energy", 2, quantity=0, classification=ItemClassification.filler)

    # "Keystone Piece": ItemData(850 + SC2LOTV_ITEM_ID_OFFSET, "Goal", 0, quantity=0_skip_balancing)
}


basic_units = {
    'Aiur Zealot',
    'Centurion',
    'Sentinel',
    'Stalker',
    'Dragoon',
    'Adept'
}

advanced_basic_units = basic_units.union({
    'Immortal',
    'Annihilator',
    'Vanguard',
    'Void Ray',
	'Destroyer'
})


def get_basic_units(multiworld: MultiWorld, player: int) -> typing.Set[str]:
    if get_option_value(multiworld, player, 'required_tactics') > 0:
        return advanced_basic_units
    else:
        return basic_units


item_name_groups = {}
for item, data in item_table.items():
    item_name_groups.setdefault(data.type, []).append(item)
item_name_groups["Missions"] = ["Beat " + mission_name for mission_name in vanilla_mission_req_table]

filler_items: typing.Tuple[str, ...] = (
    '+15 Starting Minerals',
    '+15 Starting Vespene',
	'+2 Supply',
	'+5 Spear of Adun Energy'
)

# Defense rating table
# Commented defense ratings are handled in LogicMixin
defense_ratings = {
    "Photon Cannon": 3,
    "Shield Battery": 1,
    "Khaydarin Monolith": 3,
    "Nexus Overcharge": 1,
    "Matrix Overload": 1,
	"Colossus": 2,
	"Reaver": 1,
	"Corsair": 2	
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in get_full_item_list().items() if
                                            data.code}
# Map type to expected int
type_flaggroups: typing.Dict[str, int] = {
    "Unit": 0,
    "Upgrade": 1,
    "Building": 2,
    "Spear of Adun Ability": 3,
    "Spear of Adun Passive": 4,
    "Minerals": 5,
    "Vespene": 6,
    "Supply": 7,
	"Spear of Adun Energy": 8
    "Goal": 9
}
