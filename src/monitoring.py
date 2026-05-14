from evidently import Report
from evidently.presets import DataDriftPreset
import pandas as pd

df = pd.read_csv("data/housing.csv")

report = Report(metrics=[DataDriftPreset()])
result = report.run(current_data=df, reference_data=df)

result.save_html("drift_report.html")