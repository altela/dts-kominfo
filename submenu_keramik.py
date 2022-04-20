from material_bata import *
from main_menu import *

# Mulai program dengan while repeat
def submenu_keramik():
    running = True
    while running:
        print("\n========== Sub Menu Kalkulasi Hitung Material Keramik ==========")
        sama = str(input("Apakah Anda ingin membuat lebih dari satu tembok? (y/n) : "))
        if sama.lower() == "y":
            while True:
                tembok = int(input("Berapa banyak tembok tersebut : "))
                panjang_meter = int(input("Panjang tembok tersebut dalam satuan meter : "))
                tinggi_meter = int(input("Tinggi tembok tersebut dalam satuan meter : "))
                semen = int(input("Ketebalan semen penghubung dalam satuan centimeter : "))
                bahan_tembok = str(input("Bahan tembok nantinya menggunakan bata atau batako? (bata/batako) : "))
                if bahan_tembok.lower() == "bata":
                    hitung_jumlah_bata(tembok, semen, panjang_meter, tinggi_meter)
                    break
                elif bahan_tembok.lower() == "batako":
                    hitung_jumlah_batako(tembok, semen, panjang_meter, tinggi_meter)
                    break
                else:
                    print("Harap masukkan input dengan benar")

            cek_status = str(input("Apakah ingin menghitung material bata lagi? (y/n) : "))
            if cek_status.lower() != "y":
                main_menu()

        elif sama.lower() == "n":
            while True:
                panjang_meter = int(input("Panjang tembok dalam satuan meter : "))
                tinggi_meter = int(input("Tinggi tembok dalam satuan meter : "))
                semen = int(input("Ketebalan semen penghubung dalam satuan centimeter : "))
                bahan_tembok = str(input("Bahan tembok nantinya menggunakan bata atau batako? (bata/batako) : "))
                if bahan_tembok.lower() == "bata":
                    tembok = 1
                    hitung_jumlah_bata(tembok, semen, panjang_meter, tinggi_meter)
                    break
                elif bahan_tembok.lower() == "batako":
                    tembok = 1
                    hitung_jumlah_batako(tembok, semen, panjang_meter, tinggi_meter)
                    break
                else:
                    print("Harap masukkan input dengan benar")

            cek_status = str(input("Apakah ingin menghitung material bata lagi? (y/n) : "))
            if cek_status.lower() != "y":
                main_menu()
        else:
            print("Harap isi pilihan dengan benar")

# Acuan perhitungan didapat dari https://www.omnicalculator.com/construction/brick
