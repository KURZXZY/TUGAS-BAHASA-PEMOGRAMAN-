'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# Variabel Global untuk Menyimpan Data
mahasiswa = []
barang = []
transaksi = []

# Fungsi Data Mahasiswa

def InputMahasiswa():
    global mahasiswa
    while True:
        nama = input("\nmasukkan nama atau ketik 'stop' untuk berhenti: ")
        if nama.lower() == 'stop':
            break
        nim = input("NIM: ")
        prodi = input("PRODI: ")
        nilai = float(input("NILAI: "))
        mahasiswa.append([nama, nim, prodi, nilai])

def TampilkanMahasiswa():
    global mahasiswa
    if not mahasiswa:
        print("tidak ada mahasiswa dalam database")
    else:
        for mhs in mahasiswa:
            print(f"nama: {mhs[0]}, NIM: {mhs[1]}, PRODI: {mhs[2]}, NILAI: {mhs[3]}")

def HitungStatistikMahasiswa():
    global mahasiswa
    if not mahasiswa:
        print("tidak ada mahasiswa dalam database")
        return
    TotalNilai = sum(mhs[3] for mhs in mahasiswa)
    RataRataNilai = TotalNilai / len(mahasiswa)
    NilaiTertinggi = max(mhs[3] for mhs in mahasiswa)
    NilaiTerendah = min(mhs[3] for mhs in mahasiswa)
    print(f"rata-rata Nilai: {RataRataNilai:.2f}")
    print(f"nilai tertinggi: {NilaiTertinggi}")
    print(f"nilai terendah: {NilaiTerendah}")

def CariMahasiswaDenganNilaiEkstrem():
    global mahasiswa
    if not mahasiswa:
        print("tidak ada mahasiswa dalam database")
        return
    NilaiTertinggi = max(mhs[3] for mhs in mahasiswa)
    NilaiTerendah = min(mhs[3] for mhs in mahasiswa)
    print("mahasiswa dengan nilai tertinggi:")
    for mhs in mahasiswa:
        if mhs[3] == NilaiTertinggi:
            print(f"Nama: {mhs[0]}, NIM: {mhs[1]}, Prodi: {mhs[2]}, Nilai: {mhs[3]}")
    print("mahasiswa dengan nilai terendah:")
    for mhs in mahasiswa:
        if mhs[3] == NilaiTerendah:
            print(f"Nama: {mhs[0]}, NIM: {mhs[1]}, PRODI: {mhs[2]}, NILAI: {mhs[3]}")

def MenuMahasiswa():
    while True:
        print("\nmenu data mahasiswa")
        print("1. input data mahasiswa")
        print("2. tampilkan semua mahasiswa")
        print("3. hitung statistik nilai")
        print("4. cari mahasiswa dengan nilai ekstrem")
        print("5. kembali ke menu utama")
        pilihan = input("pilih opsi: ")
        
        if pilihan == '1':
            InputMahasiswa()
        elif pilihan == '2':
            TampilkanMahasiswa()
        elif pilihan == '3':
            HitungStatistikMahasiswa()
        elif pilihan == '4':
            CariMahasiswaDenganNilaiEkstrem()
        elif pilihan == '5':
            break
        else:
            print("pilihan tidak valid coba lagi")

# Fungsi  Inventaris Barang

def InputBarang():
    global barang
    while True:
        nama = input("\nmasukkan nama barang atau ketik 'stop' untuk berhenti: ")
        if nama.lower() == 'stop':
            break
        kode = input("masukkan kode barang: ")
        jumlah = int(input("masukkan jumlah barang: "))
        barang.append([nama, kode, jumlah])

def TampilkanBarang():
    global barang
    if not barang:
        print("tidak ada barang dalam Inventaris")
    else:
        for item in barang:
            print(f"nama barang: {item[0]}, kode barang: {item[1]}, jumlah barang: {item[2]}")

def CariBarang(kode):
    global barang
    for item in barang:
        if item[1] == kode:
            print(f"nama barang: {item[0]}, kode barang: {item[1]}, jumlah barang: {item[2]}")
            return
    print("barang tidak ditemukan")

def HapusBarang(kode):
    global barang
    for item in barang:
        if item[1] == kode:
            barang.remove(item)
            print(f"barang dengan kode {kode} telah dihapus")
            return
    print("barang tidak ditemukan")

def MenuBarang():
    while True:
        print("\nmenu inventaris barang")
        print("1. input data barang")
        print("2. tampilkan semua barang")
        print("3. cari barang berdasarkan kode")
        print("4. hapus barang berdasarkan kode")
        print("5. kembali ke menu utama")
        pilihan = input("pilih opsi: ")
        
        if pilihan == '1':
            InputBarang()
        elif pilihan == '2':
            TampilkanBarang()
        elif pilihan == '3':
            KodeCari = input("masukkan kode barang yang ingin dicari: ")
            CariBarang(KodeCari)
        elif pilihan == '4':
            KodeHapus = input("masukkan kode barang yang ingin dihapus: ")
            HapusBarang(KodeHapus)
        elif pilihan == '5':
            break
        else:
            print("pilihan tidak valid Coba lagi")

# Fungsi Pengelolaan Keuangan Pribadi

def InputTransaksi():
    global transaksi
    while True:
        jenis = input("\nmasukkan jenis transaksi (pemasukan/pengeluaran) atau ketik 'stop' untuk berhenti: ")
        if jenis.lower() == 'stop':
            break
        if jenis.lower() not in ['pemasukan', 'pengeluaran']:
            print("jenis transaksi tidak valid masukkan 'pemasukan' atau 'pengeluaran'")
            continue
        deskripsi = input("masukkan deskripsi transaksi: ")
        jumlah = float(input("masukkan jumlah: "))
        transaksi.append([jenis, deskripsi, jumlah])

def TampilkanTransaksi():
    global transaksi
    if not transaksi:
        print("tidak ada transaksi yang tercatat")
    else:
        for tr in transaksi:
            print(f"jenis: {tr[0]}, deskripsi: {tr[1]}, jumlah: {tr[2]}")

def TotalPemasukan():
    global transaksi
    total = sum(tr[2] for tr in transaksi if tr[0] == 'pemasukan')
    print(f"total pemasukan: {total}")
    return total

def TotalPengeluaran():
    global transaksi
    total = sum(tr[2] for tr in transaksi if tr[0] == 'pengeluaran')
    print(f"total pengeluaran: {total}")
    return total

def SaldoAkhir():
    global transaksi
    pemasukan = TotalPemasukan()
    pengeluaran = TotalPengeluaran()
    saldo = pemasukan - pengeluaran
    print(f"saldo akhir: {saldo}")
    return saldo

def MenuKeuangan():
    while True:
        print("\nmenu pengelolaan keuangan pribadi")
        print("1. input transaksi")
        print("2. tampilkan semua transaksi")
        print("3. hitung total pemasukan")
        print("4. hitung total pengeluaran")
        print("5. hitung saldo akhir")
        print("6. kembali ke menu utama")
        pilihan = input("pilih opsi: ")
        
        if pilihan == '1':
            InputTransaksi()
        elif pilihan == '2':
            TampilkanTransaksi()
        elif pilihan == '3':
            TotalPemasukan()
        elif pilihan == '4':
            TotalPengeluaran()
        elif pilihan == '5':
            SaldoAkhir()
        elif pilihan == '6':
            break
        else:
            print("pilihan tidak valid coba lagi")

# Menu Utama
def MenuUhuy():
    while True:
        print("NAMA: KURNIAWAN")
        print("NIM: 20230801054")
        print("\nmenu utama")
        print("1. data mahasiswa")
        print("2. inventaris barang")
        print("3. pengelolaan keuangan pribadi")
        print("4. keluar")
        pilihan = input("pilih opsi: ")
        
        if pilihan == '1':
            MenuMahasiswa()
        elif pilihan == '2':
            MenuBarang()
        elif pilihan == '3':
            MenuKeuangan()
        elif pilihan == '4':
            print("terima kasih telah menggunakan program ini")
            break
        else:
            print("pilihan tidak valid coba lagi")

# Jalankan Menu Utama
MenuUhuy()
