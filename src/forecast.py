
from pathlib import Path
import pandas as pd
from .models import ARIMAModel

TRAIN = Path("data/processed/train.csv")
TEST = Path("data/processed/test.csv")
FORECASTS = Path("data/processed/forecasts.csv")

def main():
    train = pd.read_csv(TRAIN)
    test = pd.read_csv(TEST)
    model = ARIMAModel(order=(1,1,1)).fit(train)
    last_rows = test.sort_values(["ticker","date"]).groupby("ticker").tail(1)
    preds = model.predict(last_rows)
    out = last_rows[["ticker","date"]].copy()
    out["forecast_next"] = preds
    out.to_csv(FORECASTS, index=False)
    print(f"Forecasts → {FORECASTS}")

if __name__ == "__main__":
    main()
