import logging


LOGGER = logging.getLogger(__name__)


class RewardsEngine(object):

    # Store this here for now till I think of how we should get this data in to the Engine.
    REWARDS = {"rewards": [
        {"name": "General Ticket", "category": 1, "points": 100, "max_per_user": 5, "global_max": 1000},
        {"name": "VIP Ticket", "category": 1, "points": 1000, "max_per_user": 1, "global_max": 50},
        {"name": "Weekend Ticket", "category": 2, "points": 250, "max_per_user": 2, "global_max": 500},
        {"name": "Free Drink Voucher", "category": 3, "points": 50, "max_per_user": 10},
        {"name": "Free Limo to event", "category": 4, "points": 5000, "max_per_user": 1, "global_max": 1}
    ]
    }

    def __init__(self, queueService):
        self._queueService = queueService

    def points_from_purchase(self, price):
        return price * 10

    def on_message(self, body):
        LOGGER.info('REWARDS ENGINE message %s', body)
