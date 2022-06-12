import argparse
from sklearn.model_selection import train_test_split
from get_data import read_params
import pandas as pd



def split_data(config_path):
    
    config = read_params(config_path)

    raw_data_path = config['data_location']['raw_data_path']
    random_state = config['General']['random_state']
    test_size = config['General']['test_size']
    train_data_path = config['data_location']['train_data_path']
    test_data_path = config['data_location']['test_data_path']

    df = pd.read_csv(raw_data_path)

    train, test = train_test_split(df, random_state=random_state, test_size=test_size)

    train.to_csv(train_data_path, index=False, sep=',')
    test.to_csv(test_data_path, index=False, sep=',')



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default="params.yaml")
    parsed_args = args.parse_args()
    split_data(config_path=parsed_args.config)

