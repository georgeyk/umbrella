import time
import signal
import os
import sys
import logging
import random
from functools import partial

from confluent_kafka import Producer

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("producer")


def _error_handler(*args, producer):
    logger.info("shutting_down")
    producer.flush()
    sys.exit(0)


def _message_callback(err, msg):
    logger.info(f"message_produced, err={err}, msg={msg}")


def _run_forever(producer, topic):
    while True:
        producer.produce(
            topic=topic,
            key="number",
            value=f"{random.randint(1, 10000)}",
            callback=_message_callback,
        )
        producer.flush()
        time.sleep(0.3)


def main():
    config = {
        "client.id": "producer-test-1",
        "bootstrap.servers": os.environ.get("KAFKA_BROKER", "localhost:9092"),
        "acks": "all",
    }
    producer = Producer(config)
    signal.signal(signal.SIGINT, partial(_error_handler, producer=producer))
    topic = os.environ.get("KAFKA_TOPIC", "kafka-test-topic")

    logger.info(f"starting_producer, topic={topic}")
    _run_forever(producer, topic)


if __name__ == "__main__":
    main()
