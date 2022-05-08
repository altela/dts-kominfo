from menu_sub_bata import submenu_bata
from menu_sub_keramik import submenu_keramik


def main_menu():
    while True:
        print("\n========== Selamat Datang Di Program Hitung Material Bangunan ==========\n")
        print("Silahkan pilih kalkulasi yang anda perlukan :\n")
        print("1. Menghitung kebutuhan material bata atau batako")
        print("2. Menghitung kebutuhan material keramik lantai")
        print("0. Exit Program")
        pilih_submenu = int(input("\nHarap masukkan pilihan anda : "))
        if pilih_submenu == 1:
            submenu_bata()
        elif pilih_submenu == 2:
            submenu_keramik()
        elif pilih_submenu == 0:
            print("Keluar dari program. Terima kasih!\n")
            break
        else:
            print("Harap masukkan pilihan dengan benar!")


if __name__ == "__main__":
    main_menu()
