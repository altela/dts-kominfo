from hitung_keramik import *


# Mulai program dengan while repeat
def submenu_keramik():
    from menu_main import main_menu

    while True:
        try:
            print("\n========== Sub Menu Kalkulasi Hitung Material Keramik ==========\n")
            print("Input space yang tersedia")
            panjang_lantai_meter = float(input("Panjang space lantai dalam satuan meter : "))
            lebar_lantai_meter = float(input("Lebar space lantai dalam satuan meter : "))

            print("\nBerapa ukuran keramik yang digunakan?")
            print("1. Ukuran kecil (20 x 20)")
            print("2. Ukuran standar (30 x 30)")
            print("3. Ukuran sedang (40 x 40)")
            print("4. Ukuran besar (45 x 45)")
            print("5. Ukuran ekstra besar (50 x 50)")
            pilihan_keramik = int(input("Masukkan pilihan anda : "))

            gap_semen = float(input("Jarak semen penghubung dalam satuan centimeter : "))
            box_keramik = int(input("Jumlah keramik dalam satu box pembelian : "))
            harga_box = int(input("Harga per box : "))

            hitung_jumlah_keramik(panjang_lantai_meter, lebar_lantai_meter, pilihan_keramik, gap_semen, box_keramik, harga_box)
        except:
            print("\nAnda memasukkan karakter di luar pilihan!")

        cek_status = str(input("Apakah ingin menghitung estimasi keramik lagi? (y/n) : "))
        if cek_status.lower() != "y":
            break
            main_menu()

# Acuan perhitungan didapat dari https://www.omnicalculator.com/construction/tile
