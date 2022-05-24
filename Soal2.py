'''Soal 2
Topik : Aplikasi data produk deskripsi
Deskripsi : Anda diminta untuk membuat aplikasi sederhana daftar produk.
            Aplikasi tersebut dapat melakukan 5 operasi sebagai berikut :
                - Lihat Daftar produk
                - Lihat Detail sebuah produk
                - Buat Produk
                - Edit Produk
                - Hapus Produk
'''
import json

'''Bentuk file yang akan digunakan adalah json dengan contoh  
{
    produk : [{namaproduk : "nama", deskripsi : "deskripsi", hargaproduk : int(hargaproduk), stok : int(stokproduk)}]
}
'''
def readFile(fileName):
    f = open(fileName, 'r')
    file = json.load(f)
    data = file['produk']
    return data

def saveFile(fileName, data):
    f = open (fileName, 'w')
    tup = {"produk" : data}
    json.dump(tup, f)
    print ("File telah berhasil disimpan")

def exists(data, namaproduk):
    for row in data :
        if row['namaproduk']== namaproduk :
            return True
    return False
def DaftarProduk(data):
    
    print ("Nama Produk : ", end = "")
    namaproduk = input()
    print ("Deskripsi Produk : ", end = "")
    deskripsi = input ()
    harga = int(input ("Harga Produk : "))
    while (harga<0):
        print ("Masukan harga salah")
        harga = int(input ("Harga Produk : "))
    stok = int(input ("Stok Produk : "))
    while (stok <0):
        print ("Masukan stok salah")
        stok = int(input ("stok Produk : "))
    if (not exists(data, namaproduk)):
        tup = {"namaproduk" : namaproduk, "deskripsi" : deskripsi, "harga" : harga, "stok":stok}
        data.append(tup)
        print ("Data berhasil ditambahkan")
    else :
        print ("Data gagal ditambahkan karena sudah ada produk dengan nama sama")

def lihatproduk(data, nama):
    for tupp in data :
        if tupp['namaproduk'] == nama :
            print ("Produk : ", tupp['namaproduk'])
            print ("Deskripsi Produk : ", tupp['deskripsi'])
            print ("harga : ", tupp['harga'])
            print ("Stok : ", tupp['stok'])
            return 1
    print ("Produk tidak ditemukan")
    return 0

def EditProduk(data):
    print ("Tuliskan nama produk yang akan diubah : ", end = "")
    namaproduk = input()
    print ("=================")
    exist = lihatproduk(data, namaproduk)
    print ("=================")
    if exist : 
        print ("Apa yang ingin anda ubah : ")
        print ("1. Nama Produk")
        print ("2. Deskripsi")
        print ("3. Harga")
        print ("4. Stok")
        print ("5. Cancel")
        choice = int(input())
        if choice == 1:
            print ("Nama Produk yang baru : ", end = "")
            namaproduknew = input()
            for row in data : 
                if row["namaproduk"] == namaproduk :
                    row["namaproduk"] = namaproduknew
        if choice ==2 :
            print ("Deskripsi yang baru : ", end = "")
            deskripsi = input()
            for row in data :
                if row["namaproduk"]==namaproduk :
                    row["deskripsi"] == deskripsi
        if choice ==3 :
            harganew = int(input("Masukkan harga baru : "))
            while harganew<0 :
                print ("Masukan harga salah")
                harganew =int(input("Masukkan harga baru : "))
            for row in data :
                if row["namaproduk"]==namaproduk :
                    row["harga"] == harganew
        if choice == 4 :
            stoknew = int(input("Masukkan stok baru : "))
            while stoknew<0:
                print ("Masukan stok salah")
                stoknew = int(input("Masukkan stok baru : "))
        if choice == 5 :
            pass
    else :
        pass
def DaftarsemuaProduk(data):
    for tupp in data :
        print ("Produk : ", tupp['namaproduk'])
        print ("Deskripsi Produk : ", tupp['deskripsi'])
        print ("harga : ", tupp['harga'])
        print ("Stok : ", tupp['stok'])
        print ("========================")
def DeleteProduk(data, nama):
    for i in range (len(data)):
        if (data[i]["namaproduk"] == nama ):
            del(data[i])
def Main(data):
    print ("=================")
    print ("Pilihan Menu : ")
    print ("1. Daftar Semua Produk")
    print ("2. Daftarkan Produk")
    print ("3. Lihat Produk")
    print ("4. Edit Produk")
    print ("5. Delete Produk")
    print ("6. export File")
    print ("7. Import File")
    print ("8. Exit")
    print ("Masukkan pilihan : ", end = "")
    choice = int (input())
    print ("=================")
    while (choice != 8):
        if choice == 1 :
            DaftarsemuaProduk(data)
        elif choice == 2 :
            DaftarProduk(data)
        elif choice == 3 :
            print ("Nama Produk yang ingin anda cari : ", end = "")
            namaproduk = input()
            lihatproduk(data, namaproduk)
        elif choice == 4 :
            EditProduk(data)
        elif choice == 5 :
            print ("Nama Produk yang akan anda hapus : ")
            namaproduk = input ()
            DeleteProduk(data, namaproduk)
        elif choice == 6 :
            print ("Masukkan nama file tempat data anda akan disimpan : ", end = "")
            filename = input ()
            saveFile(filename, data)
        elif choice == 7 : 
            print ("Masukkan nama file tempat data anda akan disimpan : ", end = "")
            filename = input ()
            readFile(filename)
        elif choice == 8 :
            break
        else : 
            print ("Masukan perintah tidak benar")
        print ("=================")
        print ("Pilihan Menu : ")
        print ("1. Daftar Semua Produk")
        print ("2. Daftarkan Produk")
        print ("3. Lihat Produk")
        print ("4. Edit Produk")
        print ("5. Delete Produk")
        print ("6. export File")
        print ("7. Import File")
        print ("8. Exit")
        print ("Masukkan pilihan : ", end = "")
        choice = int (input())
        print ("=================")

fulldata = []
Main(fulldata)