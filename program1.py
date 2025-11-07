def input_jam_mulai():
    jam = int(input("masukan jam:"))
    return jam
def input_menit_mulai():
    menit = int(input("masukan menit:"))
    return menit
def input_detik_mulai():  
    detik = int(input("masukan detik:"))
    return detik
def input_jam_akhir():
    jam_last = int(input("masukan jam:"))
    return jam_last
def input_menit_akhir():
    menit_last = int(input("masukan menit:"))
    return menit_last
def input_detik_akhir():
    detik_last = int(input("masukan detik:"))
    return detik_last
def selisih_jam(input_jam_akhir,input_jam_mulai):
    return input_jam_akhir - input_jam_mulai
def selisih_menit(input_menit_akhir,input_menit_mulai):
    return input_menit_akhir - input_menit_mulai
def selisih_detik( input_detik_akhir,input_detik_mulai):
    return input_detik_akhir - input_detik_mulai
def selisih_waktu(jam_mulai,menit_mulai,detik_mulai,jam_akhir,menit_akhir,detik_akhir):
    selisih_detik = detik_akhir - detik_mulai
    if  selisih_detik<0:
        selisih_detik+=60
        menit_akhir-=1
   
    selisih_menit = menit_akhir-menit_mulai
    if selisih_menit<0:
        selisih_menit+= 60
        jam_akhir-=1
    selisih_jam = jam_akhir- jam_mulai
    return selisih_jam,selisih_menit,selisih_detik
print("====data perubahan waktu===")
print("input mulai")
jam_mulai = input_jam_mulai()
menit_mulai = input_menit_mulai()
detik_mulai = input_detik_mulai()
print("input akhir")
jam_akhir = input_jam_akhir()
menit_akhir= input_menit_akhir()
detik_akhir= input_detik_akhir()
selisih_hour,selisih_minute,selisih_secound = selisih_waktu(jam_mulai,menit_mulai,detik_mulai,jam_akhir,menit_akhir,detik_akhir)
print(f"selisih waktu adalah {selisih_hour}jam {selisih_minute}menit {selisih_secound}detik")
print("terima kasih sudah mengakses")
print("selamat berjuang sukses ^-^")