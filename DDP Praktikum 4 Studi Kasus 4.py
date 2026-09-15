# Instruksi Tugas:
# 1. Buat Dictionary buku yang berisi judul, penulis, dan tahun_terbit
data_buku = {
    "judul": "Belajar Pemrograman Python",
    "penulis": "Andi",
    "tahun_terbit": 2022
}

# 2. Gunakan perulangan (while loop) untuk menampilkan menu pengelolaan data.
while True:
    print("\nMENU PENGELOLAAN DATA BUKU")
    print("1. Tampilkan Data Buku")
    print("2. Tambah/Ganti Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Keluar")
    
    pilihan = input("\nPilih menu (1-5): ")
    
    if pilihan == "1":
        # 3. Tampilkan data buku ketika pengguna memilih menu tampilkan data.
        print("\nDATA BUKU SAAT INI")
        print("Judul        :", data_buku["judul"])
        print("Penulis      :", data_buku["penulis"])
        print("Tahun Terbit :", data_buku["tahun_terbit"])
        if "penerbit" in data_buku:
            print("Penerbit     :", data_buku["penerbit"])
            
    elif pilihan == "2":
        # 4. Tambahkan data penerbit ke dalam Dictionary.
        print("\nTAMBAH PENERBIT")
        penerbit_baru = input("Masukkan nama penerbit: ")
        data_buku["penerbit"] = penerbit_baru
        print("Data penerbit berhasil ditambahkan")
        
    elif pilihan == "3":
        # 5. Ubah data penulis pada Dictionary.
        print("\nUBAH PENULIS")
        print("Penulis saat ini:", data_buku["penulis"])
        penulis_baru = input("Masukkan nama penulis baru: ")
        data_buku["penulis"] = penulis_baru
        print("Data penulis berhasil diubah")
        
    elif pilihan == "4":
        # 6. Hapus data penerbit dari Dictionary. (del)
        print("\nHAPUS PENERBIT")
        if "penerbit" in data_buku:
            del data_buku["penerbit"]
            print("Data penerbit berhasil dihapus dari Dictionary")
        else:
            print("Data penerbit belum ada di dalam Dictionary")
            
    elif pilihan == "5":
        # 7. Perulangan terus berjalan sampai pengguna memilih menu keluar.
        print("\nKeluar dari program pengelolaan data buku.")
        break
        
    else:
        print("\nPilihan tidak valid. Silakan masukkan angka 1 sampai 5")

# 8. Tampilkan data buku setelah dilakukan perubahan.
print("\nDATA BUKU SETELAH PERUBAHAN")
print("Judul        :", data_buku["judul"])
print("Penulis      :", data_buku["penulis"])
print("Tahun Terbit :", data_buku["tahun_terbit"])
if "penerbit" in data_buku:
    print("Penerbit     :", data_buku["penerbit"])