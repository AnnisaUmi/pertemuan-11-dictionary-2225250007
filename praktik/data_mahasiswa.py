# ==========================================
# PRAKTIK | PENGELOLAAN DATA MAHASISWA
# ==========================================

def tampilkan_data(data):
    print("\n" + "=" * 48)
    print("             DATA MAHASISWA")
    print("=" * 48)

    for nim, mahasiswa in data.items():
        print(f"NIM   : {nim}")
        print(f"Nama  : {mahasiswa['nama']}")
        print(f"Nilai : {mahasiswa['nilai']}")
        print("-" * 48)


def hitung_rata_rata(data):
    if not data:
        return 0

    total = sum(m["nilai"] for m in data.values())
    return total / len(data)


def main():
    mahasiswa = {
        "A001": {"nama": "Dio", "nilai": 85},
        "A002": {"nama": "Ana", "nilai": 90},
        "A003": {"nama": "Axel", "nilai": 78},
        "A004": {"nama": "Dina", "nilai": 92}
    }

    tampilkan_data(mahasiswa)

    print(f"Jumlah mahasiswa : {len(mahasiswa)}")
    print(f"Rata-rata nilai  : {hitung_rata_rata(mahasiswa):.2f}")


if __name__ == "__main__":
    main()