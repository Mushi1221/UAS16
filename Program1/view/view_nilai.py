from tabulate import tabulate

def cetak_daftar_nilai(data):
    #Variabel i untuk membuat penomoran data ketika dibuat tabel
    i = range(1, len(data['nama'])+1)
    #Membuat list header kolom yang akan ditampilkan 
    headers = ["No", "Nama", "Nilai"]

    #Data dapat ditampilkan jika variabel data terisi minimal satu data
    if len(data['nama']) > 0:
        print(tabulate(data, headers, showindex=i, tablefmt="rounded_outline"))

    #Jika tidak ada data, maka tampilkan pesan 
    else :
        print("\nTidak ada Data\n")

def cetak_hasil_pencarian(dataMhs):
    print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))