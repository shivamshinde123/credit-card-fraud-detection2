import argparse
from asyncore import read
import pandas as pd
import yaml


# loading the data from the location where client has put it
# creating a function for the job

def read_params(config_path):

    """This method is used to read the parameters from the parameters yaml file

    Args:
        config_path (str): Path to the parameters yaml file
    Returns:
        loaded yaml file : Returns a loaded yaml file
    """

    with open(config_path) as config_yaml:
        config = yaml.safe_load(config_yaml)
    return config


def get_data(config_path):

    """This method is used to read and return a dataframe 

    Args:
        config_path (str): Path to the parameters yaml file

    Returns:
        dataframe  : Returns a dataframe variable
    """
    config = read_params(config_path)
    data = config['data_location']['data_given_by_client']
    df = pd.read_csv(data)
    return df


if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument('--config', default="params.yaml")
    parsed_args = arg.parse_args()
    get_data(config_path=parsed_args.config)
