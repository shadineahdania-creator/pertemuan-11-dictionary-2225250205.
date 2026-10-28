def cari_mahasiswa(data, nim):
    mahasiswa = data.get(nim)
    if mahasiswa:
        print(f"Data {mahasiswa['nama']} ditampilkan: NIM {nim}, Kelas {mahasiswa['kelas']}, Nilai {mahasiswa['nilai']}")
    else:
        print("Data tidak ditemukan")

def rata_rata_nilai(data):
    total = sum(m["nilai"] for m in data.values())
    return total / len(data) if data else 0

# Data Awal Mahasiswa
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# Test Case 1: Cari A003
cari_mahasiswa(data_mahasiswa, "A003")
# Test Case 2: Cari A999
cari_mahasiswa(data_mahasiswa, "A999")
# Test Case 3: Ubah nilai A002 menjadi 82
data_mahasiswa["A002"]["nilai"] = 82
print(f"Nilai A002 (Budi) berhasil diubah menjadi: {data_mahasiswa['A002']['nilai']}")
# Test Case 4: Tambah data mahasiswa baru (A006)
data_mahasiswa["A006"] = {"nama": "Fajar", "kelas": "B", "nilai": 80}
print(f"Key A006 berhasil ditambahkan: {data_mahasiswa['A006']}")
# Test Case 5: Rekap menggunakan items()
print("\n--- Rekap Semua Data Mahasiswa ---")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Nama: {info['nama']} | Kelas: {info['kelas']} | Nilai: {info['nilai']}")

# Tampilkan rata-rata nilai seluruh mahasiswa
print(f"\nRata-rata nilai seluruh kelas: {rata_rata_nilai(data_mahasiswa):.2f}")
