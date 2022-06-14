import numpy as np
from src.get_data import read_params
import joblib

config_path = "params.yaml"

class InvalidInput(Exception):

    def __init__(self, message="Input should be either 1 or 0"):
        self.message = message
        super().__init__(message)


def validate_input(dict_request):

    bool_list = []
    
    for key in ["repeat_retailer","used_chip","used_pin_number","online_order"]:
        if int(dict_request[key]) in [1,0]:
            bool_list.append(True)

    if False in bool_list:
        raise InvalidInput
    else:
        return True


def Predict(data):

    config = read_params(config_path)
    model_dir = config['Prediction_service']['model_dir']
    model = joblib.load(model_dir)

    prediction = model.predict(data)
    prediction = int(prediction[0])

    if prediction in [1,0]:
        if prediction == 0:
            return "The performed transaction is NOT FRAUD"
        elif prediction == 1:
            return "The preformed transaction is FRAUD"
    else:
        raise Exception('Something unexpected happened! Try again!')


def form_response(dict_request):

    data = dict_request.values()
    data = np.array([list(map(float,data))])      # Another set of closed brackets used since we need 2D array for predict method to work)

    if validate_input(dict_request):
        response = Predict(data)
        return response
    

def api_response(dict_request):


    data = dict_request.values()
    data = np.array([list(map(float,data))])      # Another set of closed brackets used since we need 2D array for predict method to work

   
    if validate_input(dict_request):
        response = Predict(data)
        return response
    

    
    

