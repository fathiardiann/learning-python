print("=== Simpel kalkulator CLI ===")
print("Pilih operasi :")
print ("1. Tambah (+)")
print ("2. Kurang (-)")
print ("3. Kali (*) ")
print ("4. Bagi (/) ")



pilihan_menu :float = float(input("Masukkan Pilihan (1/2/3/4) : "))
Angka_pertama :float = float(input("Masukkan Angka Pertama: "))
Angka_kedua = float(input("Masukkan Angka Kedua: "))


if pilihan_menu == 1:
    tambah = Angka_pertama + Angka_kedua
    print(f"Hasil : {Angka_pertama} + {Angka_kedua} = {tambah}")
    
elif pilihan_menu == 2:
    kurang = Angka_pertama - Angka_kedua
    print(f"Hasil: ",Angka_pertama , "-", Angka_kedua ,"=", kurang)
    
        
        
elif pilihan_menu == 3:
    kali = Angka_pertama * Angka_kedua
    print(f"Hasil: ",Angka_pertama , "*", Angka_kedua ,"=", kali)
elif pilihan_menu == 4:
    if Angka_kedua != 0:
         bagi = Angka_pertama / Angka_kedua
         print(f"Hasil: ",Angka_pertama , "/", Angka_kedua ,"=", bagi)
    else:
        print("tidak bisa dibagi 0")
else:
    print("PIlihan tidak valid")
    




# efficient way -->
# print(f"Hasil: {Angka_pertama} + {Angka_kedua} = {tambah}")



