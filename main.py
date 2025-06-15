from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Bagi data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Buat model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Prediksi dan evaluasi
y_pred = model.predict(X_test)
print("Akurasi:", accuracy_score(y_test, y_pred))

# Ambil dua fitur untuk visualisasi sederhana (misalnya panjang sepal & panjang petal)
x_axis = X_test[:, 0]  # sepal length
y_axis = X_test[:, 2]  # petal length

# Warna berdasarkan prediksi
plt.figure(figsize=(8,6))
plt.scatter(x_axis, y_axis, c=y_pred, cmap='viridis', edgecolor='k')
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Visualisasi Prediksi Jenis Bunga Iris")
plt.colorbar(label="Prediksi: 0=Setosa, 1=Versicolor, 2=Virginica")
plt.grid(True)
plt.show()
