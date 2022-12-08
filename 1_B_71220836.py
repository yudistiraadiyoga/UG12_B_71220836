print('SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG')
count = int(input('Masukkan Angka :'))
print(' '*(count-2),'*')
for lubang in range ((count-2),0,-1):
    print(' '*(lubang-1),'**')
print('*'*count*2-1)