def hitung_jumlah_keramik(panjang_lantai_meter, lebar_lantai_meter, panjang_keramik, lebar_keramik, gap_semen):
    # Konversi space dari meter ke centimeter
    panjang_lantai_cm = panjang_lantai_meter * 100
    lebar_lantai_cm = lebar_lantai_meter * 100

    # Menghitung keliling space
    keliling_space = panjang_lantai_cm * lebar_lantai_cm

    # Menghitung keliling keramik
    keliling_keramik = (panjang_keramik + gap_semen) * (lebar_keramik + gap_semen)

    # Menghitung kebutuhan keramik
    jumlah_keramik = keliling_space / (keliling_keramik + gap_semen)

    print("Estimasi jumlah keramik yang diperlukan adalah", int(jumlah_keramik))