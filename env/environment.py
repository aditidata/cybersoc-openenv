import random

from models.observation import Observation
from models.reward import Reward
from env.tasks import TASKS
from env.graders import grade_action


class CyberSOCEnv:

    def __init__(self):

        self.task_sequence = None
        self.current_step = 0
        self.done = False
        self.state_data = None

    def generate_state(self, alert):

        return Observation(
            alert_type=alert,
            failed_logins=random.randint(0,50),
            malware_detected=(alert == "malware_detected"),
            network_traffic=random.randint(200,1000),
            severity=random.randint(1,5)
        )

    def reset(self):

        self.done = False
        self.current_step = 0

        task_name = random.choice(list(TASKS.keys()))
        self.task_sequence = TASKS[task_name]

        alert = self.task_sequence[self.current_step]["alert"]

        self.state_data = self.generate_state(alert)

        return self.state_data

    def step(self, action):

        correct = self.task_sequence[self.current_step]["correct_action"]

        score = grade_action(action, correct)

        reward = Reward(value=score)

        self.current_step += 1

        if self.current_step >= len(self.task_sequence):

            self.done = True

        else:

            alert = self.task_sequence[self.current_step]["alert"]
            self.state_data = self.generate_state(alert)

        return self.state_data, reward, self.done, {}

    def state(self):

        return self.state_data