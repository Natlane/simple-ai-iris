# 🌸 Simple AI - Iris Flower Classifier

Proyek Python sederhana untuk memprediksi jenis bunga Iris menggunakan algoritma **Decision Tree** dari `scikit-learn`.

Dataset ini adalah dataset klasik dalam machine learning yang terdiri dari tiga spesies bunga iris: **Setosa**, **Versicolor**, dan **Virginica**, yang diklasifikasikan berdasarkan ukuran sepal dan petal.

---

## 📊 Dataset
Dataset ini diambil dari modul `sklearn.datasets`:

- 150 sampel bunga iris
- 4 fitur:
  - Sepal length (cm)
  - Sepal width (cm)
  - Petal length (cm)
  - Petal width (cm)
- 3 kelas (label):
  - `0`: Setosa
  - `1`: Versicolor
  - `2`: Virginica

---

## 🧠 Model Machine Learning

Menggunakan algoritma:
- `DecisionTreeClassifier` dari `sklearn.tree`

Langkah-langkah:
1. Membagi data menjadi data latih dan data uji
2. Melatih model menggunakan data latih
3. Memprediksi hasil dari data uji
4. Menghitung akurasi model

---

## 🚀 Cara Menjalankan

### 1. **Clone Repo** (jika belum)
```bash
git clone https://github.com/Natlane/simple-ai-iris.git
cd simple-ai-iris
