class Session:


    def __init__(self):


        self.filename = None

        self.original_stream = None

        self.current_stream = None

        self.history = []


        # trace aktif

        self.selected_trace = 0



    # ======================================
    # Load Stream
    # ======================================

    def load(

        self,

        filename,

        stream

    ):


        self.filename = filename


        self.original_stream = stream.copy()


        self.current_stream = stream.copy()


        self.selected_trace = 0


        self.history = [

            "Load"

        ]



    # ======================================
    # Apply Processing
    # ======================================

    def apply(

        self,

        stream,

        operation

    ):


        self.current_stream = stream.copy()


        self.history.append(

            operation

        )



    # ======================================
    # Get Current Trace
    # ======================================

    def current_trace(

        self,

        index=None

    ):


        if self.current_stream is None:

            return None



        if len(self.current_stream) == 0:

            return None



        if index is None:

            index = self.selected_trace



        if index >= len(self.current_stream):

            index = 0



        self.selected_trace = index



        return self.current_stream[index]



    # ======================================
    # Stream Info
    # ======================================

    def info(self):


        if self.current_stream is None:

            return "No file loaded."



        text = ""



        text += str(
            self.current_stream
        )



        text += "\n\nHistory\n"


        text += "----------------------\n"



        for item in self.history:


            text += f"{item}\n"



        return text