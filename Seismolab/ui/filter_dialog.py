from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QHBoxLayout,
    QDoubleSpinBox,
    QSpinBox,
    QPushButton,
    QCheckBox
)


class BandpassDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bandpass Filter")
        self.setMinimumWidth(320)

        layout = QVBoxLayout(self)

        form = QFormLayout()

        self.low_freq = QDoubleSpinBox()
        self.low_freq.setRange(0.001,1000)
        self.low_freq.setValue(1.0)

        self.high_freq = QDoubleSpinBox()
        self.high_freq.setRange(0.001,1000)
        self.high_freq.setValue(10.0)

        self.corners = QSpinBox()
        self.corners.setRange(1,10)
        self.corners.setValue(4)

        self.zero_phase = QCheckBox()
        self.zero_phase.setChecked(True)

        form.addRow("Low Frequency",self.low_freq)
        form.addRow("High Frequency",self.high_freq)
        form.addRow("Corners",self.corners)
        form.addRow("Zero Phase",self.zero_phase)

        layout.addLayout(form)

        buttons = QHBoxLayout()

        ok = QPushButton("Apply")
        cancel = QPushButton("Cancel")

        ok.clicked.connect(self.accept)
        cancel.clicked.connect(self.reject)

        buttons.addStretch()
        buttons.addWidget(ok)
        buttons.addWidget(cancel)

        layout.addLayout(buttons)

    def values(self):

        return {
            "freqmin": self.low_freq.value(),
            "freqmax": self.high_freq.value(),
            "corners": self.corners.value(),
            "zerophase": self.zero_phase.isChecked()
        }