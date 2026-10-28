
data = {
    "nim": "A001",
    "nama": "Ayu",
    "nilai": 85
}

print(data["nim"])
print(data["nama"])
print(data["nilai"])

# 4. Tambah, Ubah, dan Hapus data
data["jurusan"] = "Informatika"  # Menambah key baru
data["nilai"] = 95               # Mengubah nilai yang ada
del data["nim"]                  # Menghapus key "nim"

# 5. Uji key yang tidak ada (Pakai .get agar tidak error)
print(data.get("alamat", "Key tidak ditemukan!"))