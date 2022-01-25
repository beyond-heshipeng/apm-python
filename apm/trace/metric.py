import os
import threading

import psutil
from collections import namedtuple

Thread = namedtuple("Thread", ["liveCount", "daemonCount"])
IO = namedtuple("io", ["readCount", "writeCount", "readBytes", "writeBytes"])


class Metric:
    def __init__(self):
        self.pid = os.getpid()
        self.cpu = 0
        self.memory = 0.0
        self.thread = Thread(liveCount=0, daemonCount=0)
        self.io = IO(0, 0, 0, 0)
        self.created_time = 0.0

    def get_created_time(self):
        process = psutil.Process(self.pid)
        self.created_time = process.create_time()

    def get_cpu_usage(self):
        process = psutil.Process(self.pid)
        self.cpu = process.cpu_percent(1)

    def get_memory(self):
        process = psutil.Process(self.pid)
        self.memory = process.memory_info().rss / 1024.0 / 1024

    def get_thread(self):
        for thread in threading.enumerate():
            if thread.is_alive():
                self.thread = self.thread._replace(liveCount=self.thread.liveCount + 1)
            if thread.isDaemon():
                self.thread = self.thread._replace(daemonCount=self.thread.daemonCount + 1)

    def get_io(self):
        process = psutil.Process(self.pid)
        print(process.io_counters())
        io_counters = process.io_counters()
        self.io = self.io._replace(readCount=io_counters[0])
        self.io = self.io._replace(writeCount=io_counters[1])
        self.io = self.io._replace(readBytes=io_counters[2])
        self.io = self.io._replace(writeBytes=io_counters[3])

    def __repr__(self):
        return (f"create_time-[{self.created_time}], pid-[{self.pid}], cpu-[{self.cpu}],"
                f" memory-[{self.memory}], thread-[{self.thread}]")
