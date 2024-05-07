def main():
    total_items = int(input("Masukkan Jumlah Barang: "))
    total_price = 0

    for i in range(1, total_items + 1):
        price = float(input(f"Masukkan Harga Barang ke-{i}: "))
        total_price += price

    print("Total Belanjaan:", total_price)

if __name__ == "__main__":
    main()
