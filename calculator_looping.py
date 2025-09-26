def kalkulator():   # calculator cli with looping, more efficient
    while True:
        print("===" * 6)
        print('MENU KALKULATOR')
        print("===" * 6)
        print("1. Tambah")
        print("2. Kurang")
        print("3. Perkalian")
        print("4. Pembagian")
        print('5. Keluar Program')
        print('===' * 6)
        x = (['1','2','3','4','5'])

        pilihan = input("Masukkan Pilihan 1/2/3/4/5 : " )

        if pilihan == '5' : # exit program
            print("Terimakasih 😊")
            break
        
        elif pilihan in x:
            
        
            try:
                a = int(input("Masukkan Angka pertama: ")) #angka
                b = int(input("Masukkan Angka kedua: "))
                
            except ValueError:
                print('\n''harus angka !!')
                continue


            if pilihan == '1':
                hasil = a + b
                print(f"Hasil pertambahan {a} + {b} adalah {hasil}")
                break
            
            elif pilihan == '2':
                hasil = a - b
                print(f" Hasil pengurangan {a} - {b} adalah {hasil}")
                break
            elif pilihan == '3':
                hasil = a * b
                print(f" Hasil perkalian {a} * {b} adalah {hasil}")
                break
            elif pilihan == '4':
                if b == 0:
                    print('tidak bisa dibagi 0')
                hasil = a / b
                print(f" Hasil pembagian {a} + {b} adalah {hasil}")
                break
        
        else:
            
            print("Tidak ada di pilihan")
            
                
            
        

kalkulator()


