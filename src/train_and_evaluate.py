import argparse
from get_data import read_params
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
import json
import os
import joblib

def train_and_evaluate(config_path):

    config = read_params(config_path)

    random_state = config['General']['random_state']
    train_data_path = config["data_location"]["train_data_path"]
    test_data_path = config["data_location"]["test_data_path"]

    train = pd.read_csv(train_data_path)
    test = pd.read_csv(test_data_path)

    target_col = config["General"]["target_col"]

    train_y = train[target_col]
    test_y = test[target_col]

    train_X = train.drop(columns=target_col, axis=1)
    test_X = test.drop(columns=target_col, axis=1)

    knc = KNeighborsClassifier()
    knc.fit(train_X, train_y)

    y_pred = knc.predict(test_X)

    precision, recall, f1 = evaluate_metrics(test_y, y_pred)

    ## saving the paramters and metrics in the json file
    with open("reports/scores.json" ,"w") as json_file:
        d = dict()
        d['precision_score'] = precision
        d['recall_score'] = recall
        d['f1_score'] = f1

        json.dump(d, json_file, indent=4)

    model_dir = os.path.join("models", "model.joblib")

    joblib.dump(knc, model_dir)


def evaluate_metrics(y_true, y_pred):

    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    return precision, recall, f1



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)