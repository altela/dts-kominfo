def hitung_jumlah_bata(tembok, semen, panjang_meter, tinggi_meter):
    # Konversi tembok dari meter ke centimeter
    panjang_cm = panjang_meter * 100
    tinggi_cm = tinggi_meter * 100

    # Ukuran Bata dalam centimeter
    panjang_bata = 20
    tinggi_bata = 5

    # Menghitung jumlah bata yang diperlukan
    jumlah_bata = ((panjang_cm * tinggi_cm) / ((panjang_bata + semen) * (tinggi_bata + semen))) * tembok

    print("Estimasi jumlah bata yang diperlukan adalah", int(jumlah_bata))

def hitung_jumlah_batako(tembok, semen, panjang_meter, tinggi_meter):
    # Konversi Input Dari Meter ke Centimeter
    panjang_cm = panjang_meter * 100
    tinggi_cm = tinggi_meter * 100

    # Karakteristik Batako dalam centimeter
    panjang_batako = 40
    tinggi_batako = 20

    # Menghitung jumlah bata yang diperlukan
    jumlah_batako = ((panjang_cm * tinggi_cm) / ((panjang_batako + semen) * (tinggi_batako + semen))) * tembok

    print("Estimasi jumlah batako yang diperlukan adalah", int(jumlah_batako))