import xgboost as xgb
import pandas as pd
from pathlib import Path
import pickle
from math import radians, cos
from datetime import datetime, date, timedelta
import pandas as pd
from initial_data_pull_test import data_pull
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import mlflow
import os
from sklearn.metrics import root_mean_squared_error, mean_squared_error
import matplotlib.pyplot as plt
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from hyperopt.pyll import scope
from prefect import flow, task
from training_model import nj_transit_locations, find_station



os.environ["AWS_PROFILE"] = "default"

TRACKING_SERVER_HOST = "ec2-3-80-40-111.compute-1.amazonaws.com" # fill in with the public DNS of the EC2 instance
mlflow.set_tracking_uri(f"http://{TRACKING_SERVER_HOST}:5000")
mlflow.set_experiment("north-nj-apartments-experiment-v3")

with open('run_id.txt', 'r') as f_in:
    run_id = f_in.read().strip()

model_uri = f"runs:/{run_id}/models_mlflow"
loaded_model = mlflow.xgboost.load_model(model_uri)
print(loaded_model)