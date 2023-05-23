from typing import Dict, FrozenSet, Union
from BaseClasses import MultiWorld
from Options import Choice, Option, Toggle, DefaultOnToggle, ItemSet, OptionSet, Range
from .MissionTables import vanilla_mission_req_table


class GameDifficulty(Choice):
    """The difficulty of the campaign, affects enemy AI, starting units, and game speed."""
    display_name = "Game Difficulty"
    option_casual = 0
    option_normal = 1
    option_hard = 2
    option_brutal = 3

class MissionOrder(Choice):
    """Determines the order the missions are played in.  The last three mission orders end in a random mission.
    Vanilla (23): Keeps the standard mission order and branching from the LotV Campaign.
    Vanilla Shuffled (23): Keeps same branching paths from the LotV Campaign but randomizes the order of missions within.
    Mini Campaign (11): Shorter version of the campaign with randomized missions and optional branches.
    Grid (16):  A 4x4 grid of random missions.  Start at the top-left and forge a path towards final mission.
    Mini Grid (9):  A 3x3 version of Grid.  Complete the bottom-right mission to win.
    Blitz (12):  12 random missions that open up very quickly.  Complete the bottom-right mission to win.
    Gauntlet (7): Linear series of 7 random missions to complete the campaign."""
    display_name = "Mission Order"
    option_vanilla = 0
    option_vanilla_shuffled = 1
    option_mini_campaign = 2
    option_grid = 3
    option_mini_grid = 4
    option_blitz = 5
    option_gauntlet = 6


class ShufflePrologue(DefaultOnToggle):
    """Determines if the 2 prologue missions are included in the shuffle if Vanilla mission order is not enabled.
    If turned off with Vanilla Shuffled, the 2 prologue missions will be in their normal position on the first chain
       if not shuffled.
    If turned off with reduced mission settings, the 2 prologue missions will not appear."""
    display_name = "Shuffle Prologue Missions"

#class ShuffleEpilogue(DefaultOnToggle):
#    """Determines if the 3 epilogue missions are included in the shuffle if Vanilla mission order is not enabled.
#    If turned off with Vanilla Shuffled, the 3 epilogue missions will be in their normal position on the first chain
#       if not shuffled.
#    If turned off with reduced mission settings, the 2 epilogue missions will not appear."""
#    display_name = "Shuffle Epilogue Missions"


class ShuffleNoBuild(DefaultOnToggle):
    """Determines if the 4 no-build missions are included in the shuffle if Vanilla mission order is not enabled.
    If turned off with reduced mission settings, the 4 no-build missions will not appear."""
    display_name = "Shuffle No-Build Missions"


class EarlyUnit(DefaultOnToggle):
    """Guarantees that the first mission will contain a unit."""
    display_name = "Early Unit"


class RequiredTactics(Choice):
    """Determines the maximum tactical difficulty of the seed (separate from mission difficulty).  Higher settings
    increase randomness.

    Standard:  All missions can be completed with good micro and macro.
    Advanced:  Completing missions may require relying on starting units and micro-heavy units.
    No Logic:  Units and upgrades may be placed anywhere.  LIKELY TO RENDER THE RUN IMPOSSIBLE ON HARDER DIFFICULTIES!"""
    display_name = "Required Tactics"
    option_standard = 0
    option_advanced = 1
    option_no_logic = 2


class LockedItems(ItemSet):
    """Guarantees that these items will be unlockable"""
    display_name = "Locked Items"


class ExcludedItems(ItemSet):
    """Guarantees that these items will not be unlockable"""
    display_name = "Excluded Items"


class ExcludedMissions(OptionSet):
    """Guarantees that these missions will not appear in the campaign
    Only applies on shortened mission orders.
    It may be impossible to build a valid campaign if too many missions are excluded."""
    display_name = "Excluded Missions"
    valid_keys = {mission_name for mission_name in vanilla_mission_req_table.keys() if mission_name != 'Salvation'}


# noinspection PyTypeChecker
sc2lotv_options: Dict[str, Option] = {
    "game_difficulty": GameDifficulty,
    "mission_order": MissionOrder,
    "shuffle_prologue": ShufflePrologue,
 #   "shuffle_epilogue": ShuffleEpilogue,
    "shuffle_no_build": ShuffleNoBuild,
    "early_unit": EarlyUnit,
    "required_tactics": RequiredTactics,
    "locked_items": LockedItems,
    "excluded_items": ExcludedItems,
    "excluded_missions": ExcludedMissions
}


def get_option_value(multiworld: MultiWorld, player: int, name: str) -> Union[int,  FrozenSet]:
    if multiworld is None:
        return sc2lotv_options[name].default

    player_option = getattr(multiworld, name)[player]

    return player_option.value
