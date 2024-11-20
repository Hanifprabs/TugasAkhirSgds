import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

# Membaca file CSV
df = pd.read_csv('ObesityDataSet.csv')

# Mengubah fitur kategori menjadi numerik dengan LabelEncoder
label_encoders = {}
categorical_columns = ['Gender', 'CAEC', 'CALC', 'FAVC', 'SCC', 'SMOKE', 'MTRANS', 'NObeyesdad']

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Memeriksa apakah ada nilai yang hilang dan menanganinya
df = df.dropna()

# Menyiapkan fitur (X) dan target (y)
X = df.drop('family_history_with_overweight', axis=1)  # Fitur
y = df['family_history_with_overweight']  # Target

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Menstandarisasi kolom numerik pada X_train dan X_test
scaler = StandardScaler()
numeric_columns = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']

X_train[numeric_columns] = scaler.fit_transform(X_train[numeric_columns])
X_test[numeric_columns] = scaler.transform(X_test[numeric_columns])

# Menggunakan LabelEncoder untuk target 'y'
label_encoder_target = LabelEncoder()
y_train = label_encoder_target.fit_transform(y_train)
y_test = label_encoder_target.transform(y_test)

# Melakukan encoding untuk setiap kolom fitur kategori di X_train dan X_test
categorical_columns = ['Gender', 'CAEC', 'CALC', 'FAVC', 'SCC', 'SMOKE', 'MTRANS']

for col in categorical_columns:
    if col in X_train.columns:
        le = label_encoders[col]
        X_train[col] = le.transform(X_train[col])
        X_test[col] = le.transform(X_test[col])

# Melatih model RandomForest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Fungsi untuk prediksi data baru
def predict_new_data(input_data):
    input_df = pd.DataFrame([input_data], columns=X.columns)

    # Encode kolom kategorikal
    for col in categorical_columns:
        if col in input_df.columns:
            le = label_encoders[col]
            if input_df[col].iloc[0] in le.classes_:
                input_df[col] = le.transform(input_df[col])
            else:
                raise ValueError(f"Nilai '{input_df[col].iloc[0]}' di kolom '{col}' tidak valid. Pilih dari {list(le.classes_)}.")

    # Standarisasi kolom numerik
    input_df[numeric_columns] = scaler.transform(input_df[numeric_columns])

    # Prediksi menggunakan model
    prediction = model.predict(input_df)
    predicted_label = label_encoder_target.inverse_transform(prediction)

    return predicted_label[0]

# Contoh input untuk prediksi
input_data = {
    'Age': 25,
    'Gender': 'Female',  # Ganti dengan 'Male' atau 'Female'
    'Height': 160,
    'Weight': 65,
    'FCVC': 3,
    'NCP': 2,
    'CH2O': 2,
    'FAF': 2,
    'TUE': 1,
    'CAEC': 'Sometimes',
    'CALC': 'No',
    'FAVC': 'Yes',
    'SCC': 'Yes',
    'SMOKE': 'No',
    'MTRANS': 'Public_Transportation'
}

try:
    # Prediksi dengan input data pengguna
    predicted_result = predict_new_data(input_data)
    print(f"Hasil Prediksi: {predicted_result}")
except ValueError as e:
    print(f"Error: {e}")
