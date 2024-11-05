import signal
import os
import sys
import logging
from functools import partial

from confluent_kafka import Consumer

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("consumer")


def _error_handler(*args, consumer):
    logger.info("shutting_down")
    consumer.close()
    sys.exit(0)


def _run_forever(consumer, topic):
    consumer.subscribe([topic])
    while True:
        match consumer.poll(timeout=1):
            case None:
                continue
            case err if err.error():
                logger.info(f"msg_err, err={err.error()}")
            case msg:
                dumped = {
                    "topic": msg.topic(),
                    "key": msg.key().decode("utf-8"),
                    "value": msg.value().decode("utf-8"),
                }
                logger.info(f"msg_received, msg={dumped}")
                consumer.commit(msg, asynchronous=False)


def main():
    config = {
        "client.id": "consumer-test-1",
        "bootstrap.servers": os.environ.get("KAFKA_BROKER", "localhost:9092"),
        "group.id": "consumer-group-1",
        "auto.offset.reset": "smallest",
        "enable.auto.commit": False,
    }
    consumer = Consumer(config)
    signal.signal(signal.SIGINT, partial(_error_handler, consumer=consumer))
    topic = os.environ.get("KAFKA_TOPIC", "kafka-test-topic")

    logger.info(f"starting_consumer, topic={topic}")
    _run_forever(consumer, topic)


if __name__ == "__main__":
    main()
