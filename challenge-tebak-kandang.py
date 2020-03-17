import os
import sys
from random import sample, randint

class Board:
    def input_kandang(self):
        self.header()
        jumlah = input('Masukkan jumlah kandang :')
        self.show_kandang(int(jumlah))
    
    def generate_kandang(self, jumlah, guess_num, guess):
        binatang = ['K', 'B', 'Z']
        jawaban = {}
        pattern = ""
        pattern_angka = ""
        bener = 0
        for i in range(1, jumlah+1):
            rand_binatang = binatang[randint(0,2)]
            pattern += "|||\n|{}|\n|||\n\n".format(rand_binatang)
            jawaban[i] = rand_binatang
            pattern_angka += "|||\n|{}|\n|||\n\n".format(i)
        self.header()
        print(self.ColorText("-------Percobaan Buka-------", 'yellow'))
        print(pattern_angka.replace(str(guess_num), (self.ColorText(guess, 'yellow'))))
        input()
        while bener <= jumlah:
            if jawaban[guess_num] == guess:
                print(self.ColorText('Tebakan Benar!', 'green'))
                pattern_angka = pattern_angka.replace(str(guess_num), guess)
                print(pattern_angka)
                bener += 1
                if bener == jumlah:
                    print(self.ColorText("-------Selamat Anda Menebak Semua Kandang!-------", 'green'))
                    break
            else:
                print(self.ColorText('Tebakan Salah!', 'red'))
                print(pattern_angka)
            guess_num = int(input("Pilih kandang yang ingin dibuka: "))
            print("---PILIHAN---")
            print(self.ColorText('K', 'blue') + ': Kambing')
            print(self.ColorText('Z', 'red') + ': Zebra')
            print(self.ColorText('B', 'yellow') + ': Bebek')
            guess = input('Masukkan tebakan: ')
            self.header()
            print(self.ColorText("-------Percobaan Buka-------", 'yellow'))
            print(pattern_angka.replace(str(guess_num),(self.ColorText(guess, 'yellow'))))
            input()

    def show_kandang(self, jumlah):
        pattern = ""
        for i in range(1, jumlah+1):
            pattern += "|||\n|{}|\n|||\n\n".format(i)
        print(pattern)
        guess_num = int(input("Pilih kandang yang ingin dibuka: "))
        print("---PILIHAN---")
        print(self.ColorText('K', 'blue') + ': Kambing')
        print(self.ColorText('Z', 'red') + ': Zebra')
        print(self.ColorText('B', 'yellow') + ': Bebek')
        guess = input('Masukkan tebakan: ')
        self.header()
        self.generate_kandang(jumlah, guess_num, guess)
    
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

class TebakKandang(Board):
    def header(self):
        os.system('clear')
        print("-"*30)
        print(" "*8, self.ColorText('Tebak Kandang', 'blue'))
        print("-"*30)

    def mulai(self):
        self.header()
        print("1. Jumlah Kandang")
        print("99. Exit")
        pilihan_mulai = input("Pilih menu: ")
        if pilihan_mulai == "1":
            self.input_kandang()
        elif pilihan_mulai == "99":
            self.keluar()

    def keluar(self):
        self.header()
        print("Keluar dari tebak kandang .....")

coba = TebakKandang()
coba.mulai()