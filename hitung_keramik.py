def hitung_jumlah_keramik(panjang_lantai_meter, lebar_lantai_meter, pilihan_keramik, gap_semen, box_keramik, harga_box):
    import math

    # Konversi space dari meter ke centimeter
    panjang_lantai_cm = float(panjang_lantai_meter * 100)
    lebar_lantai_cm = float(lebar_lantai_meter * 100)

    # Menghitung keliling space
    keliling_space = panjang_lantai_cm * lebar_lantai_cm

    # Menghitung keliling keramik
    if pilihan_keramik == 1:
        # Keramik ukuran 20 x 20
        keliling_keramik = float((20 + gap_semen)) * float((20 + gap_semen))
    elif pilihan_keramik == 2:
        # Keramik ukuran 30 x 30
        keliling_keramik = float((30 + gap_semen)) * float((30 + gap_semen))
    elif pilihan_keramik == 3:
        # Keramik ukuran 40 x 40
        keliling_keramik = float((40 + gap_semen)) * float((40 + gap_semen))
    elif pilihan_keramik == 4:
        # Keramik ukuran 45 x 45
        keliling_keramik = float((45 + gap_semen)) * float((45 + gap_semen))
    elif pilihan_keramik == 5:
        # Keramik ukuran 50 x 50
        keliling_keramik = float((50 + gap_semen)) * float((50 + gap_semen))

    # Menghitung kebutuhan keramik
    jumlah_keramik = int(math.ceil((keliling_space / keliling_keramik)))

    # Menghitung berapa jumlah box yang harus dibeli berdasarkan banyaknya keramik
    # Jika hasil bagi keramik dengan keramik per box memiliki sisa bagi, maka pembeli harus menambahkan 1 box untuk mengcover kebutuhan sisa
    # Jika hasik bagi tidak memiliki sisa, berarti tidak memerlukan tambahan 1 box untuk sisa kebutuhan keramik
    if jumlah_keramik % box_keramik == False:
        jumlah_box = int(jumlah_keramik / box_keramik)
    else:
        jumlah_box = int((jumlah_keramik / box_keramik) + 1) # +1 maksudnya adalah +1 box tambahan

    total_harga = int(harga_box * jumlah_box)

    print(f"\nEstimasi jumlah keramik yang diperlukan adalah {int(jumlah_keramik):,} pcs, sehingga anda perlu membeli sebanyak {int(jumlah_box)} box dan membutuhkan dana sebesar Rp{total_harga:,}")