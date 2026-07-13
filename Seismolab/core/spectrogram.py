import numpy as np

from scipy.signal import spectrogram



class SpectrogramAnalyzer:


    def __init__(self, trace):

        self.trace = trace



    # ======================================
    # Compute Spectrogram
    # ======================================

    def compute(self):


        data = self.trace.data.astype(
            float
        )


        fs = (
            self.trace.stats.sampling_rate
        )



        data = data - np.mean(
            data
        )



        frequency, time, power = spectrogram(

            data,

            fs=fs,

            nperseg=256,

            noverlap=128

        )



        return (
            frequency,
            time,
            power
        )