from typing import NamedTuple, Dict, List
from enum import IntEnum

no_build_regions_list = ["Evil Awoken", "For Aiur!", "The Infinite Cycle", "Templar's Return"]
easy_regions_list = ["The Growing Shadow", "The Spear of Adun", "Sky Shield", "Amon's Reach", "Brothers in Arms"]
medium_regions_list = ["Dark Whispers", "Ghosts in the Fog", "Last Stand", "Forbidden Weapon", "Temple of Yurification",
                       "Harbinger of Oblivion", "Steps of the Rite", "Unsealing the Past"]
hard_regions_list = ["Purification", "Rak'Shir", "Templar's Charge", "The Host", "Into the Void"]


class MissionPools(IntEnum):
    STARTER = 0
    EASY = 1
    MEDIUM = 2
    HARD = 3
    FINAL = 4


class MissionInfo(NamedTuple):
    id: int
    required_world: List[int]
    category: str
    number: int = 0  # number of worlds need beaten
    completion_critical: bool = False  # missions needed to beat game
    or_requirements: bool = False  # true if the requirements should be or-ed instead of and-ed


class FillMission(NamedTuple):
    type: int
    connect_to: List[int]  # -1 connects to Menu
    category: str
    number: int = 0  # number of worlds need beaten
    completion_critical: bool = False  # missions needed to beat game
    or_requirements: bool = False  # true if the requirements should be or-ed instead of and-ed
    removal_priority: int = 0  # how many missions missing from the pool required to remove this mission

vanilla_shuffle_order = [
    
    FillMission(MissionPools.STARTER, [-1], "Aiur", completion_critical=True, removal_priority=4),#0
    FillMission(MissionPools.EASY, [0], "Aiur", completion_critical=True),#1
    FillMission(MissionPools.EASY, [1], "Aiur", completion_critical=True),#2
    FillMission(MissionPools.EASY, [2], "Korhal", completion_critical=True),#3
    FillMission(MissionPools.MEDIUM, [3], "Korhal", completion_critical=True),#4
    FillMission(MissionPools.EASY, [2], "Shakuras", completion_critical=True),#5
    FillMission(MissionPools.MEDIUM, [5], "Shakuras", completion_critical=True),#6
    FillMission(MissionPools.MEDIUM, [4,6], "Glacius", completion_critical=True, or_requirements=True),#7
    FillMission(MissionPools.HARD, [4,6,7], "Ulnar", completion_critical=True),#8
    FillMission(MissionPools.HARD, [8], "Ulnar", completion_critical=True, removal_priority=5),#9
    FillMission(MissionPools.HARD, [9], "Ulnar", completion_critical=True),#10
    FillMission(MissionPools.HARD, [10], "Endion", completion_critical=True),#11
    FillMission(MissionPools.HARD, [11], "Endion", completion_critical=True),#12
    FillMission(MissionPools.HARD, [10], "Slayn", completion_critical=True),#13
    FillMission(MissionPools.HARD, [13], "Slayn", completion_critical=True),#14
    FillMission(MissionPools.HARD, [12,14], "Ravenscar", completion_critical=True, or_requirements=True),#15
    FillMission(MissionPools.HARD, [12,14,15], "Aiur", completion_critical=True, removal_priority=6),#16
    FillMission(MissionPools.HARD, [16], "Aiur", completion_critical=True),#17
    FillMission(MissionPools.FINAL, [17], "Aiur", completion_critical=True),#18
	FillMission(MissionPools.MEDIUM, [2], "Whispers", completion_critical=True, removal_priority=3), #19
    FillMission(MissionPools.MEDIUM, [19], "Whispers", completion_critical=True, removal_priority=2),#20
    FillMission(MissionPools.MEDIUM, [20], "Whispers", completion_critical=True, removal_priority=1),#21
    FillMission(MissionPools.HARD, [10], "Void")#22
	
]

mini_campaign_order = [
    FillMission(MissionPools.STARTER, [-1], "Whispers", completion_critical=True),#0
    FillMission(MissionPools.EASY, [0], "Aiur", completion_critical=True),#1
    FillMission(MissionPools.EASY, [1], "Aiur", completion_critical=True),#2
    FillMission(MissionPools.MEDIUM, [2], "Korhal", completion_critical=True),#3
    FillMission(MissionPools.MEDIUM, [2], "Shakuras", completion_critical=True),#4
    FillMission(MissionPools.HARD, [3,4], "Ulnar", completion_critical=True),#5
    FillMission(MissionPools.HARD, [5], "Ulnar", completion_critical=True),#6
    FillMission(MissionPools.HARD, [6], "Endion", completion_critical=True),#7
    FillMission(MissionPools.HARD, [6], "Slayn", completion_critical=True),#8
    FillMission(MissionPools.HARD, [7,8], "Aiur", completion_critical=True),#9
    FillMission(MissionPools.FINAL, [9], "Aiur", completion_critical=True)#10
]

gauntlet_order = [
    FillMission(MissionPools.STARTER, [-1], "I", completion_critical=True),#0
    FillMission(MissionPools.EASY, [0], "II", completion_critical=True),#1
    FillMission(MissionPools.EASY, [1], "III", completion_critical=True),#2
    FillMission(MissionPools.MEDIUM, [2], "IV", completion_critical=True),#3
    FillMission(MissionPools.MEDIUM, [3], "V", completion_critical=True),#4
    FillMission(MissionPools.HARD, [4], "VI", completion_critical=True),#5
    FillMission(MissionPools.FINAL, [5], "Final", completion_critical=True)#6
]

grid_order = [
    FillMission(MissionPools.STARTER, [-1], "_1"),#0
    FillMission(MissionPools.EASY, [0], "_1"),#1
    FillMission(MissionPools.MEDIUM, [1, 6, 3], "_1", or_requirements=True),#2
    FillMission(MissionPools.HARD, [2, 7], "_1", or_requirements=True),#3
    FillMission(MissionPools.EASY, [0], "_2"),#4
    FillMission(MissionPools.MEDIUM, [1, 4], "_2", or_requirements=True),#5
    FillMission(MissionPools.HARD, [2, 5, 10, 7], "_2", or_requirements=True),#6
    FillMission(MissionPools.HARD, [3, 6, 11], "_2", or_requirements=True),#7
    FillMission(MissionPools.MEDIUM, [4, 9, 12], "_3", or_requirements=True),#8
    FillMission(MissionPools.HARD, [5, 8, 10, 13], "_3", or_requirements=True),#9
    FillMission(MissionPools.HARD, [6, 9, 11, 14], "_3", or_requirements=True),#10
    FillMission(MissionPools.HARD, [7, 10], "_3", or_requirements=True),#11
    FillMission(MissionPools.HARD, [8, 13], "_4", or_requirements=True),#12
    FillMission(MissionPools.HARD, [9, 12, 14], "_4", or_requirements=True),#13
    FillMission(MissionPools.HARD, [10, 13], "_4", or_requirements=True),#14
    FillMission(MissionPools.FINAL, [11, 14], "_4", or_requirements=True)#15
]

mini_grid_order = [
    FillMission(MissionPools.STARTER, [-1], "_1"),#0
    FillMission(MissionPools.EASY, [0], "_1"),#1
    FillMission(MissionPools.MEDIUM, [1, 5], "_1", or_requirements=True),#2
    FillMission(MissionPools.EASY, [0], "_2"),#3
    FillMission(MissionPools.MEDIUM, [1, 3], "_2", or_requirements=True),#4
    FillMission(MissionPools.HARD, [2, 4], "_2", or_requirements=True),#5
    FillMission(MissionPools.MEDIUM, [3, 7], "_3", or_requirements=True),#6
    FillMission(MissionPools.HARD, [4, 6], "_3", or_requirements=True),#7
    FillMission(MissionPools.FINAL, [5, 7], "_3", or_requirements=True)#8
]

blitz_order = [
    FillMission(MissionPools.STARTER, [-1], "I"),#0
    FillMission(MissionPools.EASY, [-1], "I"),#1
    FillMission(MissionPools.MEDIUM, [0, 1], "II", number=1, or_requirements=True),#2
    FillMission(MissionPools.MEDIUM, [0, 1], "II", number=1, or_requirements=True),#3
    FillMission(MissionPools.MEDIUM, [0, 1], "III", number=2, or_requirements=True),#4
    FillMission(MissionPools.MEDIUM, [0, 1], "III", number=2, or_requirements=True),#5
    FillMission(MissionPools.HARD, [0, 1], "IV", number=3, or_requirements=True),#6
    FillMission(MissionPools.HARD, [0, 1], "IV", number=3, or_requirements=True),#7
    FillMission(MissionPools.HARD, [0, 1], "V", number=4, or_requirements=True),#8
    FillMission(MissionPools.HARD, [0, 1], "V", number=4, or_requirements=True),#9
    FillMission(MissionPools.HARD, [0, 1], "Final", number=5, or_requirements=True),#10
    FillMission(MissionPools.FINAL, [0, 1], "Final", number=5, or_requirements=True)#11
]

mission_orders = [vanilla_shuffle_order, vanilla_shuffle_order, mini_campaign_order, grid_order, mini_grid_order, blitz_order, gauntlet_order]

vanilla_mission_req_table = {
    "For Aiur!": MissionInfo(1, [], "Aiur", completion_critical=True),
    "The Growing Shadow": MissionInfo(2, [1], "Aiur", completion_critical=True),
    "The Spear of Adun": MissionInfo(3, [2], "Aiur", completion_critical=True),
    "Sky Shield": MissionInfo(4, [3], "Korhal", completion_critical=True),
    "Brothers in Arms": MissionInfo(5, [4], "Korhal", completion_critical=True),
    "Amon's Reach": MissionInfo(6, [3], "Shakuras", completion_critical=True),
    "Last Stand": MissionInfo(7, [6], "Shakuras", completion_critical=True),
    "Forbidden Weapon": MissionInfo(8, [5,7], "Glacius", completion_critical=True, or_requirements=True),
    "Temple of Yurification": MissionInfo(9, [5,7,8], "Ulnar", completion_critical=True),
    "The Infinite Cycle": MissionInfo(10, [9], "Ulnar", completion_critical=True),
    "Harbinger of Oblivion": MissionInfo(11, [10], "Ulnar", completion_critical=True),
    "Unsealing the Past": MissionInfo(12, [11], "Endion", completion_critical=True),
    "Purification": MissionInfo(13, [12], "Endion", completion_critical=True),
    "Steps of the Rite": MissionInfo(14, [11], "Slayn", completion_critical=True),
    "Rak'Shir": MissionInfo(15, [14], "Slayn", completion_critical=True),
    "Templar's Charge": MissionInfo(16, [13,15], "Ravenscar", completion_critical=True, or_requirements=True),
    "Templar's Return": MissionInfo(17, [13,15,16], "Aiur", completion_critical=True),
    "The Host": MissionInfo(18, [17], "Aiur", completion_critical=True),
    "Salvation": MissionInfo(19, [18], "Aiur", completion_critical=True),
	"Dark Whispers": MissionInfo(20, [3], "Whispers"),
    "Ghosts in the Fog": MissionInfo(21, [20], "Whispers"),
    "Evil Awoken": MissionInfo(22, [21], "Whispers"),
    "Into the Void": MissionInfo(23, [11], "Void")
	
}

lookup_id_to_mission: Dict[int, str] = {
    data.id: mission_name for mission_name, data in vanilla_mission_req_table.items() if data.id}

starting_mission_locations = {
    "Evil Awoken": "Evil Awoken: Victory",
    "For Aiur!": "For Aiur!: Victory",
    "The Infinite Cycle": "GThe Infinite Cycle: Victory",
    "Templar's Return": "Templar's Return: Victory"
 #   "Zero Hour": "Zero Hour: First Group Rescued",
 #   "Evacuation": "Evacuation: First Chysalis",
 #   "Devil's Playground": "Devil's Playground: Tosh's Miners",
 #   "Smash and Grab": "Smash and Grab: First Relic",
 #   "The Great Train Robbery": "The Great Train Robbery: North Defiler"
}

alt_final_mission_locations = {
    "Purification": "Purification: Victory",
    "Rak'Shir": "Rak'Shir: Victory",
    "Templar's Charge": "Templar's Charge: Victory",
    "The Host": "The Host: Victory",
    "Into the Void": "Into the Void: Victory"
}