import logging

from sqlalchemy import desc
from queue.queue_service import QueueService
from rewards.rewards_engine import RewardsEngine
from models.reward import Reward
from db import Session

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    queue_service = QueueService('amqp://guest:guest@localhost:5672/', 'rewards', 'rewards')
    session = Session()
    rewards = session.query(Reward).order_by(desc(Reward.points)).all()

    queue_service.set_message_handler(RewardsEngine(queue_service, rewards))

    try:
        queue_service.run()
    except KeyboardInterrupt:
        queue_service.stop()


if __name__ == '__main__':
    main()
