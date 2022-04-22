def hitung_jumlah_keramik(panjang_lantai_meter, lebar_lantai_meter, pilihan_keramik, gap_semen, box_keramik, harga_box):
    # Konversi space dari meter ke centimeter
    panjang_lantai_cm = panjang_lantai_meter * 100
    lebar_lantai_cm = lebar_lantai_meter * 100

    # Menghitung keliling space
    keliling_space = panjang_lantai_cm * lebar_lantai_cm

    # Menghitung keliling keramik
    if pilihan_keramik == 1:
        keliling_keramik = (20 + gap_semen) * (20 + gap_semen)
    elif pilihan_keramik == 2:
        keliling_keramik = (30 + gap_semen) * (30 + gap_semen)
    elif pilihan_keramik == 3:
        keliling_keramik = (40 + gap_semen) * (40 + gap_semen)
    elif pilihan_keramik == 4:
        keliling_keramik = (45 + gap_semen) * (45 + gap_semen)
    elif pilihan_keramik == 5:
        keliling_keramik = (50 + gap_semen) * (50 + gap_semen)

    # Menghitung kebutuhan keramik
    jumlah_keramik = int(keliling_space / keliling_keramik)
    jumlah_box = int(jumlah_keramik / box_keramik)
    total_harga = int(harga_box * jumlah_box)

    print(f"Estimasi jumlah keramik yang diperlukan adalah {int(jumlah_keramik)}, sehingga anda perlu membeli sebanyak {int(jumlah_box)} dan membutuhkan dana sekitar Rp{total_harga:,}")