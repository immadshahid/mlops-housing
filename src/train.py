import mlflow
import mlflow.sklearn
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from src.preprocess import load_data

X, y = load_data("data/housing.csv")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

mlflow.set_experiment("housing-mlops")

with mlflow.start_run():

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    mlflow.log_metric("r2_score", score)

    # NEW: log params
    mlflow.log_param("model", "RandomForest")
    mlflow.log_param("n_estimators", 100)

    # log model properly
    mlflow.sklearn.log_model(
        model,
        "model",
        registered_model_name="HousingModel"
    )

    joblib.dump(model, "models/model.pkl")
