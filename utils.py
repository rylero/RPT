import sys, yaml

def load_config_files():
    argv = sys.argv
    env_config_filepath = argv[1]
    experiment_config_filepath = argv[2]

    with open(env_config_filepath, "r") as file:
        env_config = yaml.safe_load(file)

    with open(experiment_config_filepath, "r") as file:
        experiment_config = yaml.safe_load(file)
    
    return env_config, experiment_config