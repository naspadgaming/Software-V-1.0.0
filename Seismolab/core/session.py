class Session:

    def __init__(self):

        self.filename = None
        self.original_stream = None
        self.current_stream = None
        self.history = []

    def load(self, filename, stream):

        self.filename = filename

        self.original_stream = stream.copy()

        self.current_stream = stream.copy()

        self.history = ["Load"]

    def apply(self, stream, operation):

        self.current_stream = stream.copy()

        self.history.append(operation)

    def current_trace(self):

        if self.current_stream is None:
            return None

        return self.current_stream[0]

    def info(self):

        text = ""

        if self.current_stream is None:
            return "No file loaded."

        text += str(self.current_stream)

        text += "\n\nHistory\n"

        text += "----------------------\n"

        for h in self.history:

            text += f"{h}\n"

        return text