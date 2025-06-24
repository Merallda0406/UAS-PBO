#Nama   : Merallda Prisca Daniza
#NIM    : K3524014

# Fitur
class SistemTokoHanari:
    
    def kalkulator_profit(self):
        if len(self.produk_list) == 0:
            print("Tidak ada produk yang tersedia.")
            return
        print("========================================")
        print("        KALKULATOR ESTIMASI PROFIT")
        print("========================================")
        print("Pilih jenis produk:")
        for i in range(len(self.produk_list)):
            print(str(i+1) + ". " + self.produk_list[i].nama)
        try:
            pilihan = int(input("\nMasukkan pilihan : ")) - 1
            if pilihan >= 0 and pilihan < len(self.produk_list):
                produk = self.produk_list[pilihan]
                jumlah = int(input("Masukkan jumlah pcs yang akan diproduksi: "))
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0!")
                    return
                estimasi = produk.estimasi_profit(jumlah)
                print("========================================")
                print("       ESTIMASI PROFIT -", produk.nama.upper())
                print("========================================")
                print("Jumlah Produksi      :", int(estimasi['jumlah_produksi']), "pcs")
                print("Total Biaya Produksi : Rp", int(estimasi['total_biaya_produksi']))
                print("Total Penjualan      : Rp", int(estimasi['total_penjualan']))
                print("Estimasi Profit      : Rp", int(estimasi['estimasi_profit']))
                print("========================================")  
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
    def simulasi_produksi(self):
        if len(self.produk_list) == 0:
            print("Tidak ada produk yang tersedia.")
            return
        print("========================================")
        print("        SIMULASI PROSES PRODUKSI")
        print("========================================")
        print("Pilih produk untuk simulasi:")
        for i in range(len(self.produk_list)):
            print(str(i+1) + ". " + self.produk_list[i].nama)
        try:
            pilihan = int(input("\nMasukkan pilihan : ")) - 1
            if pilihan >= 0 and pilihan < len(self.produk_list):
                produk = self.produk_list[pilihan]
                print("========================================")
                print("    SIMULASI PRODUKSI:", produk.nama.upper())
                print("========================================")
                print("\nTAHAP 1: PENGADONAN")
                print(produk.pengadonan())
                if produk.pengembangan() is not None:
                    print("\nTAHAP 2: PENGEMBANGAN")
                    print(produk.pengembangan())
                print("\nTAHAP 3: PEMANGGANGAN")
                print(produk.pemanggangan())
                if produk.topping() is not None:
                    print("\nTAHAP 4: TOPPING")
                    print(produk.topping())
                print("\nPRODUKSI SELESAI!")
                print("Hasil:", produk.jumlah_pcs, "pcs", produk.nama)
                print("========================================")
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
    def tampilkan_detail_produk(self):
        if len(self.produk_list) == 0:
            print("Tidak ada produk yang tersedia.")
            return
        print("\nPilih produk untuk melihat detail:")
        for i in range(len(self.produk_list)):
            print(str(i+1) + ". " + self.produk_list[i].nama)
        try:
            pilihan = int(input("\nMasukkan pilihan : ")) - 1
            if pilihan >= 0 and pilihan < len(self.produk_list):
                produk = self.produk_list[pilihan]
                produk.tampilkan_info()
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
    
# Program 
def main():
    print("Selamat datang di Hanari Bakery!")
    sistem_toko = SistemTokoHanari()
    sistem_toko.run()
if __name__ == "__main__":
    main()