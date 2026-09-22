from datetime import datetime

def pemesanan_hotel(jenis_kamar, lama_menginap):
    if jenis_kamar == "standard":
        harga = 200000
    elif jenis_kamar == "deluxe":
        harga = 350000
    else:
        return None

    total_biaya = harga * lama_menginap

    return total_biaya

print("PEMESANAN HOTEL")

jenis_kamar = input("masukkan jenis kamar (Standard/Deluxe): ")
checkin = input("masukkan tanggal checkin (dd-mm-yyyy): ")
checkout =input("masukkan tanggal checkout (dd-mm-yyyy): ")

tanggal_checkin = datetime.strptime(checkin, "%d-%m-%Y")
tanggal_checkout = datetime.strptime(checkout, "%d-%m-%Y")

lama_menginap = (tanggal_checkout - tanggal_checkin).days

total = pemesanan_hotel(jenis_kamar, lama_menginap)

print("DETAIL PEMESANAN")
print("jenis kamar :", jenis_kamar)
print("tanggal checkin :", tanggal_checkin)
print("tanggal checkout :", tanggal_checkout)
print("lama menginap :", lama_menginap, "malam")
print("total biaya : Rp", total)



