def hitung_jumlah_bata(tembok, semen, panjang_meter, tinggi_meter, harga):
    import math

    # Konversi tembok dari meter ke centimeter
    panjang_cm = float(panjang_meter * 100)
    tinggi_cm = float(tinggi_meter * 100)

    # Ukuran Bata dalam centimeter
    panjang_bata = float(20)
    tinggi_bata = float(5)

    # Menghitung jumlah bata yang diperlukan
    jumlah_bata = int(math.ceil((panjang_cm * tinggi_cm) / ((panjang_bata + semen) * (tinggi_bata + semen))) * tembok)
    harga_total = jumlah_bata * harga

    print(f"\nEstimasi jumlah bata yang diperlukan yaitu {jumlah_bata} PCS dan membutuhkan dana sebesar Rp{harga_total:,}")

def hitung_jumlah_batako(tembok, semen, panjang_meter, tinggi_meter, harga):
    import math

    # Konversi Input Dari Meter ke Centimeter
    panjang_cm = float(panjang_meter * 100)
    tinggi_cm = float(tinggi_meter * 100)

    # Karakteristik Batako dalam centimeter
    panjang_batako = float(40)
    tinggi_batako = float(20)

    # Menghitung jumlah bata yang diperlukan
    jumlah_batako = int(math.ceil((panjang_cm * tinggi_cm) / ((panjang_batako + semen) * (tinggi_batako + semen))) * tembok)
    harga_total = jumlah_batako * harga

    print(f"\nEstimasi jumlah batako yang diperlukan yaitu {jumlah_batako} PCS dan membutuhkan dana sebesar Rp{harga_total:,}")
