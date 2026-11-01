# ==========================================
# LATIHAN 06 | FUNGSI DICTIONARY
# ==========================================

def hitung_rata_rata(data_nilai):
    if not data_nilai:
        return 0

    return sum(data_nilai.values()) / len(data_nilai)


nilai_mahasiswa = {
    "A001": 85,
    "A002": 90,
    "A003": 78,
    "A004": 92
}

rata_rata = hitung_rata_rata(nilai_mahasiswa)

print("=" * 42)
print("          STATISTIK NILAI")
print("=" * 42)
print(f"Jumlah mahasiswa : {len(nilai_mahasiswa)}")
print(f"Rata-rata nilai  : {rata_rata:.2f}")
print("=" * 42)