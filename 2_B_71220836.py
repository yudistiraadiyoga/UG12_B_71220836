print('~ Selamat Datang di Kalkulator Sederhana ~')
cho = input('Masukkan operator matematika yang ingin Anda hitung : ')
while True:
    if cho == '+':
        num1 = int(input('Mau penjumlahan berapa : '))
        num2 = int(input('Print berapa banyak : '))
        for i in range(num2):
            print(f'{i+1} + {num2-i} = {(i+1)+(num2-i)}')
    elif cho == '-':
        num1 = int(input('Mau pengurangan berapa : '))
        num2 = int(input('Print berapa banyak : '))
        for i in range(num2):
            print(f'{i+1} + {num2-i} = {(i+1)-(num2-i)}')
    elif cho in ('x', 'X'):
        num1 = int(input('Mau perkalian berapa : '))
        num2 = int(input('Print berapa banyak : '))
        for i in range(num2):
            print(f'{i+1} X {num2-i} = {(i+1)*(num2-i)}')
    elif cho == ':':
        num1 = int(input('Mau pembagian berapa : '))
        num2 = int(input('Print berapa banyak : '))
        for i in range(angka2):
            print(f'{i+1} : {num2-i} = {(i+1)/(num2-i)}')
    else:
        print('Maaf, Operator Matematika yang Anda cari  belum tersedia.')
        break
    end = input('Apakah Anda Ingin Menghitung Lagi? (Y/T): ')
    if end == t:
        print('Terima Kasih dan Sampai Jumpa Lagi!')
        break
    elif end == y:
        continue
    else:
        print('ERROR\nPilih Y atau T\nUlangi Program')
        break