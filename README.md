# 💹 Financial Data Lake with Predictive Analytics

[![CI](https://github.com/asmitc-source/financial-data-lake-predictive-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/asmitc-source/financial-data-lake-predictive-analytics/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

End-to-end project that builds a **financial data lake**, trains **predictive models** (Ridge/Lasso + ARIMA), and ships **interactive Tableau dashboards** for portfolio tracking and risk analysis.

---

## 🔥 Highlights
- Modular pipeline: **ETL → Features → Modeling → Evaluation → Forecasts**
- Models: Naive baseline, **Ridge/Lasso**, **ARIMA**
- Metrics: **MAPE, RMSE** with comparison chart
- **GitHub Actions CI** (lint + tests) on every push
- Tableau preview images + guide to publish dashboards

---

## 🧭 Project Structure
```bash
financial-data-lake-predictive-analytics/
├── src/                  # etl.py, features.py, models.py, train.py, evaluate.py, forecast.py
├── data/processed/       # sample_data.csv + generated outputs
├── dashboards/           # previews + instructions to publish
├── reports/figures/      # generated comparison charts
├── tests/                # lightweight pytest
├── .github/workflows/    # CI pipeline (ci.yml)
├── requirements.txt      # dependencies
├── Makefile              # one-command workflow
└── README.md
