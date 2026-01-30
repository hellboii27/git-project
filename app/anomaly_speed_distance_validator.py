from datetime import timedelta

KNOT_TO_MPS = 0.514444
NM_IN_METER = 1852
TOLERANSI_NM = 4.5


def hitung_dan_validasi_jarak():
    print("\n========================================")
    print("    ANOMALY SPEED DISTANCE VALIDATOR")
    print("========================================")

    # INPUT KECEPATAN
    v_knot_awal = float(input("Kecepatan awal (Knot) : "))
    v_knot_akhir = float(input("Kecepatan akhir (Knot) : "))

    # INPUT WAKTU
    waktu_awal_input = input("Waktu awal (Jam Menit Detik) : ")
    jam_1, menit_1, detik_1 = map(int, waktu_awal_input.split())
    waktu_awal = timedelta(hours=jam_1, minutes=menit_1, seconds=detik_1)

    waktu_akhir_input = input("Waktu akhir (Hari Jam Menit Detik) : ")
    hari_2, jam_2, menit_2, detik_2 = map(int, waktu_akhir_input.split())
    waktu_akhir = timedelta(days=hari_2, hours=jam_2, minutes=menit_2, seconds=detik_2)

    # SELISIH WAKTU
    selisih_waktu = waktu_akhir - waktu_awal
    t = selisih_waktu.total_seconds()

    if t <= 0:
        print("\n❌ ERROR: Waktu akhir harus lebih besar dari waktu awal!")
        return

    # KONVERSI SELISIH WAKTU KE JAM MENIT DETIK
    total_detik = int(t)
    jam = total_detik // 3600
    menit = (total_detik % 3600) // 60
    detik = total_detik % 60

    # KONVERSI KECEPATAN
    v1 = v_knot_awal * KNOT_TO_MPS
    v2 = v_knot_akhir * KNOT_TO_MPS

    # PERHITUNGAN
    a = (v2 - v1) / t
    s_meter = (v1 * t) + (0.5 * a * t ** 2)
    s_nm = s_meter / NM_IN_METER

    # INPUT JARAK APLIKASI
    jarak_aplikasi = float(input("Jarak pada aplikasi (Nm) : "))

    # VALIDASI
    selisih_nm = abs(jarak_aplikasi - s_nm)
    status = "NORMAL ✅" if selisih_nm <= TOLERANSI_NM else "TIDAK NORMAL ❌"

    # OUTPUT (FORMAT REVISI SESUAI PERMINTAAN)
    print("\n----------------------------------------")
    print(">> RINGKASAN PERHITUNGAN")
    print(f"Selisih waktu   : {jam:02} Jam {menit:02} Menit {detik:02} Detik")
    print(f"Jarak hitung    : {s_meter:,.1f} Meter ({s_nm:.1f} Nm)")
    print(f"Jarak aplikasi  : {jarak_aplikasi:.1f} Nm")
    print(f"Toleransi       : ± {TOLERANSI_NM} Nm")
    print("----------------------------------------")
    print(f"STATUS VALIDASI : {status}")
    print("----------------------------------------")


def main():
    while True:
        hitung_dan_validasi_jarak()

        ulang = input("\nHitung lagi? (Y/N): ").strip().lower()
        if ulang != 'y':
            print("\nPerhitungan selesai. Terima kasih.")
            break


# JALANKAN PROGRAM
main()
