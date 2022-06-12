import argparse
from asyncore import read
import pandas as pd
import yaml


# loading the data from the location where client has put it
# creating a function for the job

def read_params(config_path):
    with open(config_path) as config_yaml:
        config = yaml.safe_load(config_yaml)

    return config


def get_data(config_path):
    config = read_params(config_path)
    data = config['data_location']['data_given_by_client']
    df = pd.read_csv(data)
    return df


if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument('--config', default="params.yaml")
    parsed_args = arg.parse_args()
    get_data(config_path=parsed_args.config)
