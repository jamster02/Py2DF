from .enum_util import AutoSnakeToPascalCaseNameEnum
from enum import auto, unique


@unique
class IfPlayerType(AutoSnakeToPascalCaseNameEnum):
    """
    Contains all types of If Player blocks.
    """
    BLOCK_EQUALS = auto()  #: Checks if the block in a block interaction event is a certain block.
    CMD_ARG_EQUALS = auto(
    )  #: Checks if some argument of a player's command is equal to some text when the Player Command Event is executed.
    CMD_EQUALS = auto(
    )  #: Checks if a player's command is equal to a certain text when the Player Command Event is executed.
    CURSOR_ITEM = auto()  #: Checks if the item that is being moved with a player's cursor is a certain item.
    HAS_ALL_ITEMS = auto()  #: Checks if a player has all of the items in the chest.
    HAS_EFFECT = auto()  #: Checks if a player has a potion effect.
    HAS_ITEM = auto()  #: Checks if a player has an item in their inventory.
    HAS_ROOM_FOR_ITEM = auto()  #: Checks if a player's inventory has enough room for an item to be given.
    HAS_SLOT_ITEM = auto()  #: Checks if a player has an item in a specific inventory slot.
    IN_WORLD_BORDER = auto()  #: Checks if the player (or a location) is within their world border.
    INV_OPEN = auto()  #: Checks if a player has a certain inventory type open.
    IS_BLOCKING = auto()  #: Checks if a player is blocking with a shield.
    IS_FLYING = auto()  #: Checks if a player is flying.
    IS_GLIDING = auto()  #: Checks if a player is gliding with elytra.
    IS_GROUNDED = auto()  #: Checks if a player is supported by a block.
    IS_HOLDING = auto()  #: Checks if a player is holding an item in their hand.
    IS_HOLDING_MAIN = auto()  #: 
    IS_HOLDING_OFF = auto()  #: 
    IS_LOOKING_AT = auto()  #: Checks if a player is looking at a block of a certain type or at a certain location.
    IS_NEAR = auto()  #: Checks if a player is within a certain range of a location. (default: 5 blocks)
    IS_SNEAKING = auto()  #: Checks if a player is sneaking.
    IS_SPRINTING = auto()  #: Checks if a player is sprinting or using the sprint key to swim.
    IS_SWIMMING = auto()  #: Checks if a player is in water or lava.
    IS_WEARING = auto()  #: Checks if a player is wearing an item.
    ITEM_EQUALS = auto()  #: Checks if the items in one of the events below is a certain item.
    MENU_SLOT_EQUALS = auto(
    )  #: Checks if the player's currently open inventory menu contains an item in a specific slot.
    NAME_EQUALS = auto(
    )  #: Checks if a player's username is equal to one of the usernames in the chest (case insensitive).
    NO_ITEM_COOLDOWN = auto()  #: Checks if the player does not have a cooldown applied to an item type.
    SLOT_EQUALS = auto(
    )  #: Checks if the player's currently selected hotbar slot corresponds with a slot ID between 1 and 9.
    STANDING_ON = auto()  #: Checks if a player is standing on a block of a certain type or at a certain location.


@unique
class IfVariableType(AutoSnakeToPascalCaseNameEnum):
    """
    Contains all types of If Variable blocks.
    """
    CONTAINS = auto()  #: Checks if a text variable contains another text item.
    EQUALS = " = "  #: Checks if a variable is equal to one of the given variables.
    GREATER_THAN = ">"  #: Checks if a number variable is greater than another number.
    GREATER_THAN_OR_EQUAL_TO = ">="  #: Checks if a number variable is greater than or equal to another number.
    IN_RANGE = auto(
    )  #: Checks if a number var is within 2 other numbers or a location var is within the region of 2 other locations.
    IS_NEAR = auto(
    )  #: Checks if a number is within a certain range of another number or if a location is near another location.
    ITEM_EQUALS = auto()  #: Works the same as Variable = but has a few extra options for item comparison.
    ITEM_HAS_TAG = auto()  #: Checks if the given item has the given custom item tag.
    LESS_THAN = "<"  #: Checks if a number variable is less than another number.
    LESS_THAN_OR_EQUAL_TO = "<="  #: Checks if a number variable is less than or equal to another number.
    LIST_CONTAINS = auto()  #: Checks if any of a list's contents match the given value.
    LIST_VALUE_EQ = auto()  #: Checks if a list's value at an index is equal to a value.
    NOT_EQUALS = " != "  #: Checks if a variable does not equal another variable.
    TEXT_MATCHES = auto()  #: Checks if a text matches another text.
    VAR_IS_TYPE = auto()  #: Checks if a variable is a certain type of variable.



@unique
class IfEntityType(AutoSnakeToPascalCaseNameEnum):
    """
    Contains all types of If Entity blocks.
    """
    EXISTS = auto()  #: Checks if an entity still exists in the world.
    IS_ITEM = auto()  #: Checks if an entity is an item.
    IS_MOB = auto()  #: Checks if an entity is a mob.
    IS_NEAR = auto()  #: Checks if an entity is within a certain range of a location. (default: 5 blocks)
    IS_PROJ = auto()  #: Checks if an entity is a projectile.
    IS_TYPE = auto()  #: Checks if an entity is a certain type.
    IS_VEHICLE = auto()  #: Checks if an entity is a vehicle.
    NAME_EQUALS = auto()  #: Checks if an entity's name is equal to the text in the chest.
    STANDING_ON = auto()  #: Checks if an entity is standing on a block of a certain type or at a certain location.


@unique
class IfGameType(AutoSnakeToPascalCaseNameEnum):
    """Contains all types of If Game blocks."""
    BLOCK_EQUALS = auto()  #: Checks if a block at a certain location is a certain block.
    BLOCK_POWERED = auto()  #: Checks if a block at a certain location is powered by redstone.
    CMD_ARG_EQUALS = auto()  #: Checks if part of the command entered in this Command Event is equal to a certain text.
    COMMAND_EQUALS = auto()  #: Checks if the command entered in this Command Event is equal to a certain text.
    CONTAINER_HAS = auto()  #: Checks if a container has an item in its inventory.
    CONTAINER_HAS_ALL = auto()  #: Checks if a container has all of the items in the chest.
    EVENT_BLOCK_EQUALS = auto()  #: Checks if the block in a block- related event is a certain block.
    EVENT_CANCELLED = auto()  #: Checks if the current event is cancelled.
    EVENT_ITEM_EQUALS = auto()  #: Checks if the item in an item- related event is a certain item.
    SIGN_HAS_TXT = auto()  #: Checks if the text on a sign at a certain location contains the text in the chest.
