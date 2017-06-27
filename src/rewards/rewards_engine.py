import logging
import json
from db import Session
from models.user import User


LOGGER = logging.getLogger(__name__)


class RewardsEngine:
    def __init__(self, queue_service, rewards):
        self._queue_service = queue_service
        self._rewards = rewards

    def points_from_cost(self, cost):
        return cost * 10

    def on_message(self, body):
        session = Session()

        LOGGER.info('REWARDS ENGINE message %s', body)
        body = json.loads(body)
        user = session.query(User).filter(User.id == body['user_id']).first()

        user.points += self.points_from_cost(body['cost'])
        session.commit()

        recommended_rewards = self.calculate_recommended_rewards(user)

        self._queue_service.send_message(json.dumps({
            "type": "rewards-recommendation",
            "rewards": recommended_rewards
        }, ensure_ascii=False))

    def calculate_recommended_rewards(self, user):
        recommended_rewards = []
        for reward in self._rewards:
            if user.points >= reward.points:
                for i in range(self._calculate_max_reward_count(user, reward)):
                    recommended_rewards.append({
                        'name': reward.name,
                        'points': reward.points
                    })

        return recommended_rewards

    def _calculate_max_reward_count(self, user, reward):
        reward_count = int(user.points / reward.points)
        if reward_count > reward.max_per_user:
            reward_count = reward.max_per_user
        user.points -= reward.points * reward_count
        return reward_count
