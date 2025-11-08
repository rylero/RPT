from hemac import HeMAC_v0
import utils
import numpy as np

enviorment_config = None
experiment_config = None

def run_experiemnt():
    env = HeMAC_v0.env(**enviorment_config, render_mode="human")
    env.reset(seed=0)

    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()
        if termination or truncation:
            action = None
        else:
            # this is where you would insert your policy
            action = env.action_space(agent).sample()
        env.step(action)
    env.close()

if __name__ == "__main__":
    enviorment_config, experiment_config = utils.load_config_files()
    run_experiemnt()
