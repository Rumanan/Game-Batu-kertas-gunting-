import random

list = ["Batu","Gunting","Kertas"]
print ("Game Suit")
print ("Batu","Gunting","Kertas")
player = (input("Masukan pilihan Anda :"))
print (f"kamu memilih : {player}")
com = random.choice (list)
print (f"computer memilih : {com}")

while True:
    
    if com == player:
        print ("seri")
        
    elif com == "Batu" and player == "Gunting":
        print ("Kamu Kalah")
        
    elif com == "Gunting" and player == "Kertas":
        print ("Kamu Kalah")
        
    elif com == "Kertas" and player == "Batu":
        print ("Kamu Kalah")
        
    else:
        print ("Kamu Menang")
    
    lanjut = input ("Apakah Mau lanjut y/n?")
    if lanjut == "n":
        break
    
print ("Program Selesai")
