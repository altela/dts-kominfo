from menu_sub_bata import submenu_bata
from menu_sub_keramik import submenu_keramik


def main_menu():
    while True:
        print("\n========== Selamat Datang Di Program Hitung Material ==========\n")
        print("Silahkan pilih kalkulasi yang anda perlukan :\n")
        print("1. Menghitung kebutuhan material bata atau batako")
        print("2. Menghitung kebutuhan material keramik lantai")
        print("0. Exit Program")
        pilih_material = int(input("\nHarap masukkan pilihan anda : "))
        if pilih_material == 1:
            submenu_bata()
        elif pilih_material == 2:
            submenu_keramik()
        elif pilih_material == 0:
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Harap masukkan pilihan dengan benar!")


if __name__ == "__main__":
    main_menu()
