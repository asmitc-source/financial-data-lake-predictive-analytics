
from pathlib import Path
import pandas as pd
from pydantic import BaseModel, ValidationError

DATA_IN = Path("data/processed/sample_data.csv")
DATA_OUT = Path("data/processed/clean.csv")

class Row(BaseModel):
    date: str
    ticker: str
    close: float
    volume: int
    macro_cpi: float
    macro_rate: float

def main():
    df = pd.read_csv(DATA_IN)
    for i, row in df.iterrows():
        try:
            Row(**row.to_dict())
        except ValidationError as e:
            raise RuntimeError(f"Row {i} failed validation: {e}")
    df = df.sort_values(["ticker","date"]).reset_index(drop=True)
    df.to_csv(DATA_OUT, index=False)
    print(f"Clean data → {DATA_OUT}")

if __name__ == "__main__":
    main()
