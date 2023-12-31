from citylearn.citylearn import CityLearnEnv
from stable_baselines3.common.callbacks import BaseCallback
from typing import List
import numpy as np

class CustomCallback(BaseCallback):
    def __init__(self, env: CityLearnEnv):
        r"""Initialize CustomCallback.

        Parameters
        ----------
        env: Mapping[str, CityLearnEnv]
            CityLearn environment instance.
        loader: IntProgress
            Progress bar.
        """

        super().__init__(verbose=0)
        self.step_count = 0
        self.env = env
        self.reward_history = [0]

    def _on_step(self) -> bool:
        r"""Called each time the env step function is called."""

        if self.env.time_step == 0:
            self.reward_history.append(0)

        else:
            self.reward_history[-1] += sum(self.env.rewards[-1])

        self.step_count += 1

        return True


class SACDCallback(BaseCallback):
    def __init__(self, env: CityLearnEnv, weights_vector: List[float] = [1]):
        r"""Initialize CustomCallback.

        Parameters
        ----------
        env: Mapping[str, CityLearnEnv]
            CityLearn environment instance.
        loader: IntProgress
            Progress bar.
        """

        super().__init__(verbose=0)
        self.step_count = 0
        self.env = env
        self.reward_history = [0]
        self.weights_vector = weights_vector

    def _on_step(self) -> bool:
        r"""Called each time the env step function is called."""

        if self.env.time_step == 0:
            self.reward_history.append(0)

        else:
            self.reward_history[-1] += np.dot(np.array(self.env.rewards[-1]),np.array(self.weights_vector))

        self.step_count += 1

        return True