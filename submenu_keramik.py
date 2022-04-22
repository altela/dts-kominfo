from material_keramik import *

# Mulai program dengan while repeat
def submenu_keramik():
    from main_menu import main_menu
    running = True
    while running:
        print("\n========== Sub Menu Kalkulasi Hitung Material Keramik ==========\n")
        print("Input space yang tersedia")
        panjang_lantai_meter = int(input("Panjang space lantai dalam satuan meter : "))
        lebar_lantai_meter = int(input("Lebar space lantai dalam satuan meter : "))

        print("\nMasukkan informasi keramik")
        panjang_keramik = int(input("Panjang keramik dalam satuan centimeter : "))
        lebar_keramik = int(input("Lebar keramik dalam satuan centimeter : "))

        gap_semen = int(input("Jarak semen penghubung dalam satuan centimeter : "))
        hitung_jumlah_keramik(panjang_lantai_meter, lebar_lantai_meter, panjang_keramik, lebar_keramik, gap_semen)

        cek_status = str(input("Apakah ingin menghitung material bata lagi? (y/n) : "))
        if cek_status.lower() != "y":
            main_menu()

# Acuan perhitungan didapat dari https://www.omnicalculator.com/construction/tile
