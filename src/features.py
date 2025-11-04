
from pathlib import Path
import pandas as pd

CLEAN = Path("data/processed/clean.csv")
FEATS = Path("data/processed/features.csv")
SPLIT_DATE = "2024-07-01"

def main():
    df = pd.read_csv(CLEAN, parse_dates=["date"])
    df = df.sort_values(["ticker","date"]).reset_index(drop=True)
    df["return_1d"] = df.groupby("ticker")["close"].pct_change()
    for l in [1,2,3,5,10]:
        df[f"lag_{l}"] = df.groupby("ticker")["close"].shift(l)
    df["cpi_1d"] = df["macro_cpi"].pct_change()
    df["rate_chg"] = df["macro_rate"].diff()
    df = df.dropna()
    df.to_csv(FEATS, index=False)
    print(f"Features → {FEATS}")
    train = df[df["date"] < SPLIT_DATE]
    test  = df[df["date"] >= SPLIT_DATE]
    train.to_csv("data/processed/train.csv", index=False)
    test.to_csv("data/processed/test.csv", index=False)
    print("Train/Test splits saved.")

if __name__ == "__main__":
    main()
