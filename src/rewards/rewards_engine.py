import logging


LOGGER = logging.getLogger(__name__)


class RewardsEngine(object):
    def __init__(self, queue_service):
        self._queue_service = queue_service

    def points_from_purchase(self, price):
        return price * 10

    def on_message(self, body):
        LOGGER.info('REWARDS ENGINE message %s', body)
        print(body)
