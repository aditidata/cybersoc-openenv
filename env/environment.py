from models.observation import Observation
from models.reward import Reward
from env.tasks import TASKS
from env.graders import grade_action
import random

class CyberSOCEnv:

    def __init__(self):
        self.current_task = None
        self.state_data = None
        self.done = False

    def reset(self):

        self.done = False
        task_name = random.choice(list(TASKS.keys()))
        self.current_task = TASKS[task_name]

        self.state_data = Observation(
            alert_type=self.current_task["alert_type"],
            failed_logins=self.current_task["failed_logins"],
            malware_detected=self.current_task["malware_detected"],
            network_traffic=self.current_task["network_traffic"],
            severity=self.current_task["severity"]
        )

        return self.state_data

    def step(self, action):

        correct = self.current_task["correct_action"]

        score = grade_action(action, correct)

        reward = Reward(value=score)

        self.done = True

        return self.state_data, reward, self.done, {}

    def state(self):
        return self.state_data