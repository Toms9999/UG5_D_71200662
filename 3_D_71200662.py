import math

while True:
    jarakawal = input('Masukkan jarak awal (Dalam Meter): ')
    if jarakawal == 'Berhenti' or jarakawal == 'stop':
        break

    sudutpertama = input('Masukkan sudut elevasi pada menit ke-5 (Dalam derajat) : ')
    if sudutpertama == 'berhenti' or sudutpertama == 'stop':
        break

    sudutkedua = input('Masukkan sudut elevasi pada menit ke-6 (Dalam derajat) : ')
    if sudutkedua == 'berhenti' or sudutkedua == 'stop':
        break

    jarakawal = (float(jarakawal))
    sudutpertama = math.radians(float(sudutpertama))
    sudutkedua = math.radians (float(sudutkedua))

    tinggi_awal = jarakawal * math.tan(sudutpertama)
    jarak_akhir = jarakawal * math.tan(sudutkedua) - math.tan(sudutpertama)
    tinggi_akhir = jarak_akhir * math.tan(sudutkedua)
    
    selisih_ketinggian = tinggi_akhir - tinggi_awal
    
    print('Ketinggian drone pada menit ke-5 adalah', tinggi_awal, 'Meter')
    print("Selisih ketinggian helikopter adalah",selisih_ketinggian, "meter.")