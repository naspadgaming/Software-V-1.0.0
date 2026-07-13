import sqlite3

from pathlib import Path



class EventDatabase:



    def __init__(self, db_name="events.db"):


        base = Path(__file__).parent.parent



        self.db_path = (

            base / db_name

        )



        self.connection = None



        self.connect()

        self.create_table()



    # ======================================
    # Connect Database
    # ======================================

    def connect(self):


        self.connection = sqlite3.connect(

            self.db_path

        )



    # ======================================
    # Create Table
    # ======================================

    def create_table(self):


        query = """

        CREATE TABLE IF NOT EXISTS events

        (

            id INTEGER PRIMARY KEY AUTOINCREMENT,


            filename TEXT,


            start_time TEXT,


            station TEXT,


            network TEXT,


            channel TEXT,


            magnitude REAL,


            location TEXT


        )

        """



        cursor = self.connection.cursor()



        cursor.execute(

            query

        )



        self.connection.commit()



    # ======================================
    # Insert Event
    # ======================================

    def add_event(self, event):


        query = """

        INSERT INTO events

        (

            filename,

            start_time,

            station,

            network,

            channel,

            magnitude,

            location

        )


        VALUES

        (?,?,?,?,?,?,?)

        """



        cursor = self.connection.cursor()



        cursor.execute(

            query,

            (

                event.filename,

                event.start_time,

                event.station,

                event.network,

                event.channel,

                event.magnitude,

                event.location

            )

        )



        self.connection.commit()



        return cursor.lastrowid



    # ======================================
    # Get All Events
    # ======================================

    def get_events(self):


        cursor = self.connection.cursor()



        cursor.execute(

            "SELECT * FROM events ORDER BY id DESC"

        )



        return cursor.fetchall()



    # ======================================
    # Get Event By ID
    # ======================================

    def get_event(self,event_id):


        cursor = self.connection.cursor()



        cursor.execute(

            "SELECT * FROM events WHERE id=?",

            (

                event_id,

            )

        )



        return cursor.fetchone()



    # ======================================
    # Delete Event
    # ======================================

    def delete_event(self,event_id):


        cursor = self.connection.cursor()



        cursor.execute(

            "DELETE FROM events WHERE id=?",

            (

                event_id,

            )

        )



        self.connection.commit()



    # ======================================
    # Close
    # ======================================

    def close(self):


        if self.connection:


            self.connection.close()