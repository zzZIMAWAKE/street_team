import unittest

from src.queue.queue_service import QueueService
from src.rewards.rewards_engine import RewardsEngine
from src.models.user import User


class TestRewardsEngine(unittest.TestCase):

    def test_points_from_purchase(self):
        rewards = RewardsEngine(QueueService(3, 'rewards', 'rewards'))
        self.assertEqual(rewards.points_from_purchase(10), 100)

    def test_calculate_recommended_rewards(self):
        user = User(id=19, points=600)

        rewards = RewardsEngine(QueueService(3, 'rewards', 'rewards'))
        expected_response = {
            'Weekend Ticket': 2,
            'General Ticket': 1
        }

        self.assertEqual(rewards.calculate_recommended_rewards(user), expected_response)
