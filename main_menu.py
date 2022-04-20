from submenu_bata import *


def main_menu():
    print("\n========== Selamat Datang Di Program Hitung Material ==========\n")
    print("Silahkan pilih kalkulasi yang anda perlukan :\n")
    print("1. Menghitung kebutuhan material bata atau batako")
    print("2. Menghitung kebutuhan material keramik lantai")
    print("0. Exit Program")
    pilih_material = int(input("\nHarap masukkan pilihan anda : "))
    if pilih_material == 1:
        submenu_bata()
    elif pilih_material == 2:
        pass
    elif pilih_material == 0:
        exit()
    else:
        pass


if __name__ == "__main__":
    main_menu()



