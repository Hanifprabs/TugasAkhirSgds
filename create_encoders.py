import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

# Memuat dataset
dataset = pd.read_csv('path_to_your_dataset.csv')

# Asumsikan dataset memiliki kolom 'Gender', 'CAEC', 'CALC', 'FAVC', 'FamilyHistory', 'MTRANS'
label_encoders = {
    "Gender": LabelEncoder(),
    "CAEC": LabelEncoder(),
    "CALC": LabelEncoder(),
    "FAVC": LabelEncoder(),
    "FamilyHistory": LabelEncoder(),
    "MTRANS": LabelEncoder()
}

# Fit encoder ke dataset
label_encoders["Gender"].fit(dataset['Gender'])
label_encoders["CAEC"].fit(dataset['CAEC'])
label_encoders["CALC"].fit(dataset['CALC'])
label_encoders["FAVC"].fit(dataset['FAVC'])
label_encoders["FamilyHistory"].fit(dataset['FamilyHistory'])
label_encoders["MTRANS"].fit(dataset['MTRANS'])

# Simpan encoder menggunakan pickle
with open('gender_encoder.pkl', 'wb') as file:
    pickle.dump(label_encoders["Gender"], file)

with open('caec_encoder.pkl', 'wb') as file:
    pickle.dump(label_encoders["CAEC"], file)

with open('calc_encoder.pkl', 'wb') as file:
    pickle.dump(label_encoders["CALC"], file)

with open('favc_encoder.pkl', 'wb') as file:
    pickle.dump(label_encoders["FAVC"], file)

with open('familyhistory_encoder.pkl', 'wb') as file:
    pickle.dump(label_encoders["FamilyHistory"], file)

with open('mtrans_encoder.pkl', 'wb') as file:
    pickle.dump(label_encoders["MTRANS"], file)
