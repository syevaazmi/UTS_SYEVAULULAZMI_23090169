def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input("Masukkan tahun: "))

if is_leap_year(year):
    print("tahun"(year, "merupakan TAHUN KABISAT"))
else:
    print("tahun"(year, "bukan TAHUN KABISAT"))
