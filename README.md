# Pertemuan 11 - Dictionary/Map

**Nama:** Shadine Ahdania Sofyan  
**NIM:** 2225250205
**Kelas:** 3B

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value pada Python. Praktikum ini bertujuan memahami cara membuat, mengakses, memanipulasi, dan melakukan iterasi dictionary, termasuk dictionary bersarang serta penggunaan fungsi untuk mengolah data mahasiswa.

## Struktur Folder

```text
pertemuan-11-dictionary-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_dictionary.py
│   ├── 02_akses_get.py
│   ├── 03_manipulasi_dictionary.py
│   ├── 04_iterasi_dictionary.py
│   ├── 05_dictionary_bersarang.py
│   └── 06_fungsi_dictionary.py
└── praktik/
    └── data_mahasiswa.py
```

## Struktur Data

Program pada `praktik/data_mahasiswa.py` menggunakan dictionary bernama `data_mahasiswa` untuk menyimpan data mahasiswa.

Struktur data menggunakan konsep key-value sebagai berikut:

- **Key utama:** NIM mahasiswa, seperti `"A001"`, `"A002"`, dan `"A003"`.
- **Value:** Dictionary bersarang yang berisi informasi mahasiswa.
- **Atribut:** `nama`, `kelas`, dan `nilai`.

Contoh:

```python
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}
```

Program menyediakan dua fungsi utama:

1. `cari_mahasiswa(data, nim)` untuk mencari dan menampilkan data berdasarkan NIM.
2. `rata_rata_nilai(data)` untuk menghitung rata-rata nilai seluruh mahasiswa.

Operasi lainnya mencakup penambahan mahasiswa baru, pembaruan nilai, dan penampilan seluruh data menggunakan `items()`.

## Cara Menjalankan

Pastikan Python 3 sudah terpasang. Buka terminal pada folder utama `pertemuan-11-dictionary-NIM/`.

Jalankan program praktik dengan perintah:

```bash
python3 praktik/data_mahasiswa.py
```

Jika menggunakan Windows dan perintah `python3` tidak tersedia, gunakan:

```bash
python praktik/data_mahasiswa.py
```

Untuk menjalankan latihan satu per satu, gunakan contoh berikut:

```bash
python3 latihan/01_dasar_dictionary.py
python3 latihan/02_akses_get.py
python3 latihan/03_manipulasi_dictionary.py
python3 latihan/04_iterasi_dictionary.py
python3 latihan/05_dictionary_bersarang.py
python3 latihan/06_fungsi_dictionary.py
```

## Test Case

Pengujian dilakukan pada file `praktik/data_mahasiswa.py`.

| No. | Kasus | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Pencarian tersedia | NIM `A003` | Data Citra ditampilkan | Data Citra ditampilkan | Berhasil |
| 2 | Pencarian tidak tersedia | NIM `A999` | Pesan `Data tidak ditemukan` | Pesan data tidak ditemukan tanpa `KeyError` | Berhasil |
| 3 | Pembaruan nilai | NIM `A002` menjadi 82 | Nilai A002 berubah menjadi 82 | Nilai A002 menjadi 82 | Berhasil |
| 4 | Penambahan data | Tambahkan NIM `A006` | Key `A006` tersedia | Key `A006` tersedia setelah ditambahkan | Berhasil |
| 5 | Rekap data | Gunakan `items()` | Semua NIM dan data mahasiswa tampil | Enam mahasiswa ditampilkan | Berhasil |
| 6 | Rata-rata nilai | Hitung nilai seluruh mahasiswa | Rata-rata dihitung dengan benar | Rata-rata 83,50 jika nilai A002 sudah 82 dan A006 bernilai 80 | Berhasil |

*Catatan: Hasil aktual dan status perlu dicocokkan dengan output program yang benar-benar dijalankan.*

## Refleksi

Kesalahan yang dapat terjadi saat menggunakan dictionary adalah mengakses key yang tidak tersedia. Misalnya, pencarian NIM `A999` dapat menimbulkan `KeyError` jika program langsung mengakses `data[nim]` tanpa memeriksa keberadaan key tersebut.

Cara memperbaikinya adalah menggunakan operator `in` sebelum mengakses data.

```python
def cari_mahasiswa(data, nim):
    if nim in data:
        print(data[nim])
    else:
        print("Data tidak ditemukan")
```

Dengan cara ini, program dapat menangani NIM yang tidak terdaftar tanpa mengalami `KeyError`.

Melalui praktikum ini, saya memahami bahwa dictionary menyimpan data dalam bentuk pasangan key-value. Saya juga mempelajari penggunaan key untuk mencari data, assignment untuk menambah dan memperbarui data, serta `items()` untuk menampilkan seluruh pasangan NIM dan data mahasiswa.

## Kesimpulan

Dictionary dapat digunakan untuk mengelola data mahasiswa secara terstruktur dengan NIM sebagai key utama dan informasi mahasiswa sebagai value. Penggunaan fungsi, pemeriksaan key, penambahan data, pembaruan nilai, iterasi `items()`, dan perhitungan rata-rata membantu menghasilkan program yang lebih terorganisasi dan aman dari kesalahan akses key.
