import os
import threading

import psutil
from collections import namedtuple


Thread = namedtuple("thread", ["liveCount", "daemonCount"])
IO = namedtuple("io", ["readCount", "writeCount", "readBytes", "writeBytes"])


class Metric:
    def __init__(self):
        self.pid = os.getpid()
        self.cpu = 0
        self.memory = 0
        self.thread = Thread(0, 0)
        self.io = IO(0, 0, 0, 0)
        self.created_time = 0

    def get_created_time(self):
        process = psutil.Process(self.pid)
        self.created_time = process.create_time()

    def get_cpu_usage(self):
        process = psutil.Process(self.pid)
        self.cpu = process.cpu_percent()
        print(self.cpu)

    def get_memory(self):
        process = psutil.Process(self.pid)
        self.memory = process.memory_info()[0] / 2. ** 30 * 1024

    def get_thread(self):
        for thread in threading.enumerate():
            if thread.is_alive():
                self.thread._replace(liveCount=self.thread.liveCount + 1)
            if thread.isDaemon():
                self.thread._replace(daemonCount=self.thread.daemonCount + 1)

    def get_io(self):
        process = psutil.Process(self.pid)
        # print(process.io_counters())
        # io_counters = process.io_counters()
        # self.io.readCount = io_counters["read_count"]
        # self.io.writeCount = io_counters["write_count"]
        # self.io.readBytes = io_counters["readBytes"]
        # self.io.writeBytes = io_counters["writeBytes"]
