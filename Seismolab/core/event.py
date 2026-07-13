from datetime import datetime



class SeismicEvent:


    def __init__(

        self,

        event_id=None,

        filename=None,

        start_time=None,

        station=None,

        network=None,

        channel=None,

        magnitude=None,

        location=None

    ):


        self.event_id = event_id


        self.filename = filename


        self.start_time = start_time


        self.station = station


        self.network = network


        self.channel = channel


        self.magnitude = magnitude


        self.location = location



    # ======================================
    # Create Event From ObsPy Stream
    # ======================================

    @classmethod
    def from_stream(

        cls,

        filename,

        stream

    ):


        if stream is None or len(stream) == 0:

            return None



        trace = stream[0]



        stats = trace.stats



        return cls(


            filename=filename,


            start_time=str(

                stats.starttime

            ),


            station=getattr(

                stats,

                "station",

                ""

            ),


            network=getattr(

                stats,

                "network",

                ""

            ),


            channel=getattr(

                stats,

                "channel",

                ""

            )

        )



    # ======================================
    # Dictionary Format
    # ======================================

    def to_dict(self):


        return {


            "event_id":
            self.event_id,


            "filename":
            self.filename,


            "start_time":
            self.start_time,


            "station":
            self.station,


            "network":
            self.network,


            "channel":
            self.channel,


            "magnitude":
            self.magnitude,


            "location":
            self.location

        }



    # ======================================
    # String Display
    # ======================================

    def summary(self):


        return (

            f"Event : {self.event_id}\n"

            f"Time : {self.start_time}\n"

            f"Station : {self.station}\n"

            f"Channel : {self.channel}\n"

            f"Magnitude : {self.magnitude}\n"

            f"Location : {self.location}"

        )