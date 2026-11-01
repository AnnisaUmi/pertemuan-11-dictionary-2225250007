# ==========================================
# LATIHAN 05 | DICTIONARY BERSARANG
# ==========================================

mahasiswa = {
    "A001": {
        "nama": "Dio",
        "nilai": 88
    },
    "A002": {
        "nama": "Axel",
        "nilai": 76
    },
    "A003": {
        "nama": "Ana",
        "nilai": 95
    }
}

print("=" * 48)
print("             DATA MAHASISWA")
print("=" * 48)

for nim, data in mahasiswa.items():
    print(f"NIM   : {nim}")
    print(f"Nama  : {data['nama']}")
    print(f"Nilai : {data['nilai']}")
    print("-" * 48)