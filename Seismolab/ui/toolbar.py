from PySide6.QtWidgets import QToolBar


class MainToolBar(QToolBar):

    def __init__(self, parent):
        super().__init__("Main Toolbar")

        self.setMovable(False)

        self.addAction(parent.open_action)
        self.addSeparator()

        self.addAction(parent.filter_action)
        self.addAction(parent.fft_action)
        self.addAction(parent.spectrogram_action)
        self.addAction(parent.pick_action)