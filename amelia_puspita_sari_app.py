"""
========================
Graded Challenge 1

Nama    : Amelia Puspita Sari
Batch   : RMT-30

Program ini dibuat untuk evaluasi materi week 1 dengan menerapkan : 
- conditionals, 
- looping, 
- OOP, 
- functions 
- unit test
  dalam bentuk Shopping Cart yang simple. 
Program Shopping Cart ini akan terdiri dari 5 menu untuk menambahkan barang,
hapus barang, lihat total barang, menampilkan barang dan exit/keluar.
==========================
"""

print("Selamat datang di Toko Asanyo, selamat berbelanja!")

class ShoppingCart: 
    def __init__(self): #inisialisasi cart belanja 
        self.items = []   #dengan daftar item yang kosong, nantinya akan diinput user    

    def addItem(self, barang):
        item = (barang) #tambah item baru ke cart belanja
        self.items.append(item) #untuk menambahkan objek item ke dalam daftar items 
                                #yang dimiliki oleh class ShoppingCart
        
    def removeItem(self, itemName):  #hapus item dari cart berdasarkan 'itemName' dan hapus dari 'items'
        for item in self.items:
            if item.itemName == itemName:
                self.items.remove(item)
                break
        '''
        'for item' untuk mencari daftar 'items' yang memiliki nama sesuai dengan itemName. 
        item kemudian dihapus dari list dengan 'self.items.remove(item)'. 
        break digunakan untuk menghentikan loop menu no.2 setelah item yang sesuai selesai dihapus. 
        '''

    def totalItem(self): #hitung total harga dari semua item dalam keranjang
        totalItem = 0 # 0 sebagai nilai awal dari total harga
        for item in self.items:
            totalItem += item.price
        return totalItem
        #harga dari setiap item ditambahkan ke totalItem. Setelah semua item telah dijumlahkan, 
        #nilai totalItem yang dihitung akan dikembalikan sebagai total harga dari semua item 
        #dalam keranjang belanja.
        

class CartItem: #CartItem sebagai objek dengan nama dan harga
    def __init__(self, itemName, price):
        self.itemName = itemName
        self.price = price

def main(): #fungsi utama untuk menjalankan program dan untuk unittest nanti. jika tidak menggunakan def.main() python akan terus menerus meminta untuk menjalankan program dulu.
    cart = ShoppingCart() #cart berisi menu Shopping Cart (tambah barang, hapus barang dan hitung total), 
                            #berfungsi sebagai 'keranjang' belanja kita/user

    while True: #untuk menjalankan loop utama

    #misal, kita ingin user menginput sendiri
    #user_input = int(input("Masukkan harga barang: ")) -> nanti akan terus menerus meminta input
    #dan jika user ingin mengakhiri loop tersebut bisa dengan break.
    #if user_input.lower() == "exit": #dengan ,lower() tidak akan terdistraksi dengan upper maupun lowercase dari kata "exit"
    # break
        print("=====================")
        print("Menu: ")
        print("1. Menambah ke keranjang")
        print("2. Hapus item")
        print("3. Tampilkan keranjang saya")
        print("4. Lihat total item")
        print("5. Keluar")
        print("=====================")

        select = int(input("Pilih menu untuk melanjutkan: "))
        #user diminta untuk memilih salah satu menu untuk menjalankan program. pemakaian 'int' dikarenakan
        #kita ingin memasukan bilangan bulat (dalam hal ini nomor menu)

        '''
        selanjutnya kenapa pakai if-elif?
        -> karena ingin melihat beberapa kondisi berbeda secara berurutan dan menentukan tindakan 
            yang akan diambil berdasarkan pilihan menu oleh user.
        -> if-else tidak digunakan karena kita ingin menjalankan fungsi secara berurutan, sementara else 
            dipakai jika ada fungsi  yang berlawanan.
        '''
        
        if select == 1: #pilih menu 1 untuk tambah item ke cart
            itemName = input("Item apa yang ingin anda tambah?: ") #user menginput sendiri 
            price = int(input("Masukkan harga item yang ditambah: ")) #user menginput sendiri, menggunakan 'int' karena harga dalam bilangan bulat
            item = CartItem(itemName, price)
            #Fungsi untuk membuat objek CartItem.
            #itemName: nama item.
            #price: harga item.
            
            cart.addItem(item) #fungsi untuk menambahkan item ke dalam cart belanja
            print(f"{item.itemName} berhasil ditambahkan ke cart")

        elif select == 2: #pilih menu 2 untuk hapus item
            itemName = input("Pilih item yang akan dihapus: ") #user meng-input nama item yang akan dihapus
            cart.removeItem(itemName) #menghapus item dari cart belanja berdasarkan nama item
            print(f"{itemName} telah dihapus") 
            
        elif select == 3: #pilih menu 3 untuk tampilkan isi cart
            print("Isi cart saya: ") 
            for item in cart.items:  
                print(item.itemName, "-", item.price)
            '''
            mengapa memakai for item in cart.items?
            Setiap item dalam cart.items itu akan diakses dalam loop ini.
            Dalam soal ini, item.itemName memberikan akses ke nama item, sedangkan item.price 
            memberikan akses ke harga item. Dengan menggunakan loop for, nanti akan di-print
            item dan harganya secara berurutan.
            '''

        elif select == 4: #pilih menu 4
            total = cart.totalItem()
            print(f"Berikut total belanja anda: {total}")
            '''
            fungsi totalItem() berfungsi untuk menghitung total harga dari semua item 
            dalam cart belanja. Fungsi ini tidak diisi argumen, tetapi mengakses items 
            dari class ShoppingCart untuk mendapatkan daftar semua item. Fungsi tersebut akan
            melakukan iterasi melalui semua item dalam items, menambahkan harga setiap item ke total, 
            dan mengembalikan total harga keseluruhan.
            '''

        elif select == 5: #pilih menu 5
            print("Terima kasih telah berbelanja di toko kami!")
            break #digunakan untuk memberhentikan loop. Tanpa break, loop akan terus berlanjut .

if __name__ == "__main__":
    main()
    '''
    untuk menentukan apakah script phyton dijalankan secara langsung sebagai program 
    atau diimpor sebagai modul ke dalam script lain.
    '''




        


        


    




