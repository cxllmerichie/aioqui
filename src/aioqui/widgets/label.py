from PySide6.QtGui import QFontMetrics, QPaintEvent
from PySide6.QtWidgets import QLabel, QWidget, QSizePolicy
from PySide6.QtCore import Qt, QSize

from ..misc import Icon
from .extensions import ContextObjectExt
from src.aioqui.enums import Alignment


class Label(ContextObjectExt, Alignment, QLabel):
    __elided = False
    __non_elided_text = ''

    def __init__(self, parent: QWidget, name: str, visible: bool = True):
        QLabel.__init__(self, parent)
        ContextObjectExt.__init__(self, parent, name, visible)

    def paintEvent(self, event: QPaintEvent):
        if self.__elided:
            non_elided_text = self.__non_elided_text
            self.setText(QFontMetrics(self.font()).elidedText(non_elided_text, Qt.ElideRight, self.width() - 10))
            self.__non_elided_text = non_elided_text
        super().paintEvent(event)

    async def init(
            self, *,
            text: str = '', alignment: Qt.Alignment = None, wrap: bool = False, size: QSize = None,
            icon: Icon = None, elided: bool = False, policy: tuple[QSizePolicy, QSizePolicy] = None
    ) -> 'Label':
        self.__elided = elided
        if self.__elided:
            self.__non_elided_text = text
        self.setText(text)
        self.setWordWrap(wrap)
        if size:
            self.setFixedSize(size)
        if alignment:
            self.setAlignment(alignment)
        if icon:
            self.setPixmap(icon.icon.pixmap(icon.size))
        if policy:
            self.setSizePolicy(*policy)
        return self

    def setText(self, text: str) -> None:
        if self.__elided:
            self.__non_elided_text = text
        super().setText(text)
