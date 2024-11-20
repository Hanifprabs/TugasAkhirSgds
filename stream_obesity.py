import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Fungsi untuk memuat model dan preprocessor
def load_model_pickle(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)

# Fungsi untuk melakukan prediksi menggunakan model
# Fungsi untuk melakukan prediksi menggunakan model
# Fungsi untuk melakukan prediksi menggunakan model
def predict(data, model, label_encoders, scaler, target_encoder):
    # Memproses data input
    categorical_cols = ['Gender', 'CALC', 'FAVC', 'SMOKE', 'family_history_with_overweight', 'CAEC', 'MTRANS']
    numerical_cols = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']

    # Mengkodekan kolom kategorikal dengan pengecekan label baru
    for col in categorical_cols:
        try:
            # Transformasikan seluruh kolom, bukan hanya satu nilai
            data[col] = label_encoders[col].transform(data[col])
        except ValueError as e:
            st.warning(f"Warning: Label '{data[col][0]}' pada kolom '{col}' tidak dikenali. Menggunakan label pertama yang valid.")
            # Jika label tidak dikenali, kita akan fallback ke label pertama dalam kelas yang dikenali
            data[col] = label_encoders[col].transform([label_encoders[col].classes_[0]])

    # Menstandarkan kolom numerik
    data[numerical_cols] = scaler.transform(data[numerical_cols])

    # Melakukan prediksi
    prediction = model.predict(data)
    return target_encoder.inverse_transform(prediction)


# UI Streamlit
st.title("Obesity Prediction Model")

# Input untuk pengguna
Age = st.number_input('Age', min_value=18, max_value=100, value=30)
Height = st.number_input('Height (cm)', min_value=100, max_value=250, value=170)
Weight = st.number_input('Weight (kg)', min_value=30, max_value=200, value=70)
FCVC = st.slider('FCVC (Frequency of vegetable consumption)', 1, 5, 3)
NCP = st.slider('NCP (Number of main meals)', 1, 3, 2)
CH2O = st.slider('CH2O (Water consumption)', 1, 5, 3)
FAF = st.slider('FAF (Physical activity frequency)', 1, 5, 3)
TUE = st.slider('TUE (Technology usage time)', 1, 5, 3)
Gender = st.selectbox('Gender', ['Male', 'Female'])
CALC = st.selectbox('CALC (Alcohol consumption)', ['no', 'Sometimes', 'Frequently', 'Always'])  # Pastikan sesuai dengan label saat pelatihan
FAVC = st.selectbox('FAVC (Frequency of high-calorie food consumption)', ['no', 'yes'])
SMOKE = st.selectbox('Smoking', ['no', 'yes'])
family_history_with_overweight = st.selectbox('Family history with overweight', ['yes', 'no'])
CAEC = st.selectbox('CAEC (Eating with family)', ['Sometimes', 'Frequently', 'Always', 'no'])
MTRANS = st.selectbox('MTRANS (Transportation)', ['Public_Transportation', 'Walking', 'Automobile', 'Motorbike', 'Bike'])

# Membuat DataFrame dari input
user_input = pd.DataFrame({
    'Age': [Age],
    'Height': [Height],
    'Weight': [Weight],
    'FCVC': [FCVC],
    'NCP': [NCP],
    'CH2O': [CH2O],
    'FAF': [FAF],
    'TUE': [TUE],
    'Gender': [Gender],
    'CALC': [CALC],
    'FAVC': [FAVC],
    'SMOKE': [SMOKE],
    'family_history_with_overweight': [family_history_with_overweight],
    'CAEC': [CAEC],
    'MTRANS': [MTRANS]
})

# Memuat model yang sudah dilatih
model_data = load_model_pickle('obesity_model.pkl')

model = model_data['model']
label_encoders = model_data['label_encoders']
scaler = model_data['scaler']
target_encoder = model_data['target_encoder']

# Tombol untuk prediksi
if st.button('Predict Obesity Level'):
    prediction = predict(user_input, model, label_encoders, scaler, target_encoder)
    st.write(f"Predicted Obesity Level: {prediction[0]}")
