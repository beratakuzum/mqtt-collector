"""
Classes implementing queue data type.
"""

from queue import Queue, Empty


# A singleton class implementing queue data structure and its functions. This class will be used for storing
# events the mqtt client emits.
class DataQueue:
    __instance = None

    def __init__(self):

        if DataQueue.__instance is not None:
            raise Exception("Cannot initiate the class. It's singleton!")
        else:
            DataQueue.__instance = self
            self.queue = Queue()

    @staticmethod
    def get_instance():
        if DataQueue.__instance is None:
            DataQueue()
        return DataQueue.__instance

    def size(self):
        return self.queue.qsize()

    def add(self, event, schema_name):
        data = {"event": event, "schema_name": schema_name}
        self.queue.put(data)

    def get(self):
        try:
            data = self.queue.get(block=False)
        except Empty as e:
            return None
        return data