from tabulate import tabulate
from view import input_nilai
from view import view_nilai

def tambah_data(data):
    newData = input_nilai.input_data(data)
    return data

def hapus_data(data, nama):
    if nama in data ['nama']:
        #buat dictionary kosong untuk menampilkan data yang cocok
        dataMhs = {}
        index = data['nama'].index(nama)

        #Lakukan pengisian data yang cocok ke dalam variabel otomatis
        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
        #Lakukan konfirmasi perghapusan
        confirm = input("Anda yakin ingin menghapus data ini?? (y/t)")

        #Jika input selain y atau t lakukan konfirmasi berulang
        while (confirm not in ['y', 't']):
            print("Input Salah")
            confirm = input("Anda yakin ingin menghapus data ini?? (y/t)")

        #Jika konfirmasi selesai dilakukan, maka hapus data mahasiswa pada variabel data
        if confirm =="y":
            for key in data.keys():
                data[key].pop(index)
            print("Data berhasil dihapus!!\n")
        return data
    
    else : 
        print("Data tidak ditemukan!!")

def ubah_data(data, nama):
    if nama in data['nama']:
        #Buat dictionary kosong untuk menampilkan data yang cocok
        dataMhs = {}
        index = data['nama'].index(nama)
        
        #Lakukan pengisian data yang cocok
        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        
        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
        #Lakukan input data yang akan diubah
        pilihan = input("Pilih field yang akan diubah : \n1.Nama\n2.Nilai\n")
        #Lakukan pengecekan pada variabel pilihan yang dikonversi menjadi nilai integer
        match int(pilihan):
            case 1:
                print("Data nama sebelumnya : " + dataMhs['nama'][0])
                nama = input("Masukkan nama baru : ")
                while nama in data ['nama']:
                    if nama == dataMhs['nama'][0]:
                        break
                    print("Mahasiswa dengan nama yang sama sudah ada")
                    nama = input("Masukkan nama baru : ")
                data['nama'][index] = nama

            case 2 :
                print("data nilai sebelumnya : ", dataMhs['nilai'][0])
                nilai = input("Masukkan nilai baru : ")
                data['nilai'][index] = nilai

        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
        return data
    else : 
        print("Data tidak ditemukan!!")

def cari_data(data, nama):
    dataMhs = {}
    if nama in data ['nama']:
        index = data['nama'].index(nama)
        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        view_nilai.cetak_hasil_pencarian(dataMhs)
    else :
        print("Data tidak ditemukan!!")
