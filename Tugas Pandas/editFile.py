import pandas as pd

data = {
    'Nama': ['Andi', 'Budi', 'Cici'],
    'Umur': [21, 22, 20],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya']
}
df = pd.DataFrame(data)

# Menyaring data untuk menampilkan baris dengan Umur > 20
filtered_df = df[df['Umur'] > 20]
print(filtered_df)

# Menambahkan kolom baru
df['Pekerjaan'] = ['Dokter', 'Insinyur', 'Guru']
print(df)
