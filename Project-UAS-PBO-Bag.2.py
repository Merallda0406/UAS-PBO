#Nama : Winda Luthfi Itsnaini
#NIM : K3524016

#fitur sistem toko roti hanari
class SistemTokoHanari:
    def __init__(self):
        self.produk_list = []
        self.init_produk_default()
    def init_produk_default(self):
        self.produk_list = [
            RotiManis(),
            Croissant(),
            ButterCookies(),
            Muffin() ]
    def tambah_produk(self):
        kode = input("Masukkan kode: ")
        nama = input("Masukkan nama: (rotimanis/croissant/buttercookies/muffin): ")
        if nama == "rotimanis":
            produk = RotiManis()
        elif nama == "croissant":
            produk = Croissant()
        elif nama == "buttercookies":
            produk = ButterCookies()
        elif nama == "muffin":
            produk = Muffin()
        else:
            print("Jenis anggota tidak ada dalam daftar")
            return
        produk.kode = kode
        produk.nama = nama
        self.produk_list.append(produk)
        print(f"Produk {nama} berhasil ditambahkan!")
    def tampilkan_semua_produk(self):
        if len(self.produk_list) == 0:
            print("Tidak ada produk yang tersedia.")
            return
#menu sistem toko roti hanari
print("========================================")
print("       DAFTAR PRODUK HANARI BAKERY")
print("========================================")
for i in range(len(self.produk_list)):
            produk = self.produk_list[i]
        print(f"{produk.nama} ({produk.kode})")
        print("Jenis Roti:", produk.jenis_roti())
        print("Harga: Rp", produk.harga_jual, "/pcs")
            profit_per_pcs = produk.hitung_profit_per_produksi() / produk.jumlah_pcs
        print("Profit per pcs: Rp", int(profit_per_pcs))
        print("Profit per Produksi: Rp", produk.hitung_profit_per_produksi())
        print("Jumlah Produk per Produksi: ", produk.jumlah_pcs, "/pcs")
        print("----------------------------------------")
        print("========================================")
        print("          HANARI BAKERY")
        print("========================================")
        print("1. Tambah Produk")
        print("2. Tampilkan Semua Produk")
        print("3. Detail Produk")
        print("4. Kalkulator Estimasi Profit")
        print("5. Simulasi Proses Produksi")
        print("6. Keluar")
        print("========================================")
pilihan = input("Pilih menu : ")
    if pilihan == '1':
        self.tambah_produk()
    elif pilihan == '2':
        self.tampilkan_semua_produk()
    elif pilihan == '3':
        self.tampilkan_detail_produk()
    elif pilihan == '4':
        self.kalkulator_profit()
    elif pilihan == '5':
        self.simulasi_produksi()
    elif pilihan == '6':
        print("\nTerima kasih telah menggunakan Sistem Hanari Bakery!")
        break
    else:
        print("Pilihan tidak valid! Pilih antara 1-5.")
