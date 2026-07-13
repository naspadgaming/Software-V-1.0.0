from obspy import read


class SeismicReader:

    @staticmethod
    def load(filepath):
        return read(filepath)