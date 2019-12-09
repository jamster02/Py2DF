import typing

from ..classes import UtilityBlock, JSONData, Arguments, Block, Bracket, BracketedBlock
from ..enums import BlockType, IfPlayerType, IfType, BracketDirection, BracketType, IfEntityType, \
    RepeatType, SetVarType, SelectObjectType
from ..reading.reader import DFReader
from ..constants import BLOCK_ID
from ..utils import remove_u200b_from_doc


class Repeat(BracketedBlock, UtilityBlock, JSONData):
    """A Codeblock that repeats code inside it.

    Parameters
    ----------\u200b
    action : :class:`~py2df.enums.actions.RepeatType`
        The condition to check.

    args : :class:`~py2df.classes.collections.Arguments`
        The arguments of this Repeat block.

    target : ``None``
        (Repeats have no target.)

    append_to_reader : :class:`bool`, optional
        Whether or not this newly-created :class:`RepeatPlayer` should be already appended to the
        :class:`~py2df.reading.reader.DFReader`. Defaults to ``True``.

    codeblocks : Deque[:class:`~py2df.classes.abc.Block`], optional
        The blocks, including Brackets, inside this Repeat Player. Defaults to empty deque (None).

    Attributes
    ----------\u200b
    block : :attr:`~py2df.enums.parameters.BlockType.REPEAT`
        The type of this codeblock.

    args : :class:`~py2df.classes.collections.Arguments`
        The arguments of this Repeat block.

    action : :class:`~py2df.enums.utilityblock.RepeatType`
        The type of Repeat.

    codeblocks : Deque[:class:`~py2df.classes.abc.Block`]
        The blocks, including Brackets, inside this Repeat.

    sub_action : Optional[:class:`~py2df.enums.enum_util.IfType`]
        If ``action`` is :attr:`~py2df.enums.utilityblock.RepeatType.WHILE_COND`, then this is the If condition
        that determines if the Repeat will keep going.

    length : :class:`int`
        The length of each individual Repeat (excluding brackets). This is always equal to 1.

    total_length : :class:`int`
        The sum of all lengths of all codeblocks inside this Repeat, including Repeat itself and brackets
        (so 3 + inner length).

    data : ``None``
        ('Repeat' has no extra codeblock data.)

    target : ``None``
        ('Repeat' has no target.)
    """
    __slots__ = ()

    block: BlockType = BlockType.REPEAT
    args: Arguments
    action: RepeatType
    codeblocks: typing.Deque[Block]
    invert: bool
    sub_action: typing.Optional[IfType]
    length: int = 1
    data: None = None
    target: None = None

    def __enter__(self) -> "Repeat":
        """
        Triggers the creation of an opening bracket and the addition of all codeblocks into this If Player.

        Returns
        -------
        :class:`IfPlayer`
            self (The current instance)
        """
        self.codeblocks.extendleft([self, Bracket(BracketDirection.OPEN, BracketType.REPEAT)])
        reader = DFReader()

        if self not in reader.curr_code_loc:
            reader.append_codeblock(self)

        reader.curr_code_loc = self
        return self

    def __exit__(self, _exc_type, _exc_val, _exc_tb) -> None:
        """
        Closes the Bracket, and resets the location of codeblocks (i.e., they now go outside the brackets).

        Returns
        -------
        ``None``
            ``None``
        """
        self.codeblocks.append(Bracket(BracketDirection.CLOSE, BracketType.REPEAT))

    def as_json_data(self) -> dict:
        """
        Produces a JSON-serializable dict representing this Repeat.

        Returns
        -------
        :class:`dict`
        """
        return dict(
            id=BLOCK_ID,
            block=self.block.value,
            args=self.args.as_json_data(),
            action=self.action.value,
            **(dict(
                sub_action=(
                    "E" if self.sub_action in (
                        IfEntityType.NAME_EQUALS, IfEntityType.IS_NEAR, IfEntityType.STANDING_ON
                    ) else ""  # ENameEquals; EIsNear; EStandingOn => separate from IfPlayer's.
                ) + str(self.sub_action.value)
            ) if self.sub_action else dict())
        )


class SetVar(UtilityBlock, JSONData):
    """Used to set the value of a dynamic variable.

    Parameters
    ----------\u200b
    action : :class:`~py2df.enums.actions.SetVarType`
        The type of SetVar block this is.

    args : :class:`~py2df.classes.collections.Arguments`
        The arguments of this SetVar block.

    append_to_reader : :class:`bool`, optional
        Whether or not this newly-created :class:`SetVar` should be already appended to the
        :class:`~py2df.reading.reader.DFReader`. Defaults to ``True``.

    Attributes
    ----------\u200b
    block : :attr:`~py2df.enums.parameters.BlockType.ENTITY_ACTION`
        The type of this codeblock (SetVar).

    args : :class:`~py2df.classes.collections.Arguments`
        The arguments of this SetVar block.

    action : :class:`~py2df.enums.actions.SetVarType`
        The type of SetVar block this is.

    sub_action : ``None``
        (SetVar blocks have no sub actions.)

    length : :class:`int`
        The length, in blocks, of each individual control blocks. This is always equal to 2.

    data : ``None``
        (SetVar blocks have no extra codeblock data.)

    target : ``None``
        (SetVar blocks have no target.)
    """
    __slots__ = ("args", "action")

    block: BlockType = BlockType.SET_VAR
    args: Arguments
    action: SetVarType
    sub_action: None = None
    length: int = 2
    data: None = None
    target: None = None

    def __init__(
        self, action: SetVarType, args: Arguments = Arguments(),
        *, append_to_reader: bool = True
    ):
        """
        Initialize this SetVar block.

        Parameters
        ----------
        action : :class:`~py2df.enums.actions.SetVarType`
            The type of SetVar block this is.

        args : :class:`~py2df.classes.collections.Arguments`
            The arguments of this SetVar block.

        append_to_reader : :class:`bool`, optional
            Whether or not this newly-created :class:`SetVar` should be already appended to the
            :class:`~py2df.reading.reader.DFReader`. Defaults to ``True``. (All classmethods will set this to ``True``)
        """
        self.action = SetVarType(action)
        self.args = args

        if append_to_reader:
            DFReader().append_codeblock(self)

    def as_json_data(self) -> dict:
        """Produces a JSON-serializable dict representing this SetVar block.

        Returns
        -------
        :class:`dict`
        """
        return dict(
            id=BLOCK_ID,
            block=self.block.value,
            args=self.args.as_json_data(),
            action=self.action.value
        )


class SelectObj(UtilityBlock, JSONData):
    """Used to change the selection on the current line of code, which will affect the targets of most code blocks.

    Parameters
    ----------\u200b
    action : :class:`~py2df.enums.actions.SelectObjectType`
        The new selection, which will be the type of Select Object block.

    args : :class:`~py2df.classes.collections.Arguments`
        The arguments of this SelectObj block.

    append_to_reader : :class:`bool`, optional
        Whether or not this newly-created :class:`SelectObj` should be already appended to the
        :class:`~py2df.reading.reader.DFReader`. Defaults to ``True``.

    Attributes
    ----------\u200b
    block : :attr:`~py2df.enums.parameters.BlockType.SELECT_OBJ`
         The new selection, which will be the type of Select Object block.

    args : :class:`~py2df.classes.collections.Arguments`
        The arguments of this SelectObj block.

    action : :class:`~py2df.enums.actions.SelectObjectType`
        The type of SelectObj block this is.

    sub_action : Optional[Union[:class:`~py2df.enums.enum_util.IfPlayerType`, \
:class:`~py2df.enums.enum_util.IfEntityType`]]
        If the SelectObj type is one of :attr:`~py2df.enums.actions.SelectObjectType.ENTITIES_COND`,
        :attr:`~py2df.enums.actions.SelectObjectType.MOBS_COND` or
        :attr:`~py2df.enums.actions.SelectObjectType.PLAYERS_COND`, then this attribute represents the specific
        condition that determines whether an entity/mob/player is selected or not. Otherwise, this is ``None``.

    length : :class:`int`
        The length, in blocks, of each individual control blocks. This is always equal to 2.

    data : ``None``
        (SelectObj blocks have no extra codeblock data.)

    target : ``None``
        (SelectObj blocks have no target.)
    """
    __slots__ = ("args", "action", "sub_action")

    block: BlockType = BlockType.SELECT_OBJ
    args: Arguments
    action: SelectObjectType
    sub_action: typing.Optional[typing.Union[IfPlayerType, IfEntityType]]
    length: int = 2
    data: None = None
    target: None = None

    def __init__(
        self, action: SelectObjectType, args: Arguments = Arguments(),
        *, append_to_reader: bool = True
    ):
        """
        Initialize this SelectObj block.

        Parameters
        ----------
        action : :class:`~py2df.enums.actions.SelectObjectType`
            The type of SelectObj block this is.

        args : :class:`~py2df.classes.collections.Arguments`
            The arguments of this SelectObj block.

        append_to_reader : :class:`bool`, optional
            Whether or not this newly-created :class:`SelectObj` should be already appended to the
            :class:`~py2df.reading.reader.DFReader`. Defaults to ``True``. (All classmethods will set this to ``True``)
        """
        self.action = SelectObjectType(action)
        self.args = args

        if append_to_reader:
            DFReader().append_codeblock(self)

    def as_json_data(self) -> dict:
        """Produces a JSON-serializable dict representing this SelectObj block.

        Returns
        -------
        :class:`dict`
        """
        return dict(
            id=BLOCK_ID,
            block=self.block.value,
            args=self.args.as_json_data(),
            action=self.action.value,
            **(dict(
                sub_action=(
                    "E" if self.sub_action in (
                        IfEntityType.NAME_EQUALS, IfEntityType.IS_NEAR, IfEntityType.STANDING_ON
                    ) else ""  # ENameEquals; EIsNear; EStandingOn => separate from IfPlayer's.
                ) + str(self.sub_action.value)
            ) if self.sub_action else dict())
        )


remove_u200b_from_doc(Repeat, SetVar, SelectObj)