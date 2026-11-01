# ==========================================
# LATIHAN 04 | ITERASI DICTIONARY
# ==========================================

nilai = {
    "A001": 85,
    "A002": 90,
    "A003": 78,
    "A004": 92,
    "A005": 88
}

print("=" * 42)
print("          REKAP NILAI")
print("=" * 42)

for nim, skor in nilai.items():
    status = "Lulus" if skor >= 75 else "Belum lulus"
    print(f"{nim} | Nilai: {skor} | {status}")

print("=" * 42)