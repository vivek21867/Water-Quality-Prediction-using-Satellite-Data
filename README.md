# Water Health Prediction Using GIS Data and XGBoost

## Overview

This project leverages Geographic Information System (GIS) data, Google Earth Engine, and Machine Learning to assess and predict water body health. The system extracts environmental indicators from GIS datasets, trains an XGBoost classification model, evaluates water quality conditions, and forecasts future water health trends for upcoming years.

The objective is to support environmental monitoring, water resource management, and sustainability initiatives through data-driven predictions.

---

## Features

* GIS dataset integration using Google Earth Engine
* Automated extraction of water quality indicators
* Data preprocessing and cleaning
* Multi-class water health classification
* XGBoost machine learning model
* Model evaluation using accuracy and classification metrics
* Future water health prediction (2025–2027)
* CSV export of prediction results

---

## Technology Stack

### GIS & Remote Sensing

* Google Earth Engine (GEE)
* Geemap

### Machine Learning

* XGBoost
* Scikit-Learn

### Data Processing

* Pandas
* NumPy

### Programming Language

* Python

---

## Input Parameters

The model uses the following environmental indicators:

| Feature   | Description                       |
| --------- | --------------------------------- |
| Year      | Observation year                  |
| NDWI      | Normalized Difference Water Index |
| WHI       | Water Health Index                |
| TDS_Index | Total Dissolved Solids Index      |
| Turbidity | Water turbidity level             |
| pH        | Acidity/alkalinity level          |

---

## Water Health Categories

The system classifies water quality into three categories:

| Health Status | Label |
| ------------- | ----- |
| Poor          | 0     |
| Moderate      | 1     |
| Excellent     | 2     |

---

## Workflow

### Step 1: GIS Data Collection

Water quality data is retrieved from a Google Earth Engine Feature Collection.

```python
dataset = ee.FeatureCollection(asset_id)
```

### Step 2: Data Cleaning

Missing values are removed to ensure data quality.

```python
df = df.dropna()
```

### Step 3: Feature Engineering

Environmental indicators are selected as model inputs.

```python
X = df[["year","NDWI","WHI","TDS_Index","Turbidity","pH"]]
```

### Step 4: Model Training

An XGBoost classifier is trained using historical water quality records.

```python
model = xgb.XGBClassifier()
model.fit(X_train, y_train)
```

### Step 5: Model Evaluation

Performance is measured using:

* Accuracy Score
* Precision
* Recall
* F1-Score
* Classification Report

### Step 6: Future Prediction

Trend analysis is used to estimate future environmental parameters and predict water health conditions for:

* 2025
* 2026
* 2027

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/water-health-prediction.git

cd water-health-prediction
```

### Install Dependencies

```bash
pip install earthengine-api geemap xgboost pandas scikit-learn
```

---

## Google Earth Engine Authentication

Authenticate your Earth Engine account:

```python
import ee

ee.Authenticate()
ee.Initialize()
```

---

## Configure GIS Dataset

Replace the placeholder asset ID with your Google Earth Engine Feature Collection.

```python
asset_id = "YOUR_GIS_ASSET_LINK"
```

Example:

```python
asset_id = "projects/your-project/assets/water_health_dataset"
```

---

## Running the Project

Execute the notebook or Python script:

```bash
python water_health_prediction.py
```

---

## Sample Output

```text
Model Accuracy: 0.91

Future Prediction

Year    Predicted Health
2025    Excellent
2026    Excellent
2027    Moderate
```

---

## Generated Files

After execution, the system generates:

```text
water_health_predictions_2025_2027.csv
```

This file contains future water health predictions and estimated environmental indicators.

---

## Applications

* Water Quality Monitoring
* Environmental Impact Assessment
* Smart Water Resource Management
* Sustainable Development Planning
* Government Water Quality Surveillance
* GIS-Based Environmental Analytics

---

## Future Enhancements

* Integration with IoT water quality sensors
* Real-time monitoring dashboard
* Deep Learning models (LSTM, GRU)
* Satellite image-based water quality assessment
* Interactive GIS visualization
* Web application deployment using FastAPI and React

---

## Project Structure

```text
Water-Health-Prediction/
│
├── data/
├── notebooks/
├── models/
├── outputs/
│   └── water_health_predictions_2025_2027.csv
│
├── water_health_prediction.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## License

This project is licensed under the MIT License.

---


Chennai, India
