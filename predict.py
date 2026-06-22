import joblib
import numpy as np

kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

cluster_names = {
    0: "Active Budget Shoppers",
    1: "Conservative High-Income Customers",
    2: "Selective Affluent Customers",
    3: "Mainstream Consumers"
}

def predict_segment(age, income, spending):
    data = np.array([[age, income, spending]])
    scaled = scaler.transform(data)
    cluster = kmeans.predict(scaled)[0]
    segment = cluster_names[cluster]
    return cluster, segment

cluster, segment = predict_segment(25, 80, 67)

print(cluster)
print(segment)