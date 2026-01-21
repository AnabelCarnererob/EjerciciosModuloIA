# src/train.py

import pandas as pd
import matplotlib.pyplot as plt
import json
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import joblib

# -----------------------
# 1. Cargar dataset -  Dataset de Flores
# -----------------------
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

# -----------------------
# 2. Información básica
# -----------------------
print("Primeras filas:")
print(X.head())
print("\nEstadísticas descriptivas:")
print(X.describe())
print("\nDistribución de clases:")
print(y.value_counts())

# -----------------------
# 3. EDA mínima
# -----------------------
# Graficamos un scatter entre dos features

# Tamaño de grafico:
plt.figure(figsize=(6,4))
# Crear punto por flor
plt.scatter(X['sepal length (cm)'], X['sepal width (cm)'], c=y, cmap='viridis')
# Etiquetas y titulo en el grafico
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Scatter plot de Sepal Length vs Sepal Width')
# Muestra la leyenda de colores
plt.colorbar(label='Clase')
# Guardar el grafico en PNG
plt.savefig('eda_scatter.png')
# Mostrar el grafico en pantalla
plt.show()

# Observación: podemos notar que las clases 0 y 1 están bastante separadas, mientras que la clase 2 se superpone con la 1 en algunas áreas.

# -----------------------
# 4. Train-test split
# -----------------------

# Dividir datos de prueba y datos de entrenamiento 
X_train, X_test, y_train, y_test = train_test_split(
    # test_size=0.2 → 20% de los datos se usan para prueba, 80% para entrenamiento.
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------
# 5. Pipeline + Entrenamiento
# -----------------------
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier(random_state=42))
])
# Ajusta el pipeline a los datos de entrenamiento:
#  - Primero normaliza los datos.
#  - Luego entrena el modelo sobre esos datos.
pipeline.fit(X_train, y_train)

# -----------------------
# 6. Evaluación
# -----------------------

# Predice las clases del conjunto de prueba.
y_pred = pipeline.predict(X_test)
# Porcentaje de predicciones correctas
acc = accuracy_score(y_test, y_pred)
# F1 score promedio macro (considera todas las clases igual).
f1 = f1_score(y_test, y_pred, average='macro')
# Matriz que muestra aciertos y errores por clase
cm = confusion_matrix(y_test, y_pred)

# Mostrar por pantalla
print(f"\nAccuracy: {acc:.4f}")
print(f"F1 Score (macro): {f1:.4f}")
print("Confusion Matrix:")
print(cm)

# -----------------------
# 7. Persistencia
# -----------------------
# Guardar modelo - Guarda el pipeline entrenado en un archivo .joblib.
joblib.dump(pipeline, 'model.joblib')
print("\nModelo guardado en 'model.joblib'")

# Guardar métricas - Creamos un diccionario con las métricas importantes.
metrics = {
    'accuracy': acc,
    'f1_score_macro': f1,
    'confusion_matrix': cm.tolist()  # Convierte la matriz de confusión de NumPy a lista para que sea compatible con JSON.
}

# Abre un archivo JSON para escritura
with open('metrics.json', 'w') as f:
    #Guarda las métricas en el archivo de forma legible.
    json.dump(metrics, f, indent=4)

print("Métricas guardadas en 'metrics.json'")
