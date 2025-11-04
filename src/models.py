
from dataclasses import dataclass
import numpy as np
import pandas as pd
from typing import Dict
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

@dataclass
class Metrics:
    mape: float
    rmse: float

def evaluate(y_true, y_pred) -> Metrics:
    return Metrics(
        mape=float(mean_absolute_percentage_error(y_true, y_pred)),
        rmse=float(np.sqrt(mean_squared_error(y_true, y_pred)))
    )

class NaiveLast:
    def fit(self, X, y): return self
    def predict(self, X):
        return X["lag_1"].values

class LinearModel:
    def __init__(self, model="ridge"):
        self.model = Ridge(alpha=1.0) if model=="ridge" else Lasso(alpha=0.001, max_iter=5000)
        self.features = ["lag_1","lag_2","lag_3","lag_5","lag_10","cpi_1d","rate_chg"]
    def fit(self, X, y):
        self.model.fit(X[self.features], y)
        return self
    def predict(self, X):
        return self.model.predict(X[self.features])

class ARIMAModel:
    def __init__(self, order=(1,1,1)):
        self.order = order
        self.models: Dict[str, any] = {}
    def fit(self, df: pd.DataFrame, target_col: str = "close"):
        for t, g in df.groupby("ticker"):
            self.models[t] = ARIMA(g[target_col], order=self.order).fit()
        return self
    def predict(self, df_future: pd.DataFrame):
        preds = []
        for _, row in df_future.iterrows():
            t = row["ticker"]
            preds.append(self.models[t].forecast(1).iloc[0])
        return np.array(preds)
