# ==========================================
# LATIHAN 01 | DASAR DICTIONARY
# ==========================================

mahasiswa = {
    "nama": "Annisa Umi Solihat",
    "nim": "2225250007",
    "kelas": "3F",
    "nilai": 80
}

print("=" * 42)
print("          DATA MAHASISWA")
print("=" * 42)

for key, value in mahasiswa.items():
    print(f"{key.capitalize():<12}: {value}")

print("=" * 42)