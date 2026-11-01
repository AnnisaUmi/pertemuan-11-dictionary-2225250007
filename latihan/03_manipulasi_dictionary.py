# ==========================================
# LATIHAN 03 | MANIPULASI DICTIONARY
# ==========================================

inventaris = {
    "Buku": 15,
    "Pensil": 25,
    "Penghapus": 12
}

print("DATA INVENTARIS AWAL")
print(inventaris)

inventaris["Pulpen"] = 20
inventaris["Buku"] = 18
inventaris.pop("Penghapus", None)

print("\nDATA INVENTARIS TERBARU")
for barang, jumlah in inventaris.items():
    print(f"{barang:<15}: {jumlah}")

print("=" * 42)