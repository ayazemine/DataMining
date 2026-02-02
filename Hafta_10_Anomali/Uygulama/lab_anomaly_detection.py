"""
Hafta 10 - Lab: Aykırı Değer (Anomaly) Tespiti
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import StandardScaler

# Veri oluşturma (normal + anomaly)
X_normal, _ = make_blobs(n_samples=300, centers=1, random_state=42)
X_anomaly = np.random.uniform(low=-8, high=8, size=(20, 2))
X = np.vstack([X_normal, X_anomaly])

# Gerçek etiketler (test için)
y_true = np.array([0]*300 + [1]*20)  # 0: normal, 1: anomaly

# Ölçeklendirme
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ============================================================================
# 1. Isolation Forest
# ============================================================================
iso_forest = IsolationForest(contamination=0.1, random_state=42)
y_pred_iso = iso_forest.fit_predict(X_scaled)
# -1: anomaly, 1: normal -> 1: anomaly, 0: normal'e çevir
y_pred_iso = np.where(y_pred_iso == -1, 1, 0)

# ============================================================================
# 2. Local Outlier Factor (LOF)
# ============================================================================
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred_lof = lof.fit_predict(X_scaled)
y_pred_lof = np.where(y_pred_lof == -1, 1, 0)

# ============================================================================
# 3. Z-Score Method
# ============================================================================
from scipy import stats
z_scores = np.abs(stats.zscore(X_scaled))
y_pred_zscore = np.where((z_scores > 3).any(axis=1), 1, 0)

# ============================================================================
# Görselleştirme
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Gerçek etiketler
axes[0, 0].scatter(X[y_true==0, 0], X[y_true==0, 1], c='blue', label='Normal', alpha=0.6)
axes[0, 0].scatter(X[y_true==1, 0], X[y_true==1, 1], c='red', label='Anomaly', alpha=0.8)
axes[0, 0].set_title('Gerçek Etiketler')
axes[0, 0].legend()

# Isolation Forest
axes[0, 1].scatter(X[y_pred_iso==0, 0], X[y_pred_iso==0, 1], c='blue', label='Normal', alpha=0.6)
axes[0, 1].scatter(X[y_pred_iso==1, 0], X[y_pred_iso==1, 1], c='red', label='Anomaly', alpha=0.8)
axes[0, 1].set_title('Isolation Forest')
axes[0, 1].legend()

# LOF
axes[1, 0].scatter(X[y_pred_lof==0, 0], X[y_pred_lof==0, 1], c='blue', label='Normal', alpha=0.6)
axes[1, 0].scatter(X[y_pred_lof==1, 0], X[y_pred_lof==1, 1], c='red', label='Anomaly', alpha=0.8)
axes[1, 0].set_title('Local Outlier Factor (LOF)')
axes[1, 0].legend()

# Z-Score
axes[1, 1].scatter(X[y_pred_zscore==0, 0], X[y_pred_zscore==0, 1], c='blue', label='Normal', alpha=0.6)
axes[1, 1].scatter(X[y_pred_zscore==1, 0], X[y_pred_zscore==1, 1], c='red', label='Anomaly', alpha=0.8)
axes[1, 1].set_title('Z-Score Method')
axes[1, 1].legend()

plt.tight_layout()
plt.show()

# ============================================================================
# Performans Değerlendirme
# ============================================================================
from sklearn.metrics import classification_report, confusion_matrix

print("\n" + "="*60)
print("PERFORMANS KARŞILAŞTIRMASI")
print("="*60)

print("\n1. Isolation Forest:")
print(classification_report(y_true, y_pred_iso, target_names=['Normal', 'Anomaly']))

print("\n2. Local Outlier Factor:")
print(classification_report(y_true, y_pred_lof, target_names=['Normal', 'Anomaly']))

print("\n3. Z-Score Method:")
print(classification_report(y_true, y_pred_zscore, target_names=['Normal', 'Anomaly']))

# Confusion matrices
print("\n" + "="*60)
print("CONFUSION MATRICES")
print("="*60)

print("\nIsolation Forest:")
print(confusion_matrix(y_true, y_pred_iso))

print("\nLOF:")
print(confusion_matrix(y_true, y_pred_lof))

print("\nZ-Score:")
print(confusion_matrix(y_true, y_pred_zscore))
