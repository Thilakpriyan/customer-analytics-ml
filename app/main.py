from services.ml_api_client import MLApiClient
import numpy as np

client = MLApiClient()

predictions = []
true_labels = []   # from dataset y_final

for i in range(100):  # evaluate first 100 samples
    features = X_final[i]
    true_label = y_final[i]   # actual churn result
    
    result = client.predict_churn(features)
    
    predictions.append(result["prediction"])
    true_labels.append(true_label)
