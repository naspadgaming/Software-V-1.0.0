import numpy as np

from obspy.signal.trigger import (
    classic_sta_lta,
    trigger_onset
)



class TriggerAnalyzer:


    def __init__(
        self,
        trace
    ):

        self.trace = trace



    # ======================================
    # STA/LTA Calculation
    # ======================================

    def compute(

        self,

        sta_seconds=1,

        lta_seconds=10

    ):


        data = self.trace.data.astype(
            float
        )


        fs = (
            self.trace.stats.sampling_rate
        )



        sta = int(
            sta_seconds * fs
        )


        lta = int(
            lta_seconds * fs
        )



        cft = classic_sta_lta(

            data,

            sta,

            lta

        )


        return cft



    # ======================================
    # Trigger Detection
    # ======================================

    def detect(

        self,

        threshold_on=3,

        threshold_off=1

    ):


        cft = self.compute()



        triggers = trigger_onset(

            cft,

            threshold_on,

            threshold_off

        )


        return triggers