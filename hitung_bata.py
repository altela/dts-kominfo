def hitung_jumlah_bata(tembok, semen, panjang_meter, tinggi_meter, harga):
    # Konversi tembok dari meter ke centimeter
    panjang_cm = panjang_meter * 100
    tinggi_cm = tinggi_meter * 100

    # Ukuran Bata dalam centimeter
    panjang_bata = 20
    tinggi_bata = 5

    # Menghitung jumlah bata yang diperlukan
    jumlah_bata = ((panjang_cm * tinggi_cm) / ((panjang_bata + semen) * (tinggi_bata + semen))) * tembok
    harga_total = int(jumlah_bata) * harga

    print(f"\nEstimasi jumlah bata yang diperlukan yaitu {int(jumlah_bata)} PCS dan membutuhkan dana sekitar Rp{harga_total:,}")

def hitung_jumlah_batako(tembok, semen, panjang_meter, tinggi_meter, harga):
    # Konversi Input Dari Meter ke Centimeter
    panjang_cm = panjang_meter * 100
    tinggi_cm = tinggi_meter * 100

    # Karakteristik Batako dalam centimeter
    panjang_batako = 40
    tinggi_batako = 20

    # Menghitung jumlah bata yang diperlukan
    jumlah_batako = ((panjang_cm * tinggi_cm) / ((panjang_batako + semen) * (tinggi_batako + semen))) * tembok
    harga_total = int(jumlah_batako) * harga

    print(f"\nEstimasi jumlah batako yang diperlukan yaitu {int(jumlah_batako)} PCS dan membutuhkan dana sekitar Rp{harga_total:,}")
