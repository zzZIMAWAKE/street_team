import unittest

from src.queue.queue_service import QueueService
from src.rewards.rewards_engine import RewardsEngine


class TestRewardsEngine(unittest.TestCase):

    def test_points_from_purchase(self):
        rewards = RewardsEngine(QueueService(3, 'rewards', 'rewards'))
        self.assertEqual(rewards.points_from_purchase(10), 100)
