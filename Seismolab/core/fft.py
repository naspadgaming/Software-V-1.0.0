import numpy as np



class FFTAnalyzer:


    def __init__(self, trace):

        self.trace = trace



    # ======================================
    # Calculate FFT
    # ======================================

    def compute(self):


        data = self.trace.data.astype(
            float
        )


        sampling_rate = (
            self.trace.stats.sampling_rate
        )



        n = len(data)



        # Remove mean

        data = data - np.mean(
            data
        )



        spectrum = np.fft.fft(
            data
        )


        frequency = np.fft.fftfreq(

            n,

            d=1 / sampling_rate

        )



        # positive frequency only

        mask = frequency >= 0



        frequency = frequency[mask]


        amplitude = np.abs(
            spectrum[mask]
        ) / n



        return frequency, amplitude



    # ======================================
    # Dominant Frequency
    # ======================================

    def dominant_frequency(self):


        freq, amp = self.compute()



        index = np.argmax(
            amp[1:]
        ) + 1



        return freq[index]