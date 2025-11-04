
import json
from pathlib import Path
import pandas as pd
from .models import NaiveLast, LinearModel, ARIMAModel, evaluate

TRAIN = Path("data/processed/train.csv")
TEST = Path("data/processed/test.csv")
ARTIFACTS = Path("data/processed/metrics.json")

def main():
    train = pd.read_csv(TRAIN)
    test = pd.read_csv(TEST)
    X_train, y_train = train, train["close"]
    X_test, y_test = test, test["close"]

    naive = NaiveLast().fit(X_train, y_train)
    ridge = LinearModel("ridge").fit(X_train, y_train)
    lasso = LinearModel("lasso").fit(X_train, y_train)
    arima = ARIMAModel(order=(1,1,1)).fit(train)

    metrics = {
        "naive": vars(evaluate(y_test, naive.predict(X_test))),
        "ridge": vars(evaluate(y_test, ridge.predict(X_test))),
        "lasso": vars(evaluate(y_test, lasso.predict(X_test))),
        "arima": vars(evaluate(y_test, arima.predict(test)))
    }
    ARTIFACTS.write_text(json.dumps(metrics, indent=2))
    print("Saved metrics →", ARTIFACTS)

if __name__ == "__main__":
    main()
