class SignalProcessor:

    @staticmethod
    def bandpass(stream,
                 freqmin,
                 freqmax,
                 corners=4,
                 zerophase=True):

        new_stream = stream.copy()

        new_stream.filter(
            "bandpass",
            freqmin=freqmin,
            freqmax=freqmax,
            corners=corners,
            zerophase=zerophase
        )

        return new_stream