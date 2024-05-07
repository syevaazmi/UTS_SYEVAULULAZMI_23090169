def main():
    print("-Program Operasi Bilangan-")
    num1 = float(input("Masukkan bilangan pertama: "))
    num2 = float(input("Masukkan bilangan kedua: "))

    addition = num1 + num2
    subtraction = num1 - num2
    modulus = num1 % num2

    print(f"Hasil penjumlahan: {addition}")
    print(f"Hasil pengurangan: {subtraction}")
    print(f"Hasil modulus: {modulus}")

if __name__ == "__main__":
    main()
