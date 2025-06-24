#Nama:Aliswandani Nashifa S.P
#NIM: K3524022

from abc import ABC, abstractmethod
# Class Parent
class ProduksiRoti(ABC):
    def __init__(self, nama, kode, bahan_baku, biaya_produksi, harga_jual, jumlah_pcs):
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual
        self.jumlah_pcs = jumlah_pcs
    def hitung_profit_per_produksi(self):
        total_penjualan = self.harga_jual * self.jumlah_pcs
        return total_penjualan - self.biaya_produksi
    def estimasi_profit(self, jumlah_produksi):
        satu_kali_produksi = jumlah_produksi / self.jumlah_pcs
        total_biaya = self.biaya_produksi * satu_kali_produksi
        total_penjualan = self.harga_jual * jumlah_produksi
        profit = total_penjualan - total_biaya
        return {
            "jumlah_produksi": jumlah_produksi,
            "batch_diperlukan": satu_kali_produksi,
            "total_biaya_produksi": total_biaya,
            "total_penjualan": total_penjualan,
            "estimasi_profit": profit }
    def tampilkan_info(self):
        print("========================================")
        print("Nama Produk:", self.nama)
        print("Kode Produk:", self.kode)
        print("Jumlah per produksi:", self.jumlah_pcs, "pcs")
        print("Biaya Produksi: Rp", self.biaya_produksi, "per produksi")
        print("Harga Jual: Rp", self.harga_jual, "per pcs")
        print("Profit per produksi: Rp", self.hitung_profit_per_produksi())
        print()
        print("Bahan Baku:")
        for bahan, jumlah in self.bahan_baku.items():
            print(bahan, ":", jumlah, "gram")
        print("========================================")
    @abstractmethod
    def jenis_roti(self):
        pass
# Interface 
class ProsesProduksi(ABC):
    @abstractmethod
    def pengadonan(self):
        pass
    @abstractmethod
    def pemanggangan(self):
        pass
    def pengembangan(self):
        return None
    def topping(self):
        return None
# Class untuk Roti Manis
class RotiManis(ProduksiRoti, ProsesProduksi):
    def __init__(self):
        bahan_baku = {
            "Tepung Terigu": 270,
            "Gula Halus": 50,
            "Telur": 52,
            "Butter": 45,
            "Ragi Instan": 5,
            "Susu Cair": 120,
            "Garam": 1.5,
            "Susu Bubuk": 10 }
        super().__init__(
            nama="Roti Manis",
            kode="RM001",
            bahan_baku=bahan_baku,
            biaya_produksi=25000,
            harga_jual=3500,
            jumlah_pcs=12 )
    def jenis_roti(self):
        return "Roti Manis"
    def pengadonan(self):
        return "Campur tepung, gula, ragi, dan bahan kering lainnya. Tambahkan telur, susu, dan Butter. Uleni hingga kalis elastis selama 15 menit."
    def pengembangan(self):
        return "Diamkan adonan selama 1 jam hingga mengembang 2 kali lipat. Kemudian bentuk adonan dan diamkan lagi 30 menit."
    def pemanggangan(self):
        return "Panggang dalam oven 180 derajat Celsius selama 20-25 menit hingga berwarna kecoklatan."
class Croissant(ProduksiRoti, ProsesProduksi):
    def __init__(self):
        bahan_baku = {
            "Tepung Terigu": 500,
            "Mentega": 45,
            "Gula Pasir": 50,
            "Ragi Instan": 8,
            "Susu Cair": 120,
            "Telur": 1,
            "Air": 120,
            "Garam": 5 }
        super().__init__(
            nama="Croissant",
            kode="CR001",
            bahan_baku=bahan_baku,
            biaya_produksi=35000,
            harga_jual=8000,
            jumlah_pcs=8 )
    def jenis_roti(self):
        return "Croissant"
    def pengadonan(self):
        return "Buat adonan dasar dengan mencampurkan semua bahan. Uleni hingga halus. Lakukan teknik laminating dengan mentega dingin."
    def pengembangan(self):
        return "Proses fermentasi dan laminating berlapis. Lipat adonan 3 kali dengan jeda istirahat 30 menit di kulkas."
    def pemanggangan(self):
        return "Panggang dalam oven 200 derajat Celsius selama 15-20 menit. Turunkan suhu menjadi 180 derajat dan panggang 10 menit lagi."
class KueKering(ProsesProduksi, ProduksiRoti):
    def __init__(self, nama, kode, bahan_baku, biaya_produksi, harga_jual, jumlah_pcs):
        super().__init__(nama, kode, bahan_baku, biaya_produksi, harga_jual, jumlah_pcs)
    def jenis_roti(self):
        return "Kue Kering"
    def topping(self):
        return "Berikan topping sesuai jenis kue seperti glazing, gula halus, atau dekorasi lainnya."
class ButterCookies(KueKering):
    def __init__(self):
        bahan_baku = {
            "Tepung Terigu": 500,
            "Butter": 350,
            "Gula Halus": 300,
            "Kuning Telur": 34,
            "Tepung Maizena": 100 }
        super().__init__(
            nama="Butter Cookies",
            kode="BC001",
            bahan_baku=bahan_baku,
            biaya_produksi=20000,
            harga_jual=1500,
            jumlah_pcs=24 )
    def pengadonan(self):
        return "Kocok butter dan gula halus hingga pucat. Masukkan kuning telur. Tambahkan tepung sedikit demi sedikit."
    def pemanggangan(self):
        return "Panggang dalam oven 160 derajat Celsius selama 12-15 menit hingga tepi sedikit kecoklatan."
class Muffin(KueKering):
    def __init__(self):
        bahan_baku = {
            "Tepung Beras": 90,
            "Gula Pasir": 60,
            "Garam": 2,
            "Telur": 100,
            "Minyak Goreng": 28,
            "Susu": 120,
            "Baking Powder": 2,
            "Fiber Creme": 30,
            "Keju Oles": 80,
            "Vanili Bubuk": 0.5 }
        super().__init__(
            nama="Muffin Keju",
            kode="MF001",
            bahan_baku=bahan_baku,
            biaya_produksi=18000,
            harga_jual=4000,
            jumlah_pcs=12 )
    def pengadonan(self):
        return "Campur bahan kering dalam satu wadah. Campur bahan basah di wadah lain. Gabungkan dengan adukan minimal."
    def pengembangan(self):
        return "Diamkan adonan selama 10 menit agar baking powder bekerja dan menghasilkan tekstur yang lembut."
    def pemanggangan(self):
        return "Panggang dalam oven 180 derajat Celsius selama 18-22 menit hingga matang."