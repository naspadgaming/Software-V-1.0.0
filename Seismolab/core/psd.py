import numpy as np

from scipy.signal import welch



class PSDAnalyzer:


    def __init__(self, trace):

        self.trace = trace



    # ======================================
    # Calculate PSD
    # ======================================

    def compute(self):


        data = self.trace.data.astype(
            float
        )


        fs = (
            self.trace.stats.sampling_rate
        )



        # remove mean

        data = data - np.mean(
            data
        )



        frequency, power = welch(

            data,

            fs=fs,

            nperseg=1024

        )



        return frequency, power



    # ======================================
    # Peak Frequency
    # ======================================

    def peak_frequency(self):


        frequency, power = self.compute()



        index = np.argmax(
            power
        )


        return frequency[index]