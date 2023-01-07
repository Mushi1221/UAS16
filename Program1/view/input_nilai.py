def input_data(data):
    #Buat inputan mengisi nama 
    nama = input("Masukkan Nama : ")
    while len(nama) < 3:
        nama = input ("Masukkan Nama : ")
    
    #Jika NIM yang di input tersedia pada variabel data, cetak pesan lalu lakukan input ulang
    while nama in data['nama']:
        print("Mahasiswa dengan nama yang sama sudah ada")
        nama = input("Masukkan Nama : ")
    
    nilai = input("Masukkan Nilai : ")
    while not nilai.isnumeric():
        nilai = input("Masukkan Nilai : ")
    
    data['nama'].append(nama)
    data['nilai'].append(int(nilai))
    print("Data berhasil ditambah")
    return data