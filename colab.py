# =============================
# INSTALL LIBRARIES
# =============================
!pip install earthengine-api geemap xgboost pandas scikit-learn -q

# =============================
# IMPORT LIBRARIES
# =============================
import ee
import geemap
import pandas as pd
import numpy as np
import xgboost as xgb

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# =============================
# AUTHENTICATE EARTH ENGINE
# =============================
ee.Authenticate()
ee.Initialize()

# =============================
# CONNECT GIS DATASET
# replace with your asset link
# =============================
asset_id = "YOUR_GIS_ASSET_LINK"

dataset = ee.FeatureCollection(asset_id)

df = geemap.ee_to_pandas(dataset)

print("Dataset loaded from GIS API")
print(df.head())

# =============================
# DATA CLEANING
# =============================
df = df.dropna()

health_map = {
    "Poor":0,
    "Moderate":1,
    "Excellent":2
}

df["health_label"] = df["health"].map(health_map)

# features
X = df[["year","NDWI","WHI","TDS_Index","Turbidity","pH"]]

# target
y = df["health_label"]

# =============================
# TRAIN TEST SPLIT
# =============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =============================
# XGBOOST MODEL
# =============================
model = xgb.XGBClassifier(
    n_estimators=400,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8
)

model.fit(X_train, y_train)

# =============================
# MODEL ACCURACY
# =============================
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nReport:\n", classification_report(y_test, y_pred))

# =============================
# FUTURE PREDICTION (2025–2027)
# using trend estimation
# =============================
trend = df.diff().mean()

last_row = df.iloc[-1]

future_data = []

for year in [2025, 2026, 2027]:

    next_row = {
        "year": year,
        "NDWI": last_row["NDWI"] + trend["NDWI"],
        "WHI": last_row["WHI"] + trend["WHI"],
        "TDS_Index": last_row["TDS_Index"] + trend["TDS_Index"],
        "Turbidity": last_row["Turbidity"] + trend["Turbidity"],
        "pH": last_row["pH"] + trend["pH"]
    }

    future_data.append(next_row)

    last_row = pd.Series(next_row)

future_df = pd.DataFrame(future_data)

# =============================
# PREDICT FUTURE WATER HEALTH
# =============================
pred = model.predict(future_df)

reverse_map = {
    0:"Poor",
    1:"Moderate",
    2:"Excellent"
}

future_df["Predicted_health"] = [reverse_map[i] for i in pred]

print("\nFuture Prediction")
print(future_df)

# =============================
# SAVE RESULT CSV
# =============================
future_df.to_csv("water_health_predictions_2025_2027.csv", index=False)

print("\nCSV saved successfully")
