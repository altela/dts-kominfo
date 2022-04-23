from hitung_bata import *


# Mulai program dengan while repeat
def submenu_bata():
    from menu_main import main_menu

    while True:
        print("\n========== Sub Menu Kalkulasi Hitung Material Bata ==========\n")
        sama = str(input("Apakah Anda ingin membuat lebih dari satu tembok? (y/n) : "))
        if sama.lower() == "y":
            while True:
                tembok = int(input("Berapa banyak tembok tersebut : "))
                panjang_meter = int(input("Panjang tembok tersebut dalam satuan meter : "))
                tinggi_meter = int(input("Tinggi tembok tersebut dalam satuan meter : "))
                semen = int(input("Ketebalan semen penghubung dalam satuan centimeter : "))
                bahan_tembok = str(input("Bahan tembok nantinya menggunakan bata merah standar (20cm x 5cm) atau batako standar (40cm x 20cm)? (bata/batako) : "))
                harga = int(input("Harga per PCS : "))
                if bahan_tembok.lower() == "bata":
                    hitung_jumlah_bata(tembok, semen, panjang_meter, tinggi_meter, harga)
                    break
                elif bahan_tembok.lower() == "batako":
                    hitung_jumlah_batako(tembok, semen, panjang_meter, tinggi_meter, harga)
                    break
                else:
                    print("Harap masukkan input dengan benar")

            cek_status = str(input("Apakah ingin menghitung estimasi bata/batako lagi? (y/n) : "))
            if cek_status.lower() != "y":
                break
                main_menu()

        elif sama.lower() == "n":
            while True:
                panjang_meter = int(input("Panjang tembok dalam satuan meter : "))
                tinggi_meter = int(input("Tinggi tembok dalam satuan meter : "))
                semen = int(input("Ketebalan semen penghubung dalam satuan centimeter : "))
                bahan_tembok = str(input("Bahan tembok nantinya menggunakan bata atau batako? (bata/batako) : "))
                harga = int(input("Harga per PCS : "))
                if bahan_tembok.lower() == "bata":
                    tembok = 1
                    hitung_jumlah_bata(tembok, semen, panjang_meter, tinggi_meter, harga)
                    break
                elif bahan_tembok.lower() == "batako":
                    tembok = 1
                    hitung_jumlah_batako(tembok, semen, panjang_meter, tinggi_meter, harga)
                    break
                else:
                    print("Harap masukkan input dengan benar")

            cek_status = str(input("Apakah ingin menghitung estimasi bata/batako lagi? (y/n) : "))
            if cek_status.lower() != "y":
                break
                main_menu()
        else:
            print("Harap isi pilihan dengan benar")

# Acuan perhitungan didapat dari https://www.omnicalculator.com/construction/brick
