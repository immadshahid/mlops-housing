# MLOps Housing Price Prediction Project

This project implements a complete end-to-end MLOps pipeline for housing price prediction. It covers data ingestion, preprocessing, training, serving, monitoring, and CI/CD.

## 🚀 Features

- **Data Pipeline**: Managed with **DVC** (Data Version Control) for reproducibility.
- **Experiment Tracking**: **MLflow** is used to track parameters, metrics, and models.
- **Serving**: A production-ready API built with **FastAPI**.
- **Monitoring**: Data drift reports generated using **Evidently**.
- **CI/CD**: Automated testing, training, and Docker image building via **GitHub Actions**.
- **Containerization**: **Docker** for consistent deployment across environments.

## 📁 Project Structure

```text
mlops-housing/
├── .github/workflows/    # CI/CD pipelines
├── data/                 # Raw and processed data
├── models/               # Serialized model files (.pkl)
├── src/                  # Source code for the ML pipeline
│   ├── preprocess.py     # Data cleaning and feature engineering
│   ├── train.py          # Model training script
│   └── monitoring.py     # Data drift monitoring
├── app.py                # FastAPI application for serving
├── dvc.yaml              # DVC pipeline configuration
├── Dockerfile            # Containerization instructions
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/immadshahid/mlops-housing.git
cd mlops-housing
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/scripts/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 🏃 Running the Project

### Pipeline Execution (DVC)
To run the entire pipeline (preprocessing and training):
```bash
dvc repro
```

### Serving the Model (FastAPI)
Run the API locally:
```bash
uvicorn app:app --reload
```
Access the interactive API docs at `http://127.0.0.1:8000/docs`.

### Model Monitoring
To generate a data drift report:
```bash
python src/monitoring.py
```
This will generate a `drift_report.html` file in the root directory.

## 🐳 Docker Deployment

Build and run the container:
```bash
docker build -t mlops-housing .
docker run -p 8000:8000 mlops-housing
```

## 🤖 CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/mlops.yml`) automatically:
1. Installs dependencies.
2. Runs the training script.
3. Builds a Docker image.

## 📈 Experiment Tracking (MLflow)

To view the experiment logs and model registry:
```bash
mlflow ui
```
Then visit `http://127.0.0.1:5000` in your browser.