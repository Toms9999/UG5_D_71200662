def ganti_kata(kalimat, cari, ganti):
    k = kalimat.split()
    for i in range(len(k)):
        if k[i] == cari:
            k[i] = ganti
    kalimat_baru = ' '.join(k)
    return kalimat_baru

kalimat = str(input('Masukkan kalimat : '))
kata = str(input('Kata yang dicari : '))
ganti = str(input('Diganti menjadi : '))

kalimat_baru = ganti_kata (kalimat, kata, ganti)
print('Kalimat baru : ', kalimat_baru)
