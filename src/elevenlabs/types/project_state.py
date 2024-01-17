# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ProjectState(str, enum.Enum):
    DEFAULT = "default"
    CONVERTING = "converting"

    def visit(self, default: typing.Callable[[], T_Result], converting: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProjectState.DEFAULT:
            return default()
        if self is ProjectState.CONVERTING:
            return converting()