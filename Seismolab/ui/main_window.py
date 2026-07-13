from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

from PySide6.QtWidgets import (
    QFileDialog,
    QDockWidget,
    QMainWindow,
    QMessageBox,
    QStatusBar,
)


from core.reader import SeismicReader
from core.session import Session
from core.processor import SignalProcessor

from core.event import SeismicEvent
from core.database import EventDatabase


from ui.toolbar import MainToolBar
from ui.filter_dialog import BandpassDialog
from ui.console import ConsoleWidget


from widgets.waveform import WaveformWidget
from widgets.trace_tree import TraceTree
from widgets.event_browser import EventBrowser


from widgets.fft_window import FFTWindow
from widgets.spectrogram_window import SpectrogramWindow
from widgets.picker_window import PickerWindow
from widgets.trigger_window import TriggerWindow
from widgets.psd_window import PSDWindow



class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()


        self.session = Session()


        self.database = EventDatabase()


        self.current_event = None



        self.fft_window = None
        self.spectrogram_window = None
        self.picker_window = None
        self.trigger_window = None
        self.psd_window = None



        self.setWindowTitle(
            "SeismoLab v1.6"
        )


        self.resize(
            1400,
            900
        )



        self.create_actions()

        self.create_menu()

        self.create_toolbar()

        self.setup_ui()

        self.connect_signals()



    # ==================================================
    # ACTIONS
    # ==================================================

    def create_actions(self):


        self.open_action = QAction(
            "Open",
            self
        )


        self.save_event_action = QAction(
            "Save Event",
            self
        )


        self.exit_action = QAction(
            "Exit",
            self
        )


        self.filter_action = QAction(
            "Bandpass Filter",
            self
        )


        self.fft_action = QAction(
            "FFT",
            self
        )


        self.spectrogram_action = QAction(
            "Spectrogram",
            self
        )


        self.pick_action = QAction(
            "Pick Arrival",
            self
        )


        self.trigger_action = QAction(
            "STA/LTA",
            self
        )


        self.psd_action = QAction(
            "PSD",
            self
        )


        self.about_action = QAction(
            "About",
            self
        )



    # ==================================================
    # MENU
    # ==================================================

    def create_menu(self):


        menu = self.menuBar()


        file_menu = menu.addMenu(
            "File"
        )


        file_menu.addAction(
            self.open_action
        )


        file_menu.addAction(
            self.save_event_action
        )


        file_menu.addSeparator()


        file_menu.addAction(
            self.exit_action
        )



        process = menu.addMenu(
            "Processing"
        )


        process.addAction(
            self.filter_action
        )


        process.addAction(
            self.fft_action
        )


        process.addAction(
            self.spectrogram_action
        )


        process.addAction(
            self.pick_action
        )


        process.addAction(
            self.trigger_action
        )


        process.addAction(
            self.psd_action
        )

            # ==================================================
    # TOOLBAR
    # ==================================================

    def create_toolbar(self):


        self.toolbar = MainToolBar(
            self
        )


        self.addToolBar(
            self.toolbar
        )



    # ==================================================
    # UI SETUP
    # ==================================================

    def setup_ui(self):


        self.waveform = WaveformWidget()


        self.console = ConsoleWidget()


        self.event_browser = EventBrowser()



        self.setCentralWidget(
            self.waveform
        )



        # -----------------------------
        # Trace Explorer
        # -----------------------------

        explorer_dock = QDockWidget(
            "Trace Explorer",
            self
        )


        self.explorer = TraceTree()


        explorer_dock.setWidget(
            self.explorer
        )


        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            explorer_dock
        )



        # -----------------------------
        # Event Catalog
        # -----------------------------

        event_dock = QDockWidget(
            "Event Catalog",
            self
        )


        event_dock.setWidget(
            self.event_browser
        )


        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            event_dock
        )



        # -----------------------------
        # Console
        # -----------------------------

        console_dock = QDockWidget(
            "Console",
            self
        )


        console_dock.setWidget(
            self.console
        )


        self.addDockWidget(
            Qt.BottomDockWidgetArea,
            console_dock
        )



        status = QStatusBar()


        status.showMessage(
            "Ready"
        )


        self.setStatusBar(
            status
        )



        self.load_events()



    # ==================================================
    # SIGNALS
    # ==================================================

    def connect_signals(self):


        self.exit_action.triggered.connect(
            self.close
        )


        self.open_action.triggered.connect(
            self.open_file
        )


        self.save_event_action.triggered.connect(
            self.save_event
        )


        self.filter_action.triggered.connect(
            self.bandpass_filter
        )


        self.fft_action.triggered.connect(
            self.show_fft
        )


        self.spectrogram_action.triggered.connect(
            self.show_spectrogram
        )


        self.pick_action.triggered.connect(
            self.show_picker
        )


        self.trigger_action.triggered.connect(
            self.show_trigger
        )


        self.psd_action.triggered.connect(
            self.show_psd
        )


        self.explorer.trace_selected.connect(
            self.select_trace
        )



        self.event_browser.event_selected.connect(
            self.load_event
        )



    # ==================================================
    # OPEN FILE
    # ==================================================

    def open_file(self):


        filename, _ = QFileDialog.getOpenFileName(

            self,

            "Open Seismic File",

            "",

            "MiniSEED (*.mseed *.ms);;SAC (*.sac)"

        )



        if not filename:

            return



        try:


            self.console.log(
                f"[INFO] Loading {filename}"
            )



            stream = SeismicReader.load(
                filename
            )



            self.session.load(

                filename,

                stream

            )



            self.session.selected_trace = 0



            self.current_event = SeismicEvent.from_stream(

                filename,

                stream

            )



            self.explorer.load_stream(

                filename,

                stream

            )



            self.refresh()



            self.console.log(
                "[OK] File loaded"
            )


            self.statusBar().showMessage(
                "File Loaded"
            )



        except Exception as e:


            self.console.log(

                f"[ERROR] {e}"

            )


            QMessageBox.critical(

                self,

                "Error",

                str(e)

            )



    # ==================================================
    # SAVE EVENT
    # ==================================================

    def save_event(self):


        if self.current_event is None:


            QMessageBox.warning(

                self,

                "Warning",

                "No event loaded."

            )


            return



        event_id = self.database.add_event(

            self.current_event

        )



        self.current_event.event_id = event_id



        self.console.log(

            f"[EVENT] Saved ID {event_id}"

        )



        self.load_events()

            # ==================================================
    # LOAD EVENTS
    # ==================================================

    def load_events(self):


        events = self.database.get_events()


        self.event_browser.load_events(

            events

        )



    # ==================================================
    # LOAD EVENT FROM CATALOG
    # ==================================================

    def load_event(self,event_id):


        row = self.database.get_event(

            event_id

        )



        if row is None:

            return



        filename = row[1]



        self.console.log(

            f"[EVENT] Selected {event_id}"

        )



        QMessageBox.information(

            self,

            "Event",

            f"Event file:\n{filename}"

        )



    # ==================================================
    # TRACE SELECT
    # ==================================================

    def select_trace(self,index):


        self.session.selected_trace = index



        trace = self.session.current_trace(

            index

        )



        if trace is None:

            return



        self.waveform.plot_stream(

            self.session.current_stream,

            index

        )



        self.console.log(

            f"[TRACE] Selected {trace.id}"

        )



    # ==================================================
    # FFT
    # ==================================================

    def show_fft(self):


        trace = self.session.current_trace()


        if trace is None:

            return



        self.fft_window = FFTWindow(

            trace

        )


        self.fft_window.show()



    # ==================================================
    # SPECTROGRAM
    # ==================================================

    def show_spectrogram(self):


        trace = self.session.current_trace()


        if trace is None:

            return



        self.spectrogram_window = SpectrogramWindow(

            trace

        )


        self.spectrogram_window.show()



    # ==================================================
    # PICKER
    # ==================================================

    def show_picker(self):


        trace = self.session.current_trace()


        if trace is None:

            return



        self.picker_window = PickerWindow(

            trace

        )


        self.picker_window.show()



    # ==================================================
    # STA/LTA
    # ==================================================

    def show_trigger(self):


        trace = self.session.current_trace()


        if trace is None:

            return



        self.trigger_window = TriggerWindow(

            trace

        )


        self.trigger_window.show()



    # ==================================================
    # PSD
    # ==================================================

    def show_psd(self):


        trace = self.session.current_trace()


        if trace is None:

            return



        self.psd_window = PSDWindow(

            trace

        )


        self.psd_window.show()



    # ==================================================
    # BANDPASS FILTER
    # ==================================================

    def bandpass_filter(self):


        if self.session.current_stream is None:


            QMessageBox.warning(

                self,

                "Warning",

                "Open seismic file first."

            )


            return



        dialog = BandpassDialog()



        if dialog.exec():


            params = dialog.values()



            self.console.log(

                "[PROCESS] Bandpass"

            )



            filtered = SignalProcessor.bandpass(

                self.session.current_stream,

                params["freqmin"],

                params["freqmax"],

                params["corners"],

                params["zerophase"]

            )



            self.session.apply(

                filtered,

                "Bandpass Filter"

            )



            self.explorer.load_stream(

                self.session.filename,

                filtered

            )



            self.refresh()



            self.console.log(

                "[OK] Filter finished"

            )



    # ==================================================
    # REFRESH
    # ==================================================

    def refresh(self):


        self.waveform.plot_stream(

            self.session.current_stream,

            self.session.selected_trace

        )