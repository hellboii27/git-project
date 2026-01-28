def fmt(x):
    return int(x) if x.is_integer() else x

def calculator():
    print("=== Python Calculator Sederhana ===")
    print("Pilih operasi:")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("0. Keluar")

    while True:
        pilihan = input("\nMasukkan pilihan (0-4): ")

        if pilihan == "0":
            print("Terima kasih, calculator ditutup 👋")
            break

        if pilihan not in ["1", "2", "3", "4"]:
            print("Pilihan tidak valid!")
            continue

        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))

        if pilihan == "1":
            hasil = a + b
            operator = "+"
        elif pilihan == "2":
            hasil = a - b
            operator = "-"
        elif pilihan == "3":
            hasil = a * b
            operator = "*"
        elif pilihan == "4":
            if b == 0:
                print("Error: pembagian dengan nol!")
                continue
            hasil = a / b
            operator = "/"

        print(f"Hasil: {fmt(a)} {operator} {fmt(b)} = {fmt(hasil)}")

calculator()
