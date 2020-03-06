from turtle import *
import numpy as np
from random import randint

vmax = 25
xmax = 500
tmax = 100
t = 1
warna = ['gold', 'light green', 'black', 'violet', 'yellow', 'blue', 'green', 'sky blue', 'pink', 'red']
mobil1 = []
mobil2 = []
mobil3 = []


garis =  Turtle()

screen = Screen() # create the screen
screen.setup(xmax,xmax/2)
garis.hideturtle()
garis.penup()
garis.setposition(-xmax/2,40)
garis.pendown()
garis.forward(500)
turtles1 = [] # membuat list mobil di jalur 1garis.penup()
garis.penup()
garis.setposition(-xmax/2,10)
garis.pendown()
garis.forward(500)
turtles2 = [] # membuat list mobil di jalur 2
garis.penup()
garis.setposition(-xmax/2,-20)
garis.pendown()
garis.forward(500)


garis.penup()
garis.setposition(-xmax/2,120)
garis.pendown()
garis.forward(500)
garis.penup()
garis.setposition(-xmax/2,80)
garis.pendown()
garis.forward(500)
garis.color("black", "black")
garis.begin_fill()
garis.bk(500)
garis.goto(-xmax/2, 40)
garis.fd(500)
garis.goto(xmax/2, 80)   
garis.end_fill()


garis.color("red")
garis.penup()
garis.setposition(150,125)
garis.pendown()
garis.right(250)

garis.penup()
garis.setposition(200,125)
garis.pendown()
garis.right(250)


class IniMobil:
    def __init__(self, pos, jar, kec, lokasi):
        self.pos = pos
        self.mob = Turtle()
        self.jar = jar
        self.kec = kec
        self.mob.penup()
        self.lokasi = lokasi
        self.lewat = False
        self.ipos = pos
        self.waktu_lewat = []
        
    def setwarnamobil(self, warna):
        self.mob.color(warna)

    def setposisi(self, pos):
        self.pos = pos      

    def setjarak(self, jar):
        self.jar = jar

    def setkec(self, kec):
        self.kec = kec

    def getposisi(self):
        return self.pos

    def getjarak(self):
        return self.jar

    def getkecepatan(self):
        return self.kec

    def setposisiMobil(self, x, y):
        self.mob.hideturtle()
        self.mob.setposition(x, y)
        self.mob.showturtle()
        
    def mobilMaju(self, maju):
        self.mob.forward(maju)

    def update_kecepatan(self, kece, jarak):
        self.kec = kecepatan(kece, jarak)
        
    def mobil_pindah_jalur(self, lokasi, kec):
        self.lokasi = lokasi
        self.mob.setposition(self.pos, lokasi)
        self.kec = kec
        
    def tampil(self):
        print("Posisi : ", self.pos, "Jarak : ",self.jar, "Kecepatan : ", self.kec)
        return self.pos

    def sudahlewat(self, id_l):
        self.lewat = id_l

    def tambahlewat(self, waktu_l):
        if (self.lewat and self.pos >= self.ipos):
            self.waktu_lewat.append(waktu_l)
            self.lewat = False

    def hitungDT(self):
        for i in range (len(self.waktu_lewat)):
            if (i > 0):
                self.waktu_lewat[i] = self.waktu_lewat[i] - self.waktu_lewat[i-1]
                
        jumlah = 0
        
        for i in range (len(self.waktu_lewat)):
            jumlah = jumlah + self.waktu_lewat[i]

        avg_time = jumlah/len(self.waktu_lewat)

        print("Waktu rata-rata kembali ke titik awal adalah: ", avg_time)

    
def cek_index(a,b):
    if a >= b:
        return True
    else:
        return False
                        
def kepadatan(m):
    jumlah = 0
    for i in range(len(m)):
        if m[i].getposisi() >= 150 and m[i].getposisi() <= 200:
            jumlah+=1
    return jumlah

def sowingall(a):
    for i in range(len(a)):
        a[i].tampil()        
   

for i in range(10): #membuat 10 buah mobil
    mobil = IniMobil(0, 0, 0, 0)
    mobil1.append(mobil)
    mobil1[i].setwarnamobil(warna[i])

    mobil = IniMobil(0, 0, 0, 20)
    mobil2.append(mobil)
    mobil2[i].setwarnamobil(warna[i])

    mobil = IniMobil(0, 0, 0, 20)
    mobil3.append(mobil)
    mobil3[i].setwarnamobil(warna[i]) 

def cari_posisi(i,mob_pos):
    sama = -1
    for a in range(len(mob_pos)):
        if i == mob_pos[a].getposisi():
            sama = i
    return sama

def cek_pindah(v,d):
    if (v == d-1):
        return True
    else:
        return False

def kecepatan(v,d):
    v = min(v+1, vmax)
    v = min(v, d-1)
    if (v > 0):
        a = np.random.choice(2, 1, p=[0.7, 0.3])
        if (a==1):
            v = v - 1
    return v

def jarak_mobil(di, dj):
    if (di > dj):
        jarak = di - dj
    else:
        jarak = (xmax/2) - dj + ((xmax/2) + di)
    return jarak


def isi(a, sama, arr):
    if not sama:
        return a
    else:
        ini = randint(-xmax/2, xmax/2)
        return isi(ini, cek_posisi(ini, arr), arr)

def cek_posisi(i,mob_pos):
    sama = False
    for a in range(len(mob_pos)):
        if i == mob_pos[a].getposisi():
            sama = True
    return sama

for i in range(10):
    buat = randint(-xmax/2, xmax/2)
    buat2 = randint(-xmax/2, xmax/2)
    buat3 = randint(-xmax/2, xmax/2)
    mobil1[i].setposisi(isi(buat, cek_posisi(buat, mobil1), mobil1))
    mobil2[i].setposisi(isi(buat2, cek_posisi(buat2, mobil2), mobil2))
    mobil1[i].mob.setposition(mobil1[i].getposisi(), 0) #inisialisasi letak awal mobil
    mobil2[i].setposisiMobil(mobil2[i].getposisi(), 20)
    mobil3[i].setposisi(isi(buat3, cek_posisi(buat3, mobil3), mobil3))
    mobil3[i].setposisiMobil(mobil3[i].getposisi(), 100)
    

mobil1.sort(key=lambda x: x.pos, reverse=True)
mobil2.sort(key=lambda x: x.pos, reverse=True)
mobil3.sort(key=lambda x: x.pos, reverse=True)


for i in range(10): #inisialisasi jarak awal mobil
    if i == 0:
        d = 9
    else:
        d = i-1
    mobil1[i].setjarak(jarak_mobil(mobil1[d].getposisi(), mobil1[i].getposisi()))
    mobil2[i].setjarak(jarak_mobil(mobil2[d].getposisi(), mobil2[i].getposisi()))
    mobil3[i].setjarak(jarak_mobil(mobil3[d].getposisi(), mobil3[i].getposisi()))

for i in range(10):
    mobil1[i].setkec(kecepatan(0, mobil1[i].getjarak()))
    mobil2[i].setkec(kecepatan(0, mobil2[i].getjarak()))
    mobil3[i].setkec(kecepatan(0, mobil3[i].getjarak()))

sowingall(mobil1)
print("Mobil2")
sowingall(mobil2)

def pindah_jalur(posisi_x, next_line, v):
    cek = False
    for i in range(len(next_line)):
        if i == len(next_line)-1:
            n = 0
        else:
            n = i+1
        if next_line[i].getposisi() > posisi_x and next_line[n].getposisi() < posisi_x :
            gap_back = posisi_x - next_line[n].getposisi()
            gap_ahead = next_line[i].getposisi() - posisi_x
            if gap_back >= vmax and gap_ahead >= v:
                cek = True
    return cek

def update_jarak(input_mobil):
    for i in range(len(input_mobil)):
        if i == 0:
            d = len(input_mobil)-1
        else:
            d = i-1
        input_mobil[i].setjarak(jarak_mobil(input_mobil[d].getposisi(), input_mobil[i].getposisi()))
                        
def kecepatan_pindah (v, arr, poss):
    
   
    v = min(v+1, vmax)
    if (v > 0):
        a = np.random.choice(2, 1, p=[0.7, 0.3])
        if a==1:
            v = v - 1
    return v

def cari_index(arr, a):
    out = -1
    for i in range(len(arr)):
        if i == 0:
            sblm = len(arr)-1
        else:
            sblm = i-1
        if a.getposisi() >= arr[i].getposisi() and a.getposisi() < arr[sblm].getposisi():
            out = i
    return out

def delete_geser_insert(i, mob1, mob2):
    temp = mob1.pop(i)
    geser = cari_index(mob2, temp)
    mob2.insert(geser, temp)

def geser_array(arr, a):
    i = len(arr)-1
    while (i>a):
        arr[i] = arr[i-1]
        i-=1



def update(current_time):
    pergeseran = 0
    pergeseran2 = 0
    pindah1to2 = False
    pindah2to1 = False
    id_pindah_1to2 = 40
    id_pindah_2to1 = 40

    for i in range(20):
        i_sebelumnya = i
        if (pindah1to2 and id_pindah_1to2 <= i):
            pergeseran2+=1
        else:
            i = i+pergeseran2
        
        if (cek_index(len(mobil2)-1, i)):
            pindah2to1 = False
            mobil2[i].setposisi(mobil2[i].getposisi()+mobil2[i].getkecepatan())

            if mobil2[i].getposisi() > xmax/2:
                ini = -xmax/2 + ( mobil2[i].getposisi() - xmax/2)
                mobil2[i].setposisi(ini)
                mobil2[i].setposisiMobil(mobil2[i].getposisi(), 20)
                mobil2[i].sudahlewat(True)
            else:
                mobil2[i].mobilMaju(mobil2[i].getkecepatan())
                        
            update_jarak(mobil2)
            mobil2[i].tambahlewat(current_time)
            kec_sblm = mobil2[i].getkecepatan()
            mobil2[i].update_kecepatan(mobil2[i].getkecepatan(), mobil2[i].getjarak())
            kec_pindah = kecepatan_pindah(kec_sblm, mobil1, mobil2[i].getposisi())          
            
            if (cek_pindah(mobil2[i].getkecepatan(), mobil2[i].getjarak()) and pindah_jalur(mobil2[i].getposisi(),mobil1,kec_pindah)):
                
                nilai_pindah = mobil2[i].getposisi()
                mobil_pindah = mobil2[i]
                id_pindah_2to1 = cari_index(mobil1, mobil_pindah) 
                mobil2[i].mobil_pindah_jalur(0, kec_pindah)

                delete_geser_insert(i, mobil2, mobil1)

                update_jarak(mobil1)
                update_jarak(mobil2)
                
                pindah2to1 = True
                pergeseran2 =  pergeseran2 - 1
                if id_pindah_2to1 <= i:
                    pergeseran+=1

            i = i_sebelumnya
        
        i_sebelumnya = i
        if (pindah2to1 and id_pindah_2to1 <= i):
            pergeseran+=1
        else:
            i = i+pergeseran
        if (cek_index(len(mobil1)-1, i)):

            pindah1to2 = False
            
            mobil1[i].setposisi(mobil1[i].getposisi()+mobil1[i].getkecepatan())
            if mobil1[i].getposisi() > xmax/2:
                mobil1[i].setposisi(-xmax/2 + ( mobil1[i].getposisi() - xmax/2))
                mobil1[i].setposisiMobil(mobil1[i].getposisi(), 0)
              
                mobil1[i].sudahlewat(True)
            else:
                mobil1[i].mobilMaju(mobil1[i].getkecepatan())
            update_jarak(mobil1)
            mobil1[i].tambahlewat(current_time)
            kec_sblm = mobil1[i].getkecepatan()
            mobil1[i].update_kecepatan(mobil1[i].getkecepatan(), mobil1[i].getjarak())
            kec_pindah = kecepatan_pindah(kec_sblm, mobil2, mobil1[i].getposisi()) 

            if (cek_pindah(mobil1[i].getkecepatan(), mobil1[i].getjarak()) and pindah_jalur(mobil1[i].getposisi(),mobil2,kec_pindah)):


                nilai_pindah = mobil1[i].getposisi()
                mobil_pindah = mobil1[i]
                id_pindah_1to2 = cari_index(mobil2, mobil_pindah) 
                mobil1[i].mobil_pindah_jalur(20, kec_pindah)
                delete_geser_insert(i, mobil1, mobil2)
           
                update_jarak(mobil1)
                update_jarak(mobil2)
                
                pindah1to2 = True
                pergeseran-=1
          
            i = i_sebelumnya
    

def satu_jalur(one_time):
    
    for i in range(10):            
        mobil3[i].setposisi(mobil3[i].getposisi()+mobil3[i].getkecepatan())
        if mobil3[i].getposisi() > xmax/2:
            mobil3[i].setposisi(-xmax/2 + ( mobil3[i].getposisi() - xmax/2))
            mobil3[i].setposisiMobil(mobil3[i].getposisi(), 100)
            mobil3[i].sudahlewat(True)
        else:
            mobil3[i].mobilMaju(mobil3[i].getkecepatan())
        update_jarak(mobil3)
        mobil3[i].tambahlewat(one_time)
        mobil3[i].update_kecepatan(mobil3[i].getkecepatan(), mobil3[i].getjarak())
        

while(t <= 100):
    
    print("Kepadatan jalur 1 waktu", t," :", kepadatan(mobil1))
    print("Kepadatan jalur 2 waktu", t," :", kepadatan(mobil2))
    print("Kepadatan satu jalur waktu", t," :", kepadatan(mobil3))
    update(t)
    satu_jalur(t)
    t+=1

print("Dua jalur")
for i in range (len(mobil1)):
    mobil1[i].hitungDT()

    
for i in range (len(mobil2)):
    mobil2[i].hitungDT()

print("Satu Jalur")
for i in range (len(mobil3)):
    mobil3[i].hitungDT()
