nama = input("Masukan nama pelanggan            :")
hari = input("Jenis hari (biasa / akhir pekan)  :").lower()
studio = input("Jenis studio (regural / vip)    :").lower()
jumlah = int(input("Jumlah tiket                :"))

if hari == "biasa":
    harga_tiket = 35000
elif hari == "akhir pekan":
    harga_tiket = 50000
else:
    print("jenis hari tidak valid!")
    exit()

if studio == "regural":
    tambahan = 0
elif studio == "vip":
    tambahan = 25000
else:
    print("jenis studio tidak valid!")
    exit()

total = (harga_tiket + tambahan) * jumlah

if jumlah >= 5:
    diskon = total * 10 / 100
else:
    diskon = 0

total_bayar = total - diskon

print("\n======= STRUK PEMBELIAN TIKET =======")
print("Nama Pelanggan       :", nama)
print("Jenis Hari           :", hari.title())
print("Jenis Studio         :", studio.upper())
print("Jumlah Tiket         :", jumlah)
print("Harga Tiket          :", (harga_tiket), "per tiket")
print("Biaya Studio         :", (tambahan), "per tiket")
print("Total                :", (total))
print("Diskon               :", (diskon))
print("Total Bayar          :", (total_bayar))



