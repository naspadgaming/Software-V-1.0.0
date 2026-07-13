from PySide6.QtCore import Qt, Signal

from PySide6.QtWidgets import (
    QTreeWidget,
    QTreeWidgetItem
)


class TraceTree(QTreeWidget):

    trace_selected = Signal(int)

    def __init__(self):
        super().__init__()

        self.setHeaderHidden(True)

        self.itemClicked.connect(
            self.on_item_clicked
        )

    # =====================================

    def load_stream(self, filename, stream):

        self.clear()

        root = QTreeWidgetItem()

        root.setText(0, filename.split("/")[-1])

        self.addTopLevelItem(root)

        for i, tr in enumerate(stream):

            item = QTreeWidgetItem()

            item.setText(0, tr.id)

            item.setData(
                0,
                Qt.ItemDataRole.UserRole,
                i
            )

            root.addChild(item)

        root.setExpanded(True)

    # =====================================

    def on_item_clicked(self, item):

        index = item.data(
            0,
            Qt.ItemDataRole.UserRole
        )

        if index is None:
            return

        self.trace_selected.emit(index)