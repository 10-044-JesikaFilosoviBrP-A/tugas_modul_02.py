import random

class Robot:
    def __init__(self, nama, serangan, hp, akurasi, peluang_krit):
        self.nama = nama
        self.serangan = serangan
        self.hp = hp
        self.akurasi = akurasi  # Persentase keberhasilan serangan
        self.peluang_krit = peluang_krit  # Persentase serangan kritis
        self.terstun = False  # Status stun
    
    def serang_musuh(self, musuh):
        if self.terstun:
            print(f"{self.nama} terkena stun dan tidak bisa menyerang!")
            self.terstun = False  # Hanya stun satu ronde
            return
        
        if random.random() <= self.akurasi:
            kerusakan = random.randint(self.serangan - 5, self.serangan + 5)  # Variasi kerusakan

            musuh.hp -= kerusakan
            print(f"{self.nama} menyerang {musuh.nama} sebesar {kerusakan} kerusakan. HP {musuh.nama}: {musuh.hp}")
        else:
            print(f"{self.nama} gagal menyerang!")
    
    def regenerasi_hp(self):
        pemulihan = random.randint(5, 15)
        self.hp += pemulihan
        print(f"{self.nama} memulihkan {pemulihan} HP. HP saat ini: {self.hp}")
    
    def serangan_spesial(self, musuh):
        if random.random() < 0.3:  # 30% peluang untuk stun musuh
            musuh.terstun = True
            print(f"{self.nama} menggunakan serangan spesial! {musuh.nama} terkena stun!")
        else:
            print(f"{self.nama} mencoba serangan spesial, tetapi gagal!")

class Permainan:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
    
    def mulai(self):
        ronde = 1
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            print(f"\n--- Ronde {ronde} ---")
            
            aksi = random.choice(["serang", "regenerasi", "spesial"])
            if aksi == "serang":
                self.robot1.serang_musuh(self.robot2)
            elif aksi == "regenerasi":
                self.robot1.regenerasi_hp()
            elif aksi == "spesial":
                self.robot1.serangan_spesial(self.robot2)
            
            if self.robot2.hp <= 0:
                aksi = random.choice(["serang", "regenerasi", "spesial"])
                if aksi == "serang":
                    self.robot2.serang_musuh(self.robot1)
                elif aksi == "regenerasi":
                    self.robot2.regenerasi_hp()
                elif aksi == "spesial":
                    self.robot2.serangan_spesial(self.robot1)
            
            ronde += 1
        
        print("\nPermainan Selesai!")
        pemenang = self.robot1 if self.robot1.hp > 0 else self.robot2
        print(f"Pemenangnya adalah {pemenang.nama}!")

# Contoh permainan
robot_a = Robot("A", serangan=20, hp=100, akurasi=0.8, peluang_krit=0.2)
robot_b = Robot("B", serangan=18, hp=110, akurasi=0.85, peluang_krit=0.15)

permainan = Permainan(robot_a, robot_b)
permainan.mulai()
