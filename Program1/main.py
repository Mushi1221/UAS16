from model import daftar_nilai
from view import view_nilai

data = {'nama' : [], 'nilai' : []}
while True:
    print("[ (l)ihat, (t)ambah, (c)ari, (u)bah, (h)apus, (k)eluar ]\n ")
    tanya = input("Masukkan Pilihan : ")
    match tanya : 
        case "l":
            view_nilai.cetak_daftar_nilai(data)
        case "t":
            data = daftar_nilai.tambah_data(data)
        case "c" :
            view_nilai.cetak_daftar_nilai(data)
            if len(data['nama']) > 0:
                nama = input("Masukkan Nama mahasiswa yang akan dicari : ")
                data = daftar_nilai.ubah_data(data, nama)
        case "u":
            view_nilai.cetak_daftar_nilai(data)
            if len(data['nama']) > 0:
                nama = input("Masukkan Nama mahasiswa yang akan diubah : ")
                data = daftar_nilai.ubah_data(data, nama)
        case "h":
            view_nilai.cetak_daftar_nilai(data)
            if len(data['nama']) > 0:
                nama = input("Masukkan Nama mahasiswa yang akan di hapus : ")
                data = daftar_nilai.hapus_data(data, nama)
        case "k":
            print("Anda sudah keluar dari program")
            break
        case _:
            print("Tidak sesuai pilihan, silahkan pilih kembali!!\n")
            continue