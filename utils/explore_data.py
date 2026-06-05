import pandas as pd

df = pd.read_csv('../data/formasi_cpns_2024.csv')  # sesuaikan nama file

print("=== INFO DATASET ===")
print(f"Jumlah baris: {len(df)}")
print(f"Jumlah kolom: {len(df.columns)}")
print(f"\nNama kolom:")
print(df.columns.tolist())
print(f"\nContoh 3 baris pertama:")
print(df.head(3))
print(f"\nCek missing values:")
print(df.isnull().sum())

print("\n=== CEK NILAI UNIK ===")
print(f"\nTingkat pendidikan unik:")
print(df['nama'].value_counts().head(15))

print(f"\nFormasi tipe unik:")
print(df['formasi_nm'].value_counts())

print(f"\nContoh nilai cepat_kode (kemungkinan kode jurusan):")
print(df['cepat_kode'].value_counts().head(10))

print(f"\nContoh jabatan_nm unik (10 pertama):")
print(df['jabatan_nm'].value_counts().head(10))

print(f"\nRange jumlah_formasi:")
print(df['jumlah_formasi'].describe())