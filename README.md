# 💹 Financial Data Lake with Predictive Analytics  

> **End-to-end project** integrating data engineering, time series modeling, and interactive Tableau dashboards for financial forecasting and portfolio insights.  

---

### 🏫 Project Overview  
Developed as part of an **IIT Roorkee** analytics project *(Jan 2025 – Apr 2025)*.  
This project builds a **Financial Data Lake** containing thousands of stock and macroeconomic records, applies **predictive models**, and creates **interactive Tableau dashboards** for portfolio tracking and risk analysis.  

---

### 🚀 Features  
✅ Automated ETL pipeline for stock & macroeconomic data  
✅ Feature engineering with lags, returns, and macro indicators  
✅ Predictive modeling using:
   - Multiple Linear Regression (Ridge / Lasso)
   - ARIMA Time-Series Forecasting  
✅ Evaluation with **MAPE** and **RMSE**  
✅ 4 Tableau dashboards for:
   - Portfolio Overview  
   - Risk & Drawdown  
   - Forecast Drill-down  
   - Sector Heatmap  

---

### 🧠 Tech Stack
| Area | Tools / Libraries |
|------|--------------------|
| Data Processing | Python (Pandas, NumPy, Pydantic) |
| Modeling | Scikit-Learn, Statsmodels |
| Visualization | Matplotlib, Tableau |
| Workflow | Makefile, GitHub Actions CI |
| Environment | Conda / Virtualenv |

---

### 📈 Results
- Achieved **~18% improvement** in forecast accuracy vs. naive baseline  
- Clean modular design with reproducible pipeline  
- Exported results and dashboards to aid portfolio management  

---

### 🗂️ Folder Structure
financial-data-lake-predictive-analytics/
│
├── src/ # ETL, feature engineering, models, training scripts
├── data/processed/ # Cleaned & processed datasets
├── dashboards/ # Tableau dashboards + previews
├── reports/figures/ # Auto-generated comparison charts
├── tests/ # Lightweight pytest suite
├── .github/workflows/ # CI/CD with lint & tests
├── requirements.txt # Dependencies
├── Makefile # One-command workflow
└── README.md # Project documentation

---

### ⚙️ How to Run Locally

# 1️⃣ Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate      # (Windows: .venv\Scripts\activate)

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run full pipeline
make all
📊 Dashboards (Tableau)

Portfolio Overview – performance trends & cumulative returns

Risk Analysis – drawdowns & volatility tracking

Forecast Drill-down – model comparison & forecasts

Sector Heatmap – return-based heatmap visualization

(Add your Tableau Public dashboard links here once published.)

🧾 License

Licensed under the MIT License

👤 Author

Asmit
📧 asmit_c@me.iitr.ac.in
⭐ https://github.com/asmitc-source
