import logging

from queue.queue_service import QueueService
from rewards.rewards_engine import RewardsEngine

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    queue_service = QueueService('amqp://guest:guest@192.168.99.100:5672/', 'rewards', 'rewards')

    queue_service.set_message_handler(RewardsEngine(queue_service))

    try:
        queue_service.run()
    except KeyboardInterrupt:
        queue_service.stop()


if __name__ == '__main__':
    main()
