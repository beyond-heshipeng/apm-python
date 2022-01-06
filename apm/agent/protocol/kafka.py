#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging
from queue import Queue, Empty
from time import time

from apm import config
from apm.agent import Protocol
from apm.client.kafka import (KafkaServiceManagementClient, KafkaTraceSegmentReportService, KafkaLogDataReportService,
                              KafkaMetricReportService)
from apm.loggings import logger, getLogger, logger_debug_enabled
from apm.protocol.common.Common_pb2 import KeyStringValuePair
from apm.trace.metric import Metric
from apm.protocol.language_agent.Tracing_pb2 import SegmentObject, SpanObject, Log, SegmentReference

from apm.protocol.logging.Logging_pb2 import LogData
from apm.trace.segment import Segment

# avoid too many kafka logs
logger_kafka = getLogger('kafka')
logger_kafka.setLevel(max(logging.WARN, logger.level))


class KafkaProtocol(Protocol):
    def __init__(self):
        self.service_management = KafkaServiceManagementClient()
        self.traces_reporter = KafkaTraceSegmentReportService()
        self.log_reporter = KafkaLogDataReportService()
        self.metric_reporter = KafkaMetricReportService()

    def heartbeat(self):
        self.service_management.send_heart_beat()

    def report(self, queue: Queue, block: bool = True):
        start = None

        def generator():
            nonlocal start

            while True:
                try:
                    timeout = config.QUEUE_TIMEOUT  # type: int
                    if not start:  # make sure first time through queue is always checked
                        start = time()
                    else:
                        timeout -= int(time() - start)
                        if timeout <= 0:  # this is to make sure we exit eventually instead of being fed continuously
                            return
                    segment = queue.get(block=block, timeout=timeout)  # type: Segment
                except Empty:
                    return

                queue.task_done()
                if logger_debug_enabled:
                    logger.debug('reporting segment %s', segment)

                s = SegmentObject(
                    traceId=str(segment.related_traces[0]),
                    traceSegmentId=str(segment.segment_id),
                    service=config.service_name,
                    serviceInstance=config.service_instance,
                    spans=[SpanObject(
                        spanId=span.sid,
                        parentSpanId=span.pid,
                        startTime=span.start_time,
                        endTime=span.end_time,
                        operationName=span.op,
                        peer=span.peer,
                        spanType=span.kind.name,
                        spanLayer=span.layer.name,
                        componentId=span.component.value,
                        isError=span.error_occurred,
                        logs=[Log(
                            time=int(log.timestamp * 1000),
                            data=[KeyStringValuePair(key=item.key, value=item.val) for item in log.items],
                        ) for log in span.logs],
                        tags=[KeyStringValuePair(
                            key=tag.key,
                            value=str(tag.val),
                        ) for tag in span.iter_tags()],
                        refs=[SegmentReference(
                            refType=0 if ref.ref_type == 'CrossProcess' else 1,
                            traceId=ref.trace_id,
                            parentTraceSegmentId=ref.segment_id,
                            parentSpanId=ref.span_id,
                            parentService=ref.service,
                            parentServiceInstance=ref.service_instance,
                            parentEndpoint=ref.endpoint,
                            networkAddressUsedAtPeer=ref.client_address,
                        ) for ref in span.refs if ref.trace_id],
                    ) for span in segment.spans],
                )

                yield s

        self.traces_reporter.report(generator())

    def report_log(self, queue: Queue, block: bool = True):
        start = None

        def generator():
            nonlocal start

            while True:
                try:
                    timeout = config.QUEUE_TIMEOUT  # type: int
                    if not start:  # make sure first time through queue is always checked
                        start = time()
                    else:
                        timeout -= int(time() - start)
                        if timeout <= 0:  # this is to make sure we exit eventually instead of being fed continuously
                            return
                    log_data = queue.get(block=block, timeout=timeout)  # type: LogData
                except Empty:
                    return
                queue.task_done()

                if logger_debug_enabled:
                    logger.debug('Reporting Log')

                yield log_data

        self.log_reporter.report(generator=generator())

    def report_metric(self):

        metric = Metric()
        # 计算进程运行时间
        metric.get_created_time()
        # 计算进程占用内存
        metric.get_memory()
        # 计算进程占用CPU
        metric.get_cpu_usage()
        # 计算进程的线情况
        metric.get_thread()
        # 计算io情况
        metric.get_io()

        self.metric_reporter.report(metric)
