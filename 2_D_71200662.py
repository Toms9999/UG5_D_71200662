def mobil():
    jumlahSol = 0
    jumlahSur = 0
    jumlahJog = 0
    jumlahMag = 0


    while True:
        asal = input ('Masukkan asal mobil (ketik "done" untuk keluar): ')
        asal = asal.lower()
        if asal == 'done':
            break
        elif asal == 'solo':
            jumlahSol += 1
            
        elif asal == 'surabaya':
            jumlahSur += 1
            
        elif asal == 'jogja':
            jumlahJog += 1
            
        elif asal == 'magelang':
            jumlahMag += 1

    print('Masukkan mobil dari Solo : ', jumlahSol)      
    print('Masukkan mobil dari Surabaya : ', jumlahSur)
    print('Masukkan mobil dari Jogja : ', jumlahJog)
    print('Masukkan mobil dari Magelang : ', jumlahMag)
mobil()










