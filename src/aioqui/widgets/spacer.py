from PySide6.QtWidgets import QSpacerItem, QSizePolicy

from ..enums import Policy


class Spacer(QSpacerItem):
    def __init__(self, horizontal: bool = False, vertical: bool = False):
        super().__init__(
            0, 0,
            Policy.Expanding if horizontal else Policy.Minimum,
            Policy.Expanding if vertical else Policy.Minimum
        )
