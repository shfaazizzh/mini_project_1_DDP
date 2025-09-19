# NAMA: NURUL SHAFA AZIZAH #
# NIM:2509116112 #
# SISTEM INFORMASI C #

masa_berlaku = []

while True:
    print("===== SISTEM DATA TAMBAHAN =====")
    print("1. tambah dokumen")
    print("2. tampilkan semua dokumen")
    print("3. mengubah data")
    print("4. hapus dokumen")
    print("5. keluar")

    pilihan = input("pilih dokumen (1/2/3/4/5): ")


    if pilihan == "1":
        if not masa_berlaku:
            print("belum ada dokumen")
        else:
            print("\n===== DAFTAR NAMA =====")
            data=masa_berlaku[0]
            print ("dokumen 2")
            print ("KTP/SIM", masa_berlaku[0][0])
            print ("masa berlaku", masa_berlaku[0][1])
            print ("kadaluwarsa", masa_berlaku[0][2])
            print ("\n dokumen 3")
            print ("KTP/SIM", masa_berlaku[0][0])
            print ("masa berlaku", masa_berlaku[0][1])
            print ("kadaluwarsa", masa_berlaku[0][2])


    elif pilihan == "2":
        print("\n===== tambah dokumen =====")
        KTP_SIM = input("Masukkan KTP/SIM: ")
        masa_aktif = input("Masukkan tanggal (YYYY-MM-DD):")
        kadaluwarsa = input("Masukkan tanggal kadaluwarsa (YYY-MM-DD): ")
        log = [KTP_SIM, masa_berlaku, kadaluwarsa]
        masa_berlaku.append(log)
        print("Dokumen berhasil ditambahkan!")

    elif pilihan == "3":
        KTP_SIM = input("Masukkan nama dokumen yang ingin diubah:")
        masa_aktif= input("Masukkan tanggal (YYYY-MM-DD) :")
        kadaluwarsa= input("Masukkan tanggal kadaluwarsa YYYY-MM-DD: ")
        print ("Dokumen berhasil diubah!")

    elif pilihan == "4":
        KT_SIM = input("Masukkan nama dokumen yang mau dihapus:")
        if "dokumen" in masa_aktif:
            del masa_aktif["dokumen"] 
            print("dokumen berhasil dihapus!")

    elif pilihan == "5":
     print("Terimakasih program berhenti.")
     break


    else:
        print("Pilihan tidak benar. Silahkan coba kembali.")

        


    