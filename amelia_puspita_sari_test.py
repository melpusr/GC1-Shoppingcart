import unittest
from amelia_puspita_sari_app import CartItem, ShoppingCart

class TestShoppingCart(unittest.TestCase): #Pengaturan awal yang dijalankan sebelum setiap tes
    def setUp(self): #untuk objek class ShoppingCart
        self.cart = ShoppingCart()
        self.item1 = CartItem("Item 1", 1000)
        self.item2 = CartItem("Item 2", 2000)
        self.item3 = CartItem("Item 3", 3000)
        '''
        class CartItem memiliki atribut itemName yaitu nama item dan atribut price 
        yaitu harga item. Dengan memasukkan CartItem dengan nama dan harga yang berbeda, 
        dapat diuji ke berbagai item dan harga yang berbeda. misal item 1 dengan harga 1000 dst.
        '''
    def test_addItem(self): #untuk uji addItem
        self.cart.addItem(self.item1) #tambah item1 ke cart
        self.assertEqual(len(self.cart.items), 1) #jumlah item yang ditambah ke cart itu 1
        self.assertEqual(self.cart.items[0].itemName, "Item 1") #memastikan item yang ditambah adalah item 1

        '''
        menggunakan 0 untuk 'Item 1' karena sesuai dengan index. 1 -> 0
        1 2 3
        0 1 2 -> index
        '''

    def test_removeItem(self): #untuk uji removeItem
        self.cart.addItem(self.item1) #tambah item1 ke cart
        self.cart.addItem(self.item2)   #tambah item2 ke cart
        self.cart.addItem(self.item3)   #tambah item3 ke cart

        self.cart.removeItem("Item 2") #kita coba hapus inputan item2 dari cart
        self.assertEqual(len(self.cart.items), 2) #memastikan jumlah item menjadi 2 di cart
        self.assertEqual(self.cart.items[1].itemName, "Item 3")

        '''
        untuk ini juga sama, misalkan kita ada 3 laci.
        1 2 3
        0 1 2 -> index

        kita ingin menghapus laci ke 2. maka dari itu, laci tsb dengan index 1 dimasukkan untuk di remove dalam 
        self.cart.items[1].
        item/laci ke 3 pun maju menjadi laci ke 2
        '''

    def test_totalItem(self): #untuk uji totalItem
        self.cart.addItem(self.item1) #tambah item1 ke cart
        self.cart.addItem(self.item2)   #tambah item2 ke cart
        self.cart.addItem(self.item3)   #tambah item3 ke cart

        total = self.cart.totalItem() #hitung total harga dari semua item dalam cart
        self.assertEqual(total, 6000) #memastikan hasil total sesuai yang di-expect, yaitu 6000 (dari 1000+2000+3000 = 6000)

if __name__ == "__main__": #jika script dijalankan sebagai program utama
    unittest.main(argv=[''], verbosity=5, exit=False)
    '''
    # Menjalankan unit test dengan verbosity level 2
    # argv=[''] digunakan untuk mengabaikan argumen baris perintah yang diberikan ke unittest
    # exit=False digunakan untuk mencegah unittest keluar setelah selesai dijalankan
    '''
