"""
Hafta 5 - Lab: k-NN Algoritması Uygulaması
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Veri yükleme
iris = load_iris()
X = iris.data
y = iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Ölçeklendirme (k-NN için önemli!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# k-NN modeli
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Tahmin
y_pred = knn.predict(X_test_scaled)

# Değerlendirme
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# En iyi k değerini bulma
k_range = range(1, 31)
k_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train_scaled, y_train, cv=5, scoring='accuracy')
    k_scores.append(scores.mean())

# Görselleştirme
plt.figure(figsize=(10, 6))
plt.plot(k_range, k_scores)
plt.xlabel('k değeri')
plt.ylabel('Cross-Validation Accuracy')
plt.title('En İyi k Değeri Seçimi')
plt.grid(True)
plt.show()

optimal_k = k_range[np.argmax(k_scores)]
print(f"\nEn iyi k değeri: {optimal_k}")
