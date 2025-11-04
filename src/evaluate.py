
import json
from pathlib import Path
import matplotlib.pyplot as plt

ARTIFACTS = Path("data/processed/metrics.json")
FIG = Path("reports/figures/model_compare.png")

def main():
    metrics = json.loads(ARTIFACTS.read_text())
    names = list(metrics.keys())
    mape_vals = [metrics[n]["mape"] for n in names]

    plt.figure()
    plt.bar(names, mape_vals)
    plt.ylabel("MAPE (lower is better)")
    plt.title("Model Comparison")
    FIG.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(FIG, bbox_inches="tight")
    print(f"Figure saved → {FIG}")

if __name__ == "__main__":
    main()
