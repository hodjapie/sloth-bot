# import.standard
import enum
from typing import Callable

# import.thirdparty
import discord

# import.local
from .quests_callbacks import *

class QuestEnum(enum.Enum):
    """ Class for the Quests enum. """

    one: Callable = quest_one_callback
    two: Callable = quest_two_callback
    three: Callable = quest_three_callback
    four: Callable = quest_four_callback
    five: Callable = quest_five_callback
    six: Callable = quest_six_callback
    seven: Callable = quest_seven_callback
    eight: Callable = lambda cb: cb
    nine: Callable = lambda cb: cb
    ten: Callable = quest_ten_callback
    eleven: Callable = lambda cb: cb
    twelve: Callable = quest_twelve_callback
    thirteen: Callable = quest_thirteen_callback
    fourteen: Callable = quest_fourteen_callback