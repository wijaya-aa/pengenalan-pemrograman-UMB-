#buatlah coding dengan output sebagai barikut
#npm (2355201078)

import datetime; #import waktu
x=datetime.datetime.now()



no= float(input("masukan nomor struk"))
nama= input("masukan nama anda")
 

barang1=input("masukan nama barang 1 ")
hargabarang1=input("masukan harga barang 1")

barang2=input("masukan nama barang 2 ")
hargabarang2=input("masukan harga barang 2")

barang3=input("masukan nama barang 3 ")
hargabarang3=input("masukan harga barang 3")

print("------------------------------")

totalbayar= int(hargabarang1) + int(hargabarang2) + int(hargabarang3)
print("Total Bayar Rp :",totalbayar)
print("\n")
print("Bali,%a/%a/%a"%(x.day, x.month, x.year)) #ini syntax 
print("kasir :")
print(nama)
print("TERIMA KASIH SUDAH BERBELANJA DI TOKO KAMI")

#nama kasir
#barang 1
#harga barang 1
#barang 2
#harga barang 2
#barang 3 
#harga barang 3

#total bayar 
#(tambahakan karakter new line)
#3TERMIA KASIH SUDAH BERBELANJA DI TOKO KAMI