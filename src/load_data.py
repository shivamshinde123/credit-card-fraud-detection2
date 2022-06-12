import argparse
import pandas as pd
from get_data import get_data, read_params

# loading the data from the location where client has put it
# then copying the dat into the data/raw folder


def load_and_save(config_path):
    config = read_params(config_path)
    raw_data_path = config['data_location']['raw_data_path']
    df = get_data(config_path)
    df.to_csv(raw_data_path, sep=',', index=False)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)
