# ==========================================
# LATIHAN 02 | AKSES DATA
# ==========================================

nilai_mahasiswa = {
    "A001": 85,
    "A002": 90,
    "A003": 78,
    "A004": 92
}

print("=" * 42)
print("          PENCARIAN NILAI")
print("=" * 42)

nim = input("Masukkan NIM: ").strip().upper()

if nim in nilai_mahasiswa:
    print(f"Nilai mahasiswa: {nilai_mahasiswa[nim]}")
else:
    print("Data mahasiswa tidak ditemukan.")

print("=" * 42)