import os
import sys
from random import randint

class Interface:
    def header(self):
        os.system('clear')
        print("-"*41)
        print(" "*15 + self.ColorText('Guess Games', 'blue'))
        print("-"*41)
        print("1. Board Size")
        print("2. Choose Cell")
        print("98. Refresh Board")
        print("99. Exit")
        print("-"*41)

    def mulai(self):
        self.header()
        self.pilihan_header = int(input("Masukkan Pilihan Anda: "))
        if self.pilihan_header == 1:
            self.jumlah_kolom = int(input("Masukkan Jumlah Kolom: "))
            self.jumlah_baris = int(input("Masukkan Jumlah Baris: "))
            self.generate_objek(self.jumlah_kolom, self.jumlah_baris)

    def keluar(self):
        print("Keluar dari game ....")
        sys.exit()

    def ColorText(self, text, color):
        CEND      = '\033[0m'
        CBOLD     = '\033[1m'
        CRED    = '\033[91m'
        CGREEN  = '\033[32m'
        CYELLOW = '\033[33m'
        CBLUE   = '\033[34m'
        CVIOLET = '\033[35m'
        CBEIGE  = '\033[36m'
        if color == 'red':
            return CRED + text + CEND
        elif color == 'green':
            return CGREEN + text + CEND
        elif color == 'yellow':
            return CYELLOW + text + CEND
        elif color == 'blue':
            return CBLUE + text + CEND 

class Game(Interface):
    def mulai(self):
        super().mulai()

    def mulai_ulang(self):
        self.header()
        if self.pilihan_header == 1:
            self.jumlah_kolom = int(input("Masukkan Jumlah Kolom: "))
            self.jumlah_baris = int(input("Masukkan Jumlah Baris: "))
            self.generate_objek(self.jumlah_kolom, self.jumlah_baris)

    def generate_objek(self, jumlah_kolom, jumlah_baris):
        self.skor = 0
        tipe_cell = ['regular_cell', 'mine_cell', 'bonus_cell']
        self.jawaban = {}
        self.board_show = []
        self.banyak_cell = jumlah_baris*jumlah_kolom
        for cell in range(1, self.banyak_cell+1):
            rand_cell = tipe_cell[randint(0,2)]
            self.jawaban[cell] = rand_cell
            self.board_show.append("x")
        self.show_objek(jumlah_kolom, jumlah_baris)

    def show_objek(self, jumlah_kolom, jumlah_baris, message = "", skor=0, list_tebakan=[]):
        self.header()
        self.skor = skor
        self.board_show
        print("Jumlah kolom {} (yang horizontal), Jumlah baris {} (yang vertikal)".format(jumlah_kolom, jumlah_baris))
        print(message)
        print("Score : {}".format(self.skor))
        #kolom itu kesamping
        for i in range(jumlah_kolom+1):
            if i == 0:
                print("  ", end="")
            elif i == jumlah_kolom:
                print(self.ColorText(str(i), 'green')) #diwarnain
            else:
                print(self.ColorText(str(i), 'green'), end="") #diwarnain
        #baris itu kebawah
        for i in range(jumlah_baris):
            for j in range(jumlah_kolom+1):
                if j == 0:
                    if i > 8:
                        print((self.ColorText(str(i+1), 'green')), end="") #diwarnain
                    else:
                        print((self.ColorText(str(i+1), 'green')), end=" ")
                elif j == jumlah_kolom:
                    print(self.board_show[(jumlah_kolom*i+j)-1])
                else:
                    print(self.board_show[(jumlah_kolom*i+j)-1], end="")
        self.check_selesai(list_tebakan)
        self.pilihan_header = int(input("Masukkan Pilihan Anda: "))
        if self.pilihan_header == 2:
            self.check_isi(list_tebakan)
        elif self.pilihan_header == 99:
            del self.list_tebakan[:] 
            self.keluar()
        elif self.pilihan_header == 1:
            self.list_tebakan = []
            del self.list_tebakan[:] 
            self.mulai_ulang()
        elif self.pilihan_header == 98:
            del self.list_tebakan[:] 
            self.generate_objek(self.jumlah_kolom, self.jumlah_baris)
        else:
            message = self.ColorText("Pilih yang bener", 'red')
            self.show_objek(self.jumlah_kolom, self.jumlah_baris, message)

    def check_isi(self, list_tebakan = []):
        pilih_kolom = int(input("Masukkan kolom yang akan dibuka: "))
        pilih_baris = int(input("Masukkan baris yang akan dibuka: "))
        index_board = (self.jumlah_kolom*(pilih_baris-1)+pilih_kolom)-1
        tebakan = str(pilih_kolom)+str(pilih_baris)
        self.list_tebakan = list_tebakan
        if tebakan in self.list_tebakan:
            # input("kombinasi kolom dan baris tersebut sudah terpilih")
            message = self.ColorText("Pilih Ulang (kombinasi kolom dan baris tersebut sudah terpilih)", 'red')
            self.show_objek(self.jumlah_kolom, self.jumlah_baris, message, self.skor)
        elif pilih_kolom > self.jumlah_kolom or pilih_baris > self.jumlah_baris:
            message = self.ColorText("Tolong pilih yang bener! Kolom sama barisnya ngga sampe segitu", "red")
            self.show_objek(self.jumlah_kolom, self.jumlah_baris, message, self.skor) 
        elif tebakan not in self.list_tebakan:
            list_tebakan.append(tebakan)
            if self.jawaban[index_board+1] == 'regular_cell':
                self.skor += 0
                self.board_show[index_board] = " "
                message = self.ColorText("Regular Cell", 'yellow')
            elif self.jawaban[index_board+1] == 'mine_cell':
                self.skor -= 10
                self.board_show[index_board] = self.ColorText("!", 'red') #kasih warna
                message = self.ColorText("Mine Cell - Explode", 'red')
            elif self.jawaban[index_board+1] == 'bonus_cell':
                self.skor += 10
                self.board_show[index_board] = self.ColorText("$", 'yellow') #kasih warna
                message = self.ColorText("Bonus Cell - Alhamdulillah", 'green')
        self.show_objek(self.jumlah_kolom, self.jumlah_baris, message, self.skor, self.list_tebakan)

    def check_selesai(self, list_tebakan):
        if len(list_tebakan) == self.jumlah_baris * self.jumlah_kolom:
            print(self.ColorText("Permainan Selesai", 'blue'))
            self.keluar()

guess_game = Game()
guess_game.mulai()
