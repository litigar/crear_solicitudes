import datetime
import os


class UtilLog:
    __instance = None
    file_name = None
    fLog = None

    def __str__(self):
        return 'UtilLogSingleton file_name {} '.format(len(self.file_name))

    def __new__(cls):
        if not UtilLog.__instance:
            UtilLog.__instance = object.__new__(cls)
        return UtilLog.__instance

    @staticmethod
    def get_instance():
        if not UtilLog.__instance:
            UtilLog.__instance = UtilLog()
        return UtilLog.__instance

    def set_file_name(self, new_file_name: str):
        # pathLogsBatch = os.environ.get('local_path')
        # print(f"pathLogsBatch {pathLogsBatch}")
        # print(f"new_file_name {new_file_name}")
        self.file_name = new_file_name
        if self.file_name:
            self.fLog = open(self.file_name, 'a+')
        # print(f"file_log {self.file_name}")

    def write(self, message: str):
        print(message)
        self.fLog.write("{} {}\n".format(datetime.datetime.now(), message))
