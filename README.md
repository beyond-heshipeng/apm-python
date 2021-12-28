## Install 

```shell
git clone https://github.com/beyond-heshipeng/apm-python
cd apm-python
pip install -r requirements.txt
git submodule update --init
make install
```

## Usage

```shell
sw-python run command [args...]
```

for example: 
```shell
sw-python run python3 test.py
```

## Config
| parameters | describe | default |
| :-----| :---- | :---- |
| ENV | environment | DEV |
| SW_AGENT_PROTOCOL | protocol | kafka |
| APM_COLLECTOR_KAFKA_BOOTSERVERS | kafka bootstrap servers | localhost:9092 |
| SW_KAFKA_REPORTER_TOPIC_MANAGEMENT | management report topic | apm-managements-{ENV} |
| SW_KAFKA_REPORTER_TOPIC_SEGMENT | segement report topic | apm-segments-{ENV} |
| SW_KAFKA_REPORTER_TOPIC_LOG | log report topic | apm-log-{ENV} |
| SW_KAFKA_REPORTER_TOPIC_METRIC | metrics report topic | apm-metrics-{ENV} |