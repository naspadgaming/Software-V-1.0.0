from core.processor import SignalProcessor


class ProcessingController:

    def __init__(self, session):

        self.session = session

    # ============================================
    # Bandpass
    # ============================================

    def bandpass(
        self,
        freqmin,
        freqmax,
        corners,
        zerophase
    ):

        filtered = SignalProcessor.bandpass(

            self.session.current_stream,

            freqmin,

            freqmax,

            corners,

            zerophase

        )

        self.session.apply(

            filtered,

            f"Bandpass {freqmin}-{freqmax} Hz"

        )

        return self.session.current_trace()

    # ============================================
    # Restore
    # ============================================

    def restore(self):

        self.session.restore()

        return self.session.current_trace()