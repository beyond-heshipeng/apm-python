import threading
import os
from kafka import KafkaConsumer


def read_managements():
    consumer = KafkaConsumer("apm-managements-DEV", bootstrap_servers=os.getenv('APM_COLLECTOR_KAFKA_BOOTSERVERS'))
    for msg in consumer:
        print("msg from managements --- ", msg.value)


def read_segment():
    consumer = KafkaConsumer("apm-segments-DEV", bootstrap_servers=os.getenv('APM_COLLECTOR_KAFKA_BOOTSERVERS'))
    for msg in consumer:
        print("msg from segment --- ", msg.value)


def read_log():
    consumer = KafkaConsumer("apm-log-DEV", bootstrap_servers=os.getenv('APM_COLLECTOR_KAFKA_BOOTSERVERS'))
    for msg in consumer:
        print("msg from log --- ", msg.value)


def read_metric():
    consumer = KafkaConsumer("apm-metrics-DEV", bootstrap_servers=os.getenv('APM_COLLECTOR_KAFKA_BOOTSERVERS'))
    for msg in consumer:
        print("msg from metrics --- ", msg.value)


t1 = threading.Thread(target=read_managements, name="read-managements")
t2 = threading.Thread(target=read_segment, name="read-segment")
t3 = threading.Thread(target=read_log, name="read-log")
t4 = threading.Thread(target=read_metric, name="read-metric")

t1.start()
t2.start()
t3.start()
t4.start()